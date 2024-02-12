# 33) Consider the string text = "Python programming is fun, isn't it?". 
# Use string methods to replace all instances of 'is' with 'should be' and 
# then find the position of the first occurrence of 'fun' in the modified string.

text = "Python programming is fun, isn't it?"
# Replace 'is' with 'should be'
modified_text = text.replace('is', 'should be')
# Find the position of 'fun'
position_fun = modified_text.find('fun')
print(modified_text)
print(position_fun)
