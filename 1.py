import os

ini_path = os.path.abspath('Result_avarege of fit_n.txt')
res_path = os.path.abspath('Res_Asym')

if os.path.exists(ini_path)==False:
    ini_path = os.path.abspath('From_avarege_fit_to_ASYM/Result_avarege of fit_n.txt')
    res_path = os.path.abspath('From_avarege_fit_to_ASYM/Res_Asym')

file = open(ini_path, 'r')
file2 = open(res_path, 'w')

v = input('Number of state ')

while(True):
    str1 = file.readline()

    if len(str1) == 0:
        break

    str1=str1.split()
    numb, E, w, J, Ka, Kc= str1

    file2.write ('%5s V= %1s J=%2s%3s%3s %32s\n' % (numb, v, J, Ka, Kc, E))

file.close()
file2.close()
