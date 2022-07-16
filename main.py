from datetime import datetime
from application.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    data_time_ = datetime.today()
    print(f'Привет! Сейчас:{data_time_}')
    get_employees()
    calculate_salary()
