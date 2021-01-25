#BMI

kg=int(input('Enter Your mass : '))
cm=int(input('Enter your Tall : '))

'''
ตรงเอา cm ไปหาร100 ก่อนค่อยกลับเข้ามาคำนวณของ resl ก็ได้จะได้ดูง่ายกว่าของผม
เช่น 
m = cm/100
resl = kg/m**2
ก็ได้เช่นกัน
'''
resl=kg/(cm/100)**2


print('You BMI is : '+ str(resl)) #ต้องใช้ str เพื่อให้ resl เป็น String สำหรับแสดงผล

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

