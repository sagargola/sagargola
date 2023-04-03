Secret_number = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess = int(input("guess the number"))
  guess_count+= 1
  if guess == Secret_number:
    print("you won")
    break
else:
    print("you failed")


