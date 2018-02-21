import datetime 
now=datetime.datetime.now ()

print "Today's date is "+ now.strftime("%Y-%m-%d ") + "and the day is " +now.strftime ("%A")
from datetime import date
today = date.today()
mera=date(today.year, today.month, today.day).weekday()
sum=0
for i in range (1,11):
    if mera==date(today.year +i, today.month, today.day).weekday():
        sum=sum+1 #athroisma poswn etwm tha einai akribws idia mera kai hmeromhnia ektos tou etous
        print 'Same date at: '
        print date(today.year+i, today.month, today.day) #emfanizei poia xronologia tha einai

print "Number of same dates:" 
print sum #emfanizei to athroisma
