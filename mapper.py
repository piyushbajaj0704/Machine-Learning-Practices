import sys
output={}


for line in sys.stdin:
   temp=line.strip().split('\t')

   temp.sort()
   # count the occurrences of all the single items
   for item in temp:
      if item in output:
         output[item]+=1
      else:
         output[item]=1


   #count the occurrences of each pair of items
   for i in range(len(temp)):
      for j in range(i+1,len(temp)):
         key=temp[i]+'-'+temp[j]
         if key in output:
            output[key]+=1
         else:
            output[key]=1

for data in output.items():
   print data[0]+'\t'+data[1]
