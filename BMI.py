#BMI

kg=int(input('Enter Your mass : '))
while not kg:
    kg=int(input('Enter Your mass : '))

cm=int(input('Enter your Tall : '))


resl=kg/(cm/100)**2
print('You BMI is : '+ str(resl))

if resl <= 18.5:
    print('Your are lean')

elif resl <= 24:
    print('Your are Normal')

elif resl <= 29.9:
    print('You are fat')

elif resl > 30:
    print('You are very fat')

else:
    print('Invalid input')

