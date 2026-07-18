first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
import tools
add_result = tools.add(first_num, second_num )
print(f"Addition: {add_result}")
sub_result = tools.subtract(first_num, second_num)
print(f"Subtraction: {sub_result}")
mult_result = tools.multiply(first_num, second_num)
print(f"Multiplication: {mult_result}")
