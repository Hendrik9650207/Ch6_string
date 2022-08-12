# 字串中有'，句子改用"夾
print("This is Alice's cat.")

# 或是改用\，轉義字元來處理
print('Say hi to Bob\'s mother')

'''
常用轉義字元
\'    '
\"    "
\t    tab
\n    return
\\    \
'''

# r 把字串轉為原始字串
print(r'This is Alice\'s \n cat.')
print()

# ''' 表示多行字串
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

print()
# index and slice
str1 = 'Hello World'
print(str1[-1])
print(str1[-5:-1])
print(str1[0:7])
print()

# in、not in
print('Hello' in str1)
print()

# 字串放置 + 或者 %s 或者用fstring 語法: f'{var}'
name = 'Al'
age = 25
print('My name is ' + name + '.' + 'I am ' + str(age) + ' years old.')
print()
print('My name is %s.I am %s years old.' % (name, age))
print()
print(f'My name is {name}.I am {age} years old.')
print()


# String Method
'''
String Method
upper()
lower()
isupper()
islower()
'''

str2 = 'Hell No!'
print(str2.upper())
print()
print(str2.lower())
print()

'''
String Method
startswith()
endswith()
'''

print('Hello World!'.startswith('He'))
print()
print('Hello World!'.endswith('World!'))
print()

'''
join()  用指定字串把list內容連接起來
split()
'''

lst3 = ['cat', 'dog', 'bird', 'fish']
print('-'.join(lst3))

str4 = 'qqq,www,eee,rrr,ttt'
print(str4.split(','))
print()
lst4 = str4.split(',')
for i in lst4:
    print(i)
    print()


'''
partition()
'''

'''
rjust() 
ljust()
center()
'''

str5 = 'ABCDE'
print(str5.rjust(10))  # 從右邊對齊，共10 bytes
print()
print(str5.ljust(10))  # 從左邊對齊，共10 bytes
print()
print(str5.center(20, '='))  # 置中對齊，共20 bytes
print()


'''
strip()
rstrip()
lstrip()
'''
str6 = '    Hello World    '
print(str6.strip())
print()


'''
unicode 編碼
ord()  alphabet->num
chr()  num->alphabet
'''
print(ord('A'))
print(ord('B'))
print(ord('C'))
print(chr(ord('A')))

'''
使用pyperclip套件複製剪貼簿中的內容
'''

