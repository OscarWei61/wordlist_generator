from typing import final
import numpy as np
import os
from tqdm import tqdm
import random
from itertools import permutations

def create_password_element_list(candiate):
    
    number_switch = False
    uppercase_letter_switch = False
    lowercase_letter_switch = False
    special_symbol_switch = False
    password_element = np.array([])

    for word in range(len(candiate)):
        if candiate[word] == '1':
            number_switch = True
        if candiate[word] == '2':
            uppercase_letter_switch = True
        if candiate[word] == '3':
            lowercase_letter_switch = True
        if candiate[word] == '4':
            special_symbol_switch = True
    
    for num in range(33,127):
        operate_code = False

        if 48 <= num <= 57 :
            if number_switch == True:
                operate_code = True
        elif 65 <= num <= 90:
            if uppercase_letter_switch == True:
                operate_code = True
        elif 97 <= num <= 122:
            if lowercase_letter_switch == True:
                operate_code = True
        else:
            if special_symbol_switch == True:
                operate_code = True
        if operate_code == True:
            password_element = np.append(password_element,[num])
    
    return password_element
            
password_length_minimum = int(input("Input minimum length of password : "))
password_length_mxnimum = int(input("Input maximun length of password : "))
print("Choose what combination do you want for your password")
print("Enter the number of category")
password_combination = str(input("1.number 2.uppercase letter 3.lowercase letter 4.special symbol : "))

password_element = create_password_element_list(password_combination)
print(password_element)

   
f = open('wordlist.txt',mode = 'w')

password_string = ""
for i in range(password_element.shape[0]):
    password_string = password_string + chr(int(password_element[i]))
print("Password element " + password_string)
for pass_length in range(password_length_minimum,password_length_mxnimum+1):
    
    password_result = np.array(list(permutations(password_string,pass_length)))
    for count in tqdm(range(password_result.shape[0])):
        final_password = ""
        for countt in range(password_result.shape[1]):
            final_password = final_password + password_result[count][countt]
        #print(final_password)
        f.write(final_password)
        f.write("\n")
f.close()
os.system("wordlist.txt")

