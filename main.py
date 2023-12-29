from datetime import date, datetime, timedelta


def get_birthdays_per_week(users:list):
    '''Функція перевіряє список з словників [{"name":...,"birthday":...},...]
    чи випадає день народження протягом наступного тижня та повертає словник
    де ключ це день тижня та значенн це імя в кого буде день народження.
    Якщо день народження у вихідні переносить день народження на понеділок.
    '''
    # Створення словника де ключами є назви днів тижня (на англійській мові)
    result_dict = {current_date.strftime('%A'): [] for current_date in (date.today() + timedelta(days=i) for i in range(7))}
    # Цикл що перебирає список з словниками в яких ключі "name" = Імя(Строка) "birthday" = день народження (datetime обєкт)
    for user in users:
        # Змінна яка приймає день народження 
        birthday_in_this_year = user['birthday']
        # Перевірка: якщо день народження вказаний не в теперішньому році та цей рік в минулому
        if birthday_in_this_year.year != date.today().year and birthday_in_this_year.year < date.today().year:
            #Вказує теперішній рік в змінну
            birthday_in_this_year = birthday_in_this_year.replace(year=date.today().year, month=birthday_in_this_year.month, day=birthday_in_this_year.day)
            # Перевірка: якщо різниця між сьогоднішньою датою та датою дня народження = 359 днів(з врахуванням того що 366-7 найближчий тиждень який ми перевіряємо)
            # Тобто день нарождення минув 359 днів тому назад
            if  date.today() - birthday_in_this_year >= timedelta(359):
                # Заміняє рік на наступний 
                birthday_in_this_year = birthday_in_this_year.replace(year=date.today().year + 1, month=birthday_in_this_year.month, day=birthday_in_this_year.day)
        # Первірка: якщо день народження в періодні від сьогодні до 7 днів від сьогодні
        if date.today() <= birthday_in_this_year <= date.today() + timedelta(7):
            # Перевірка: якщо день тижня на який випадає день народження в суботу або неділю 
            if birthday_in_this_year.strftime('%A') == 'Sunday' or birthday_in_this_year.strftime('%A') == 'Saturday':
                # Добавляє імя користувача зі списку в словник де ключем буде понеділок
                result_dict['Monday'] += [user["name"]]
            else:
                # Якщо день народження в будній день 
                # Добавляє імя користувача зі списку в словник де ключем буде день тижня
                result_dict[birthday_in_this_year.strftime('%A')] += [user["name"]]
        # Якщо день народження не в періодні від сьогодні до 7 днів від сьогодні
        # Пропускаємо такий варіант
        else:
            continue     
    # Видаляє пусті ключ-значення з словника з результатом
    result_dict = {key: value for key, value in result_dict.items() if value}
    # Повертаєм словник з результатом де ключ це назва дня тижня та значення це імя
    return result_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2023, 1, 1).date()},
        {'name': 'Oleh', 'birthday': datetime(2023,1,4).date()},
        {'name': 'Olena', 'birthday': datetime(2023,11,28).date()},
        {'name': 'Viktor', 'birthday': datetime(2024,1,2).date()},
        {'name': 'Petro', 'birthday': datetime(2023,12,29).date()},
        {'name': 'Andry', 'birthday': datetime(2023,1,1).date()},
        {'name': 'Katya', 'birthday': datetime(2023,9,5).date()},
        {'name': 'Ira', 'birthday': datetime(2021,1,4).date()},
        {'name': 'Ihor', 'birthday': datetime(2021,12,30).date()},
    ]
    
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
