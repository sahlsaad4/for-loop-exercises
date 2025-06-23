write_somthing= input("please write somthing(space them out):  ")
#حساب عدد الحروف فقط بدون الارقام
counter_of_letters=0
for letters in write_somthing:
    number= letters.isdigit()
    if letters  !=" " and not number:
        counter_of_letters+=1


print(f"عدد الحروف = {counter_of_letters}")
