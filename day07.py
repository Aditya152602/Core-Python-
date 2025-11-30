#BREAK AND CONTINUE
for i in range (1,50,1):
     print(i,end=" ")
     if(i==50):
         break
else:
     print("Mississippi")
print("Thank You")    
for i in [2,3,4,5,6,7,8,0]:
     if (i%2!=0):
         continue
     print(i)