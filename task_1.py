import re # импортировал модуль для разделения строки на список сразу по нескольким символам

temp_list = re.split(r'[,\s]', '1h 45m,360s,25m,30m 120s,2h 60s') # преобразовал строку в список отдельных значений времени

minutes = [] # создал пустой список для сбора значений в минутах
    
for i in temp_list: # запустил цикл для поиска и преобразования часов и секунд в минуты 
    if 'h' in i:
        minutes.append(int(i.replace(i, i[:-1])) * 60)
    elif 'm' in i:
        minutes.append(int(i.replace(i, i[:-1])))
    else:
        minutes.append(int(i.replace(i, i[:-1])) // 60)

sum_all_minutes = sum(minutes) # посчитал сумму всех минут
print(sum_all_minutes)
