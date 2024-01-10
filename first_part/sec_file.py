import re

service_list = []
new_string = ''
data = open('Чеки.txt', encoding="utf-8")
for el in data:
    new_string += el

january_list = []
december_list = []
febrary_list = []
march_list = []
april_list = []
mat_list = []
june_list = []
july_list = []
august_list = []
september_list = []
october_list = []
november_list = []
pattern_month = re.compile('[_]\w+[.]')
pattern_service = re.compile('\w+[_]')
first_result = pattern_service.findall(new_string)
for el in first_result:
    service_list.append(el[:-1])
short_service_list = set(service_list)

result_file = open("чеки_по_папкам.txt", "w")
for el in new_string.split():
    if 'январь' in el:
        january_list.append(el)
list1 = []
stop_string2 = ''
for el in january_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/январь/{x}.pdf\n")
    list1.append(x)
if len(january_list) == 9:
    result_file.write(f"Все услуги за январь оплачены\n")
else:
    for el in short_service_list:
        if el not in list1:
            stop_string2 += f' {el},'
    result_file.write(f"Не все услуги за январь оплачены!\nНе оплачены: {stop_string2[:-1]} \n")

for el in new_string.split():
    if 'декабрь' in el:
        december_list.append(el)
list2 = []
stop_string1 = ''
for el in december_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/декабрь/{x}.pdf\n")
    list2.append(x)
if len(december_list) == 9:
    result_file.write(f"Все услуги за декабрь оплачены\n")
else:
    for el in short_service_list:
        if el not in list2:
            stop_string1 += f' {el},'
    result_file.write(f"Не все услуги за декабрь оплачены!\nНе оплачены: {stop_string1[:-1]} \n")

for el in new_string.split():
    if 'февраль' in el:
        febrary_list.append(el)
list3 = []
stop_string3 = ''
for el in febrary_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/февраль/{x}.pdf\n")
    list3.append(x)
if len(febrary_list) == 9:
    result_file.write(f"Все услуги за февраль оплачены\n")
else:
    for el in short_service_list:
        if el not in list3:
            stop_string3 += f' {el},'
    result_file.write(f"Не все услуги за февраль оплачены!\nНе оплачены: {stop_string3[:-1]} \n")

for el in new_string.split():
    if 'март' in el:
        march_list.append(el)
list4 = []
stop_string4 = ''
for el in march_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/март/{x}.pdf\n")
    list4.append(x)
if len(march_list) == 9:
    result_file.write(f"Все услуги за март оплачены\n")
else:
    for el in short_service_list:
        if el not in list4:
            stop_string4 += f' {el},'
    result_file.write(f"Не все услуги за март оплачены!\nНе оплачены: {stop_string4[:-1]} \n")

for el in new_string.split():
    if 'апрель' in el:
        april_list.append(el)
list5 = []
stop_string5 = ''
for el in april_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/апрель/{x}.pdf\n")
    list5.append(x)
if len(april_list) == 9:
    result_file.write(f"Все услуги за апрель оплачены\n")
else:
    for el in short_service_list:
        if el not in list5:
            stop_string5 += f' {el},'
    result_file.write(f"Не все услуги за апрель оплачены!\nНе оплачены: {stop_string5[:-1]} \n")

for el in new_string.split():
    if 'май' in el:
        mat_list.append(el)
list6 = []
stop_string6 = ''
for el in mat_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/май/{x}.pdf\n")
    list6.append(x)
if len(mat_list) == 9:
    result_file.write(f"Все услуги за май оплачены\n")
else:
    for el in short_service_list:
        if el not in list6:
            stop_string6 += f' {el},'
    result_file.write(f"Не все услуги за май оплачены!\nНе оплачены: {stop_string6[:-1]} \n")

for el in new_string.split():
    if 'июнь' in el:
        june_list.append(el)
list7 = []
stop_string7 = ''
for el in june_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/июнь/{x}.pdf\n")
    list7.append(x)
if len(june_list) == 9:
    result_file.write(f"Все услуги за июнь оплачены\n")
else:
    for el in short_service_list:
        if el not in list7:
            stop_string7 += f' {el},'
    result_file.write(f"Не все услуги за июнь оплачены!\nНе оплачены: {stop_string7[:-1]} \n")

for el in new_string.split():
    if 'июль' in el:
        july_list.append(el)
list8 = []
stop_string8 = ''
for el in july_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/июль/{x}.pdf\n")
    list8.append(x)
if len(july_list) == 9:
    result_file.write(f"Все услуги за июль оплачены\n")
else:
    for el in short_service_list:
        if el not in list8:
            stop_string8 += f' {el},'
    result_file.write(f"Не все услуги за июль оплачены!\nНе оплачены: {stop_string8[:-1]} \n")

for el in new_string.split():
    if 'август' in el:
        august_list.append(el)
list9 = []
stop_string9 = ''
for el in august_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/август/{x}.pdf\n")
    list9.append(x)
if len(august_list) == 9:
    result_file.write(f"Все услуги за август оплачены\n")
else:
    for el in short_service_list:
        if el not in list9:
            stop_string9 += f' {el},'
    result_file.write(f"Не все услуги за август оплачены!\nНе оплачены: {stop_string9[:-1]} \n")

for el in new_string.split():
    if 'сентябрь' in el:
        september_list.append(el)
list10 = []
stop_string10 = ''
for el in september_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/сентябрь/{x}.pdf\n")
    list10.append(x)
if len(september_list) == 9:
    result_file.write(f"Все услуги за сентябрь оплачены\n")
else:
    for el in short_service_list:
        if el not in list10:
            stop_string10 += f' {el},'
    result_file.write(f"Не все услуги за сентябрь оплачены!\nНе оплачены: {stop_string10[:-1]} \n")

for el in new_string.split():
    if 'октябрь' in el:
        october_list.append(el)
list11 = []
stop_string11 = ''
for el in october_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/октябрь/{x}.pdf\n")
    list11.append(x)
if len(october_list) == 9:
    result_file.write(f"Все услуги за октябрь оплачены\n")
else:
    for el in short_service_list:
        if el not in list11:
            stop_string11 += f' {el},'
    result_file.write(f"Не все услуги за октябрь оплачены!\nНе оплачены: {stop_string11[:-1]} \n")

for el in new_string.split():
    if 'ноябрь' in el:
        november_list.append(el)
list12 = []
stop_string12 = ''
for el in november_list:
    x = pattern_service.findall(el)[0][:-1]
    result_file.write(f"/ноябрь/{x}.pdf\n")
    list12.append(x)
if len(november_list) == 9:
    result_file.write(f"Все услуги за ноябрь оплачены\n")
else:
    for el in short_service_list:
        if el not in list12:
            stop_string12 += f' {el},'
    result_file.write(f"Не все услуги за ноябрь оплачены!\nНе оплачены: {stop_string12[:-1]} \n")

result_file.close()

