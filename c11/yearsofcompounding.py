import pylab
principal = 10000
interest_rate = 0.05
years = 20
values = []
for i in range(years+1):
    values.append(principal)
    principal += principal * interest_rate
pylab.plot(values)
pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')
pylab.savefig('yearsofcompounding/years_of_compounding')