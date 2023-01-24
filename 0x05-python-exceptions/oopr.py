
#!/usr/bin/python3

while True:
    try:
        val = int(input("Please enter an integer number: "))
        break
    except ValueError:
        print("Oops! That was not a valid integer number. Try it again...")
