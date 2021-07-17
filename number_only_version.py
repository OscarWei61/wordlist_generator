import numpy as np
import os
import tqdm

password_length_minimum = int(input("Input minimum length of password : "))
password_length_mxnimum = int(input("Input maximun length of password : "))

'''only number password conditon'''
starting_point = 0
ending_point = 99

for i in tqdm.trange(password_length_minimum):
    starting_point = starting_point * 10 + 1
    ending_point = ending_point * 10 + 9

print(starting_point)
print(ending_point)
result_wordlist = np.array([starting_point])
result_wordlist = result_wordlist.astype(np.uint8)
f = open('wordlist.txt',mode = 'w')

for i in tqdm.trange(starting_point,ending_point+1):
    
    f.write(str(i)+"\n")
    result_wordlist = np.append([],i)

print(result_wordlist)

f.close()
os.system("wordlist.txt")

