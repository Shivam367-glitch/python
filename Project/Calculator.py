
# https://www.onlinegdb.com/eeBiEFnXK

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    else:
        return a / b
    
def factorial(a):
     dp = [-1] * (a + 1)
     dp[0]=0
     dp[1]=1
     
     for i in range(2,a+1):
        dp[i] = i * factorial(i - 1)
         
     return dp[a]

if __name__ == "__main__":
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Factorial")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        elif choice == '5':
            num1 = int(input("Enter a number to find factorial: "))
           
            print("Result:", factorial(num1))
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
