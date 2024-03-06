"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


def name_outline(department):
    name_outline_str = ', '.join([item["first_name"] for item in department["employers"]])
    return name_outline_str  # отдельная функция вывода значений имени


def salary_outline(department):
    return [item["salary_rub"] for item in department["employers"]]  # отдельная функция вывода значений зарплаты


def sum_salary_department(department):
    return sum([item["salary_rub"] for item in department["employers"]])  # отдельная функция суммы зарплат отдела


def min_salary_department(department):
    return min([item["salary_rub"] for item in
                department["employers"]])  # отдельная функция вывода минимальной зарплаты отдела


def max_salary_department(department):
    return max([item["salary_rub"] for item in
                department["employers"]])  # отдельная функция вывода максимальной зарплаты отдела


def avg_salary_department(department):
    return sum([item["salary_rub"] for item in department["employers"]]) / len(
        department["employers"])  # отдельная функция вывода средней зарплаты в отделе


def tax_for_all(money_for_tax):
    tax_in_money = 0
    for item in taxes:
        if item["department"] == None:
            tax_in_money += money_for_tax * (item["value_percents"] / 100)
    return tax_in_money
# отдельная функция подсчета налогов, применяемых для всех


def taxes_for_department(money_for_tax):
    tax_in_money = 0
    for item in taxes:
        if item["department"] == None:
            tax_in_money += money_for_tax * (item["value_percents"] / 100)
    return tax_in_money
# отдельная функция подсчета налогов, применяемых для конкретного отдела


# 1 задание
for department in departments:
    print(f"{department['title']}")
print()  # пустая строка

# 2 задание
for department in departments:
    name_of_employee = name_outline(department)
    print(f"{name_of_employee}")
print()  # пустая строка

# 3 задание
for department in departments:
    name_of_employee = name_outline(department)
    print(f"{department['title']} : {name_of_employee}")
print()  # пустая строка

# 4 задание
employees_high_salary = []
for department in departments:
    for item in department["employers"]:
        salary_employee = item['salary_rub']
        if salary_employee > 100000:
            employees_high_salary.append(item['first_name'])
employees_high_salary_str = ", ".join(employees_high_salary)
print(f"{employees_high_salary_str} получают больше 100000 рублей.")
print()  # пустая строка

# 5 задание
positions_low_salary = []
for department in departments:
    for item in department["employers"]:
        salary_employee = item['salary_rub']
        if salary_employee < 80000:
            positions_low_salary.append(item['position'])
positions_low_salary_str = ", ".join(positions_low_salary)
print(f"На этих позициях: {positions_low_salary_str} - получают меньше 80000 рублей.")
print()  # пустая строка

# 6 задание
for department in departments:
    sum_salary_of_department = sum_salary_department(department)
    print(f"{department['title']} : {sum_salary_of_department}")
print()  # пустая строка

# 7 задание
for department in departments:
    min_salary_of_department = min_salary_department(department)
    print(f"{department['title']} : {min_salary_of_department}")
print()  # пустая строка

# 8 задание
for department in departments:
    max_salary_of_department = max_salary_department(department)
    min_salary_of_department = min_salary_department(department)
    avg_salary_of_department = avg_salary_department(department)
    print(
        f"{department['title']} : {min_salary_of_department} - минимальная, {avg_salary_of_department} - средняя, {max_salary_of_department} и максимальная зарплаты в отделе.")
print()  # пустая строка

# 9 задание
sum_salary_of_company = 0
sum_employees_of_company = 0
for department in departments:
    sum_salary_of_company += sum_salary_department(department)
    sum_employees_of_company += len(department['employers'])
avg_salary_in_company = sum_salary_of_company / sum_employees_of_company
print(f"Средняя месячная зарплата в компании -  {avg_salary_in_company}")
print()  # пустая строка

# 10 задание
positions_high_salary = set()
for department in departments:
    for item in department["employers"]:
        salary_employee = item['salary_rub']
        if salary_employee > 90000:
            positions_high_salary.add(item['position'])
positions_high_salary_str = ", ".join(positions_high_salary)
print(f"На этих позициях: {positions_high_salary_str} - получают больше 90000 рублей.")
print()  # пустая строка

# 11 задание
avg_women_salary_in_department = 0
sum_women_salary_in_department = 0
women = ["Michelle", "Christina", "Caitlin"]
for department in departments:
    count_of_women = 0
    for item in department['employers']:
        if item['first_name'] in women:
            sum_women_salary_in_department += item["salary_rub"]
            count_of_women += 1
    avg_women_salary_in_department = sum_women_salary_in_department / count_of_women
    print(f"Средняя зарплата в {department['title']} среди женщин: {avg_women_salary_in_department}")
print()  # пустая строка

# 12 задание
name_with_end_vowel = set()
vowels = "aeouiy"
for department in departments:
    for item in department["employers"]:
        if item["last_name"][-1] in vowels:
            name_with_end_vowel.add(item['first_name'])
name_with_end_vowel_str = ", ".join(name_with_end_vowel)
print(f"У этих людей: {name_with_end_vowel_str} - фамилия заканчивается на гласную.")
print()  # пустая строка

# 13 задание
departments_title_dict = {}
for department in departments:
    avg_tax_only_for_department = 0
    avg_salary_of_department = avg_salary_department(department)
    avg_tax_of_department_for_all = taxes_for_department(avg_salary_of_department)
    departments_title_dict['title'] = department['title']
    for item in taxes:
        if item['department'] == departments_title_dict['title']:
            avg_tax_only_for_department += avg_salary_of_department * (item['value_percents'] / 100)
    avg_common_tax_department = avg_tax_of_department_for_all + avg_tax_only_for_department
    print(f"{department['title']}: {avg_common_tax_department}")
print()  # пустая строка
