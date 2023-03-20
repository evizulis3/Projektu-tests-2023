sk=int(input("Ievadi skaitli (0-beigt):"))

summa=0
skaits=1

while sk !=0:
    summa+=sk
    skaits+=1
    sk=int(input("Ievadi skaitli (0-beigt):"))
print("Visu ievadito skaitlu aritmetiskais videjais ir",
summa/skaits)