import pylab

def find_payment(loan, r, m):
    """loan と r を float型 とし, m を int型 とする
       月割の金利を r として借入額 loan の住宅ローンを
       mヶ月で返済する場合の毎月の返済額を返す"""

    return loan * ((r* (1+r)**m) / ((1+r)**m - 1))

class Mortgage(object):
    """異なる住宅ローンを扱うための抽象クラス"""

    def __init__(self, loan, ann_rate, months):
        self.loan = loan
        self.rate = ann_rate / 12.0
        self.month = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = find_payment(loan, self.rate, months)
        self.legend = None

    def make_payment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1] * self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def get_total_paid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend

    def plot_payments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)

    def plot_balance(self, style):
        pylab.plot(self.outstanding, style, label=self.legend)

    def plot_total_paid(self, style):
        total_paid = [self.paid[0]]
        for i in range(1, len(self.paid)):
            total_paid.append(total_paid[-1] + self.paid[i])
        pylab.plot(total_paid, style, label=self.legend)

    def plot_net(self, style):
        total_paid = [self.paid[0]]
        for i in range(1, len(self.paid)):
            total_paid.append(total_paid[-1] + self.paid[i])
        equity_acquired = pylab.array([self.loan] * len(self.outstanding))
        equity_acquired = equity_acquired - pylab.array(self.outstanding)
        net = pylab.array(total_paid) - equity_acquired
        pylab.plot(net, style, label=self.legend)


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%'

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend = 'Fixed, ' + str(r * 100) + '%, ' + str(pts) + ' points'

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_month):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self.teaser_month = teaser_month
        self.teaser_rate = teaser_rate
        self.next_rate = r/12.0
        self.legend = str(teaser_rate * 100) + '% for ' + str(self.teaser_month) + ' months, then ' + str(r*100) + '%'

    def make_payment(self):
        if len(self.paid) == self.teaser_month + 1:
            self.rate = self.next_rate
            self.payment = find_payment(self.outstanding[-1], self.rate, self.month - self.teaser_month)
        Mortgage.make_payment(self)

def compare_mortgages(amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months):
    total_months = years * 12
    fixed1 = Fixed(amt, fixed_rate, total_months)
    fixed2 = FixedWithPts(amt, pts_rate, total_months, pts)
    two_rate = TwoRate(amt, var_rate2, total_months, var_rate1, var_months)
    morts = [fixed1, fixed2, two_rate]
    for m in range(total_months):
        for mort in morts:
            mort.make_payment()
    plot_mortgages(morts, amt)

def plot_mortgages(morts, amt):
    def label_plot(figure, title, xlabel, ylabel):
        pylab.figure(figure)
        pylab.title(title)
        pylab.xlabel(xlabel)
        pylab.ylabel(ylabel)
        pylab.legend(loc='best')
    styles = ['k-', 'k-', 'k:']

    payments, cost, balance, net_cost = 0, 1, 2, 3
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plot_payments(styles[i])
        pylab.figure(cost)
        morts[i].plot_total_paid(styles[i])
        pylab.figure(balance)
        morts[i].plot_balance(styles[i])
        pylab.figure(net_cost)
        morts[i].plot_net(styles[i])

    label_plot(payments, 'Monthly Payments of $' + str(amt) + ' Mortgages', 'Months', 'Monthly Payments')
    pylab.savefig('mortgage/payments')
    label_plot(cost, 'Cash Outlay of $' + str(amt) + ' Mortgages', 'Months', 'Total Payments')
    pylab.savefig('mortgage/cost')
    label_plot(balance, 'Balance Remaining of $' + str(amt) + ' Mortgages', 'Months', 'Remaining Loan Balance of $')
    pylab.savefig('mortgage/balance')
    label_plot(net_cost, 'Net Cost of $' + str(amt) + ' Mortgages', 'Months', 'Payments - Equity $')
    pylab.savefig('mortgage/net_cost')

compare_mortgages(
    amt=200000,
    years=30,
    fixed_rate=0.07,
    pts=3.25,
    pts_rate=0.05,
    var_rate1=0.045,
    var_rate2=0.095,
    var_months=48
)
