write_somthing = input("please write somthing(space them out):  ")
numbers = []
the_2=0
the_1=0
for n2 in write_somthing:
    if n2.isdigit():
        numbers.append(int(n2))


total = 0
for n4 in numbers:
    total += n4
print(f"مجموع الارقام ={total}")




