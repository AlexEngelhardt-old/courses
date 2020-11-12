from placing_parentheses import get_maximum_value

expression = '5-8+7*4-8+9'
print(get_maximum_value(expression))

assert get_maximum_value(expression) == 200