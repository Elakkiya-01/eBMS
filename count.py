
# Write a program to find out the count of 9s in the numbers between 2 given numbers
def countnine():
    Lower_value = int(input("Enter the lower_value="))
    Higher_value = int(input("Enter the Higher_value="))
    count = 0
    for i in range(Lower_value,Higher_value):
        if "9" in (str(i)):
            count = count + str(i).count('9')
    print(count)
countnine()