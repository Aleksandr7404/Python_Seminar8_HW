title = ["\033[1;3m№", "Фамилия", "Имя", "Отчество", "Телефон\033[0m"]
def menu():
    while True:
        item = input(f'\n     \033[1mГлавное меню:\033[0m \n\n 1 - Найти контакт\n 2 - Добавить контакт'
                     '\n 3 - Удалить контакт\n 4 - Смотреть весь справочник\n 5 - Копировать контакт в файл'
                     '\n 0 - Выход\n\nВыберите действие > ')
        print()
        if item.isdigit() and int(item) < 6:
            if int(item) == 1:
                find_contact()
            elif int(item) == 2:
                add_new_contact()
            elif int(item) == 3:
                remove_cotact()    
            elif int(item) == 4:
                open_phonebok() 
            elif int(item) == 5:
                copy_contact()     
            elif int(item) == 0: 
                return()   
        else:
            print('\033[0;31;40m\nОшибка выбора!')
        input('\033[0m\nНажмите Enter, чтобы продолжить\n')    
       
def add_new_contact():
    print('\033[1mДобавление контакта\033[0m')
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")

    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        contact = ";".join([s_name, f_name, m_name, phone])
        if contact == ';;;':
            print('\033[0;31;40m\nНет данных для записи!\033[0m')
            return
        file.write(contact + '\n')
        print('\n\033[3m',' '.join(contact.split(';')),'\033[0m', ' - контакт сохранен.')
    return


def find_contact(): # общий поиск
    data_find = input("Введите данные для поиска или нажмите Enter для выбора: ").lower()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        phone_book = file.readlines()
        result_find = list()                                         # список для индексов строк с совпадениями
        print("\n","\t\t".join(title),"\n")
        for i in range(len(phone_book)):
            if data_find in phone_book[i].lower():
                print(i,"\t\t","\t\t".join(phone_book[i].split(';')))
                result_find.append(i)
        if len(result_find) == 0:
            print("Совпадений не найдено!\n")
            return        
    return result_find
                           
def remove_cotact():
    print('\033[1mУдаление контакта\033[0m')
    list_ind = find_contact()
    if list_ind:
        remove_ind = input('Выберите номер контакта для удаления: ')
    else:
        return    
    if remove_ind.isdigit() and int(remove_ind) in list_ind:
        with open('phonebook.txt', 'r', encoding='utf-8') as file:
            phone_book = file.readlines()
        with open('phonebook.txt', 'w', encoding='utf-8') as file:
            print('\n',remove_ind,' '.join(phone_book[int(remove_ind)].split(';')),'- этот контакт удален из справочника')
            phone_book.pop(int(remove_ind))    
            file.write("".join(phone_book))
            return
    else:
        print('\033[0;31;40m\n Ошибка выбора!')
    return    

def open_phonebok():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
                print("\t\t".join(title[1:]),"\n")              # вывод заголовка без нумерации
                for line in file:
                    print("\t\t".join(line.split(';')))
    return  

def copy_contact():
    print('\033[1mКопирование контакта\033[0m\n')
    list_ind = find_contact()
    if list_ind:
        copy_ind = input('\nВыберите номер контакта для копирования: ')
    else:
        return
    if copy_ind.isdigit() and int(copy_ind) in list_ind:
        with open('phonebook.txt', 'r', encoding='utf-8') as file:
            phone_book = file.readlines()
        file_name = (input('Введите имя файла для записи: '))
        if file_name:
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(("".join(phone_book[int(copy_ind)])))
                print("\n№",copy_ind, ' '.join(phone_book[int(copy_ind)].split(';')),"Контакт сохранен.")
                return
        else: 
            print('\033[0;31;40m\nНет имени файла!')      
            return
    else:
        print('\033[0;31;40m\n Ошибка выбора!')
    return          
             
menu()          