import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценки ученика по предмету
        5. Редактировать имя ученика
        6. Редактировать название предмета
        7. Вывести оценки ученика
        8. Вывести средний балл по каждому предмету ученика
        9. Вывести оценки учеников по конкретному предмету
        10. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценки ученика по предмету')
        print(students) #чтоб видеть список учеников
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        print(classes) #чтоб видеть наименование предметов
        # считываем название предмета
        class_ = input('Введите предмет: ')
        #если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            #Выводим имя, предмет и оценки по предмету
            print(f'{student}\n{class_}\n{students_marks[student][class_]}')
            remove_mark = int(input('Введите, какую оценку удалить: '))
            #если у ученика по предмету есть оценка, которую надо удалить, удаляем
            if remove_mark in students_marks[student][class_]:
                students_marks[student][class_].remove(remove_mark)
                print(f'оценка {remove_mark} удалена из журнала')
            else:
                print(f'оценки {remove_mark} нет')
                #выводим имя, предмет и оценки по предмету без удаленной оценки
            print(f'{student}\n{class_}\n{students_marks[student][class_]}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 5:
        print('5. Редактировать имя ученика')
        print(f'Список учеников:\n{students}') #чтоб видеть список учеников
        # считываем имя ученика
        student = input('Введите имя ученика, которое надо изменить: ')
        #если данные введены верно
        if student in students:
            students.remove(student)
            changed_student = input('Введите отредактированное имя ученика: ')
            students.append(changed_student)
            students.sort()
        else:
            print('ОШИБКА: имя ученика введено неверно')
        print()
    elif command == 6:
        print('6. Редактировать название предмета')
        print(f'Список предметов:\n{classes}') #чтоб видеть наименование предмета
        # считываем название предмета
        class_ = input('Введите название предмета, которое надо изменить: ')
        # если данные введены верно
        if class_ in classes:
            classes.remove(class_)
            changed_class = input('Введите отредактированное название предмета: ')
            classes.append(changed_class)
            classes.sort()
        else:
            print('ОШИБКА: наименование предмета введено неверно')
        print()
    elif command == 7:
        print('7. Вывести оценки ученика')
        print(students) #чтоб видеть список учеников
        student = input('Введите имя ученика, оценки которого нужно вывести: ')
        #если данные введены верно
        if student in students:
            print(f'{student}\n{students_marks[student]}')
        else:
            print('ОШИБКА: имя ученика введено неверно')
        print()
    elif command == 8:
        print('8. Вывести средний балл по каждому предмету ученика')
        print(students) #чтоб видеть список учеников
        student = input('Введите имя ученика: ')
        if student in students:
            print(f'{student}\n{students_marks[student]}')
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету с округлением до 2 знаков после запятой
                print(f'{class_} - {marks_sum / marks_count:.2f}')
        else:
            print('ОШИБКА: имя ученика введено неверно')
        print()
    elif command == 9:
        print('9. Вывести оценки учеников по конкретному предмету') #полезная команда для задачи
        print(classes) #чтоб видеть, из чего выбирать наименование предмета
        class_ = input('Введите название предмета: ')
        if class_ in classes:
            print(f'{class_}')
            for student in students:
                print(f'{student}\n{students_marks[student][class_]}\n')
        else:
            print('ОШИБКА: наименование предмета введено неверно')
        print()
    elif command == 10:
        print('10. Выход из программы')
        break
