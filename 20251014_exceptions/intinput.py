answer = input('Сколько тебе лет? ')
try:
    answer = int(answer)
except:
    print('Ответ должен быть числом, а не ' + answer)
else:
    print('Твой год рождения ' + str(2025 - answer))
finally:
    print('Пока!')