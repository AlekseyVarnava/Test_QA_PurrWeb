import random
import datetime

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()

def generated_person():
    yield Person(
        email_me=faker_ru.ascii_free_email(),
        first_name=fake_en.first_name_male(),
    )

def generated_file():
    list_extension = ['doc', 'docx', 'pdf', 'ppsx', 'ppt', 'pptx', 'jpg', 'jpeg', 'bmp', 'png', 'xls', 'xlsx', 'txt', 'html', 'gif']
    number_extension = random.randint(0, 14)
    extension = list_extension[number_extension]
    path = rf'D:\Job_by_Aleksey_IT\PurrWeb\Test_QA-PurrWEB\generator\filetest\file{random.randint(0, 999)}.{extension}'
    file = open(path, 'w+')
    file.write(f'Hello PurrWeb\nIn this test, we used the file format: - {extension}')
    file.close()
    return file.name, path