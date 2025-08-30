age = int(input("How old are you? "))

divideby = 10

remainder = age % divideby

print("You are " + str(int((age - remainder) / divideby)) + " decades and " + str(remainder) + " years old.")