def reverse(x):
    output = ""
    for c in x:
        output = c + output
    return output

str_name = "hello"
print(type(reverse))
print(reverse(str_name))

def reverse_t(text):
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i]
    return a

print(reverse_t ("world"))

def reverse_slicing(w):
	return w[::-1]

print(reverse_slicing("kyle"))

def reverse_while(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length -= 1
    return s1

print(reverse_while("sebastian"))