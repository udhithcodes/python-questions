n = int(input("Enter a number: "))

original = n  # Save the original number
temp = n      # Create a temporary copy
count = 0
total = 0

# Count the number of digits and find the power
while temp > 0:
    count = count + 1 
    temp = temp // 10 

temp = n  # Reset temp to the original number

# Extract each digit and calculate its power
while temp > 0:
    digit = temp % 10             # Get the last digit
    total = total + digit ** count  # Add digit raised to count
    temp = temp // 10             # Remove the last digit

# Compare the calculated total with the original number
if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")