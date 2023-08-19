#handling zero division error

def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divid by zero")
        return None
#test case
numerator = int(input("Enter the numerator value: "))
denominator = int(input("Enter the denominator value:"))

print(safe_divide(numerator, denominator))