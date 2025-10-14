result = 0
znam = int(input('Введите число, я найду обратное:'))
try: # потенциально опасный участок заключаем в try:except:
    result = 1 / znam
except ZeroDivisionError:
    result = None
if result:
    print('Обратное равно ', result)
else:
    print('Обратного не существует! ' + str(znam))