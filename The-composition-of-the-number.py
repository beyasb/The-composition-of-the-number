import random
def check_sum(n, a, b):
    return a + b == n


def validate_input(prompt, input_type):
    while True:
        user_input = input(prompt)
        if input_type == 'int':
            if user_input.isdigit():
                return int(user_input)
            else:
                incorrect_answer = ['Я не понимаю. Если хочешь выйти, скажи «Стоп» или «Хватит». '
                                    'Состав какого числа будем повторять?',
                'Ой, я не знаю ответа на этот вопрос. Если ты хочешь выйти, скажи «Стоп» или «Хватит».'
                'Если ты хочешь выйти, скажи «Стоп» или «Хватит».'
                'Скажи мне, состав какого числа ты хочешь повторить. ',
                'Некорректный ввод. Чтобы выйти из навыка скажи «Стоп» или «Хватит».'
                'Какое число повторим?',
                'К сожалению, помочь с этим я не могу. Если захочешь выйти, скажи «Стоп» или «Хватит».'
                ' Давай повторим состав числа, которое ты скажешь?']
                print(random.choice(incorrect_answer))
        elif input_type == 'str':
            return user_input
        else:
            return user_input

start_lesson = ['Привет! Я Фани, готов помочь тебе с изучением состава чисел.'
            ' \nЕсли ты устанешь и захочешь выйти, просто скажи: “Хватит”.',
            'Рад тебя видеть! Я Фани, твой помощник в повторении состава числа.'
            '\nЕсли ты захочешь остановиться, просто скажи: «Хватит».',
            'Молодец, что нашел время на повторение состава чисел! '
            '\nЯ Фани, помогу тебе в этом. Если захочешь выйти, скажи: «Хватит».',
            'Здравствуй! Я Фани, вместе мы повторим состав чисел. '
            '\nЕсли захочешь выйти, скажи: «Хватит».']
print(random.choice(start_lesson))

while True:
    cmd_var = ['Состав какого числа будем повторять?', 'Состав какого числа хочешь повторить?',
               'Состав какого числа повторим?']
    cmd = validate_input(random.choice(cmd_var), 'str')
    if cmd.lower() == 'хватит' or cmd.lower() == 'стоп':
        break
    n = int(cmd)

    if n > 100:
        upper_100 = ['Я принимаю только числа меньше 100. Если ты хочешь закончить, скажи «Стоп» или «Хватит».',
                     'Нет, состав этого числа мы не сможем повторить. Подумай и скажи число меньше 100. '
                     'Если ты хочешь закончить, скажи «Стоп» или «Хватит».',
                     'Ох, я ожидал услышать другое. Попробуй еще раз, назови число меньше 100. '
                     'Если ты хочешь закончить, скажи «Стоп» или «Хватит».',
                     'Не понимаю. Ответом должно быть число меньше 100. '
                     'Если ты хочешь закончить, скажи «Стоп» или «Хватит».']
        print(random.choice(upper_100))
        continue

    while True:
        print(f'Из каких двух чисел состоит число {n}?')
        a = validate_input("Скажи первое число: ", 'int')
        b = validate_input("Скажи второе число: ", 'int')

        if check_sum(n, a, b):
            right_answer = ['Да, все верно!',
                            'Это верный ответ, молодец!',
                            'Верно! Так держать!',
                            'Да ты гений математики! Ответ верный.']
            print(random.choice(right_answer),
                '\n', f"Числа {a} и {b} в сумме дают число {n}.")
            break

        else:
            wrong_answer = ['Ответ неверный. Попробуй еще раз.',
                            'Нет, это не те числа. Подумай и назови слагаемые еще раз.',
                            'Ох, я ожидал услышать другое. Попробуй еще раз.']
            print(random.choice(wrong_answer),
                '\n', f"Сумма чисел {a} и {b} не равна числу {n}.")

end_lesson = ['Хорошо! Буду ждать тебя с новыми задачками.',
              'Классно порешали! Заходи еще!',
              'С тобой так здорово! Буду скучать.',
              'Пока-пока!']
print(random.choice(end_lesson))