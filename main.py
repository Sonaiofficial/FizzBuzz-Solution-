#Write your code below this row 👇
#take i as a veriable and start from 0
i=0
# here we take the range for fizz buzz is 1-100
for numbers in range(1, 101):
# we tart i from 1 and check if the i is divisble by 3 , 5 or both at a time ad the print statement derive as per the condition matched
  i += 1
  if (i % 3==0 and i % 5==0):
    print("FizzBuzz")
  elif i % 3==0:
    print("Fizz")
  elif i % 5==0:
    print("Buzz")
  else:
    print(i)
  
 

