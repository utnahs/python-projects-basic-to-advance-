import random

lowercase_letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

uppercase_letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

digits = [
    '0','1','2','3','4','5','6','7','8','9'
]

special_characters = [
    '!','@','#','$','%','^','&','*',
    '(',')','-','_','=','+',
    '[',']','{','}',
    '.',',','?'
]

print("Generate a strong password!")
upper_char=int(input("How many uppercase letters do you want in the password?\n "))
lower_char=int(input("How many lowercase letters do you want in the password?\n "))
num=int(input("How many numbers do you want in the password?\n "))
sp_char=int(input("How many special characters do you want in the password?\n "))

upper_char_list=''
for i in range(0,upper_char):
    upper_char_list=upper_char_list+uppercase_letters[random.randint(0,len(uppercase_letters)-1)]                 #concats the extracted random letter with the empty string char_list
#print(char_list)

lower_char_list=''
for i in range(0,lower_char):
    lower_char_list=lower_char_list+lowercase_letters[random.randint(0,len(lowercase_letters)-1)]                 #concats the extracted random letter with the empty string char_list
#print(char_list)

num_list=''
for i in range(0,num):
    num_list=num_list+str(digits[random.randint(0,len(digits)-1)])                     #concats the extracted random digits to num_list after CONVERTING it to STRING
#print(num_list)

sp_char_list=''
for i in range(0,sp_char):
    sp_char_list=sp_char_list+special_characters[random.randint(0,len(special_characters)-1)]          #concats the extracted random special character with the empty string sp_char_list
#print(char_list)

final_password=upper_char_list+lower_char_list+num_list+sp_char_list
#print(final_password)       ### the easy mode



s=[]
for _ in final_password:
    s=s+[_]

random.shuffle(s)
print(''.join(s))               ###shuffled, hard mode
