def multiply_by(number):
    def multiply(x):
        return x * number
    return multiply


multiply_by3 = multiply_by(3)
result = multiply_by3(10)

print(result)

