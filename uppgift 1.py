while True:
       year = int(input("Enter year:"))

       if not 1583 <= year <= 9999:
              print ("Out of allowed range 1583 - 9999")
              
else:
break

month = int(input ("Enter month:"))
while True:
       if not 1 <= month <= 12:
              print ("Out of allowed range 1 - 12")

else:
       False

if month == 1 or month == 2:
       month += 12
       year -=1
       
while True:
       day = int(input ("Enter day: "))
if not 1 <= day <= 30:
       print ("Out of allowed range 1 - 30")
else:
       False

weekday = ( day + 13*(month+1)//5 + year + year//4 - year//100 + year//400 ) % 7

print ("It it a " + weekday)

