from config import  *
import threading #импортируем нужные библиотеки


if cur_op == '+':
    res = num1 + num2
elif cur_op == '-':
    res = num1 - num2
elif cur_op == ':':
    if num2 != 0:
        res = num1 / num2
    else:
        res = 'Деление на ноль невозможно'
elif cur_op == '*':
    res = num1 * num2 #вычисляем ответ

if isinstance(res, float):
    res = round(res, 1) #если число содержит знаки после запятой, то округляем его иначе пользователь не успеет их ввести

print(f"Решите: {num1} {cur_op} {num2}") #выводим пример

user_ans = None #создаем глобальную переменную для ответа пользователя
input_received = threading.Event() #событие для завершения отсчета времени

def inputnum(): #поток для ввода
    global user_ans
    user_ans = input('Введите ответ: ')
    input_received.set() #флаг что ввод завершен

#запуск потока ввода
input_thread = threading.Thread(target=inputnum)
input_thread.daemon = True #автоматически завершаем поток при завершении основной программы
input_thread.start()

input_thread.join(timeout=12) #ждем 12 сек или завершения ввода 
#сгенирировала с помощью gpt

if input_received.is_set(): #проверяем завершился ли ввод
    try:
        user_ans = float(user_ans) #проверяем является ли ответ числом
        if user_ans == res:
            print('Отлично! Это верный ответ, вы выиграли!')
        else:
            print(f'К сожалению, это неверный ответ, вы проиграли. Верный ответ: {res}')
    except ValueError:
        print('Некорректный ввод. Вы проиграли.')
else:
    print(f'Время вышло, вы проиграли. Ответ: {res}')
