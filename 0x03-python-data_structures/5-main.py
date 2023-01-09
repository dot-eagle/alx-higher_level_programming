#!/usr/bin/env python3

no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))


'''
#!/usr/bin/python3
def no_c(my_string):
    tmp_string = list(my_string)
    for c in range(0, len(tmp_string)):
        if ord(tmp_string[c]) == ord('c') or ord(tmp_string[c]) == ord('C'):
            tmp_string[c] = ''
            return ''.join(tmp_string)
'''
