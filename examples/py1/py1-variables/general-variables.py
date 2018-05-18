a = 10
b = 20

result = a + b \
    +10

print("Result for a({0}) + b({1}) is {2}".format(a,b,result))


myname = "Теодор Колев" + "\r\n"

print(myname)

print("Type of Result variable is: {}".format(type(myname)))

print(1 + 10 + 12)

# 75myname = "Теодор Колев"

myname = "Sean O\'Conner"

print(myname)

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(2.0/3))

# fill with underscores (_) with the text centered
print('{0:_^11}'.format('здрасти'))

print('{name} е написал(а) {book}'.format(name='Толкин', book='Властелинът на Пръстените'))


print('А', end='') # can be ended with a empty string or a character
print('Б', end='')
print('В')

print("test %s '")

multi_line = "First line \
             second line"

print(multi_line)

# raw string, suitable for regular expressions or with a lot of symbols

print(r"some string ' %% with some things %s \ ")

print(type(10))

print(type('10'))

print(type("10"))

print(type(10 + 2))

print(type(10 + 2.78))

print(type('10' + "2"))

print(type("10" + "2"))