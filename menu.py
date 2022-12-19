import users
def get_menu(param):

    flag = False if param == None else True

    while flag:
        if param[2] == 'Admin':
            print("\n1. Показать всех пользователей")
            print("2. Добавить новых пользователей")
            print("3. Удалить пользователя")
            print("9. Закрыть программу\n")

        if param[2] == 'Учитель':
            print("\n1. Показать список учеников")
            print("2. Добавить расписание занятий")
            print("3. Посмотреть расписание занятий")
            print("9. Закрыть программу\n")
        
        if param[2] == 'Ученик':
            print("\n1. Посмотреть расписание занятий")
            print("9. Закрыть программу\n")

        try:
            number_menu = [int(input('Выберите пункт меню: ')), param[2]]
        except ValueError:
            print("Вы ввели чушь!")
            break

        if number_menu[0] == 1 and number_menu[1] == 'Admin':
            users.all_users('All')
        
        elif number_menu[0] == 2 and number_menu[1] == 'Admin':
            users.new_users()
        
        elif number_menu[0] == 3 and number_menu[1] == 'Admin':
            n = input("Введите логин пользователя, которого нужно удалить: ")
            p = input("Введите пароль: ")
            user = users.seach_users(n, p)
            if user != None:
                users.delete_users(user)

        elif number_menu[0] == 1 and number_menu[1] == 'Учитель':
            users.all_users('Ученик')
        
        elif number_menu[0] == 2 and number_menu[1] == 'Учитель':
            users.add_home_work()

        elif number_menu[0] == 3 and number_menu[1] == 'Учитель':
            users.time_table()
        
        elif number_menu[0] == 1 and number_menu[1] == 'Ученик':
            users.time_table()

        elif number_menu[0] == 9:
            print("Спасибо, что воспользовались нашей программой.")
            break