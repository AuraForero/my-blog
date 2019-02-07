print('Hello,Django girls')
if 5>2:
    print('5 is indeed greater than 2!')
else:
    print('5 is not greater than 2')
name= 'Sonja'
if name == 'Ola':
    print('Hey Ola')
elif name == 'Sonja':
    print('Hey Sonja')
else:
    print('Hey anonymous')

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("Me duelen las orejas! :(")

#Cambiar el volumen si esta muy alto  o muy bajo
volume = 12
if volume < 20 or volume > 80:
   print("Mucho mejor!")

def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi(name1):
    if name1 == 'Ola':
        print('Hi Ola!')
    elif name1 == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi("Sonja")

def hi (name):
    print('hi '+ name+ '!')
hi("Rachel")

#codigo para loops
def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
#loop usando in range:  incluye el primer valor, pero no el último.
for i in range(1, 6):
    print(i)
#diccionarios
participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
print(participant['name'])
len(participant)
participant['favorite_language'] = 'Python'
participant.pop('favorite_numbers')
participant['country'] = 'Germany'
participant