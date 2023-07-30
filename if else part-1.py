user1 = input("enter the user1 age: ")
user2 = input("enter the user2 age: ")
user3 = input("enter the user3 age: ")
if user1>user2:
  if user1>user3:
    print("user1 is oldest ")
  else:
    print("user3 is oldest")
else:
  if user2>user3:
    print("user2 is oldest")
  else:
    print("user3 is oldest")
if user1<user2:
  if user1<user3:
    print("user1 is youngest")
  else:
    print("user3 is youngest")
else:
  if user2<user3:
    print("user2 is youngest")
  else:
    print("user3 is youngest")
