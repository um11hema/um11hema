#leap year

year=int(input ("Enter the year:"))
                
if (year%4==0): 
  if(year%100==0):
   if(year%400):
      print (year,"is a leap year")
else: 
   print (year,"is not a leap year")
  

   print (2016,"is leap year") 
   print (year,"Not a leap year")