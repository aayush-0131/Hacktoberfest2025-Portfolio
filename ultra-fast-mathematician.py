
x = input().strip()
y = input().strip()
result = ""
for i in range(len(x)):
    if x[i] != y[i]:
        result += "1"
    else:
        result += "0"
print(result)
