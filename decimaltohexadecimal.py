num = int (input("enter the number"))
temp = num
hexa = []
result = []
while (temp!= 0):
    rem = temp%16
    if rem < 10:
        hexa.append(chr(rem +48))
    else:
        hexa.append(chr(rem + 55))
    temp = int(temp/16)
j = 1
for i in hexa :
    result.append(hexa[len(hexa) - j])
    j = j+1
print(result)