import random

def generate(length):
  symbol = 0
  lower = 0
  upper = 0
  number = 0
  count = 0
  password = []

  
#length = input("Please Enter Desired Password Length (default 16)\n")
#length = 16 if length == '' else int(length)

#randomly select ascii character classes and individual characters

  while count < length:
      rand = random.randint (0,3)
      if rand == 0:
          lower += 1
          b = int(random.randint (97,123))
          password.append(b)
      elif rand == 1:
          upper += 1
          b = random.randint (65,91)
          password.append(b)
      elif rand == 2:
          number += 1
          b = random.randint (48,58)
          password.append(b)
      elif rand == 3:
          r = random.randint(0,2)
          symbol += 1
          if r == 0:
              b = random.randint (33,48)
              password.append(b)
          elif r == 1:
              b = random.randint (91,97)
              password.append(b)
          elif r == 2:
              b = random.randint (123,126)
              password.append(b)
      count += 1

  #convert ascii code to characters
  word = "".join([chr(c) for c in password])

  #print the result
  #print ("Random password of length %s is: \n" % length)

  #print('******')
  return word
  #print('******')
  
  contains = ("\nThis Password contains",lower,"lowercase,",upper,"uppercase,",number,"numbers and",symbol,"symbol characters")
  return contains
