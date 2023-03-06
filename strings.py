my_list = ['h', 'e', 'l', 'l', 'o']
my_text = 'hello'

my_list[0] = 'c'
print(my_list)

name = 'Jan'
age = 30

text = 'Jestem ' + name + ' i mam ' + str(age) + ' lat.'
print(text)

text_2 = 'Jestem {} i mam {} lat'.format(name, age)
print(text_2)

text_3 = 'I am {name} and I am {years} old'.format(name=name, years=age)

funds = 150.9723

print('Funds: {:10.1f}'.format(funds))

text_3 = 'I\'m Jan'
print(text_3)

print(f'I am {name} and I am {age} years old')
print(f'I am {name} and I am {age:.2f} years old')

