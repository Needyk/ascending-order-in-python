import time
Numbers = []
while True:
    a = input("to enter a number simply enter a number to finish enter q: ")
    if 'q' not in a:
        Numbers.append(a)
    else: 
        break
Numbers.sort()
print(Numbers)
time.sleep(10)