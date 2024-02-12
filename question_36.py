# 36) Given a multiline string paragraph = """Python is an interpreted, high-level and general-purpose programming language. 
# Python's design philosophy emphasizes code readability with its notable use of significant whitespace.""", 
# count how many times the substring 'Python' (case-sensitive) appears in paragraph.

paragraph = """Python is an interpreted, high-level and general-purpose programming 
language. Python's design philosophy emphasizes code readability with its notable use 
of significant whitespace."""
count_python = paragraph.count('Python')
print(count_python)
