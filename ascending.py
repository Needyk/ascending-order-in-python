import time
Numbers = []
while True:
    a = input("to enter a number simply enter a number to finish enter Q: ")
    if 'Q' not in a:
        Numbers.append(a)
    else: 
        break
Numbers.sort()
print(Numbers)
time.sleep(10)
