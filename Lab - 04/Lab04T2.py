class Power:
    def pow(x, n):
        result = 1
        if n >= 0:        
            for i in range(n):
                result *= x
        else:         
            for i in range(-n):
                result *= x
            result = 1 / result
        return result
x = float(input("Enter base x: "))
n = int(input("Enter power n: "))
print("Result:", Power.pow(x, n))
