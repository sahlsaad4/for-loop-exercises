write_somthing= input("please write somthing(space them out):  ")

numbers=[]
for n2 in write_somthing:
    if n2.isdigit():
        numbers.append(int(n2))

the_2=0
the_1=0

for n3 in numbers:
    if n3%2==0:
        the_2+=1
    if n3 %2!=0:
        the_1+=1
print(f"عدد الارقام الزوجية{the_2}")
print(f"عدد الارقام الفردية{the_1}")
