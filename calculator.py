def calculator(num1, num2, operator):  
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "unknown value"
    else:
        return "Enter a valid operator"
    
    return int(result) if result.is_integer() else result

def main():
    
        num1 = int(input("Enter a number: "))  
        num2 = int(input("Enter another number: "))
        operator = input("Enter an operator ")
        if not isinstance(num1, (int)) or not isinstance(num2, (int)):
             print("Enter a valid number")
        else:
            result = calculator(num1, num2, operator)  
            print("Result:", result) 

main()
