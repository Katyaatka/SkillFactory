from api import PetFriends
from settings import valid_email, valid_password, not_valid_email, not_valid_password
import os


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

     #Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

     #Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
         #если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_add_new_pet_without_photo_with_valid_data(name='Барсик', animal_type='кот', age='7'):
    """(1 написанный тест) Проверяем возможность добавления нового питомца без фото и статус 200"""

    #Получаем список auth_key и добавляем нового питомца
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    #Проверяем, что статус == 200, и имя питомца соответствует заданному
    assert status == 200
    assert result['name'] == name

def test_add_photo_of_pet_with_valid_data(pet_photo='images/cat1.jpg'):
    """(2 написанный тест) Проверяем возможность добавления фото для питомца и статус 200"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем добавить фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа = 200 и в ответе есть 'pet_photo'
        assert status == 200
        assert 'pet_photo' in result
    else:
        # если спиcок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_get_api_key_with_not_valid_email(email=not_valid_email, password=valid_password):
    """(3 написанный тест) Проверяем невозможность получить api key с невалидным логином и получение
    статуса 403"""

    #Запрашиваем auth_key с невалидным email
    status, result = pf.get_api_key(email, password)

    # Сверяем полученный статус с ожидаемым
    assert status == 403

def test_get_api_key_with_not_valid_password(email=valid_email, password=not_valid_password):
    """(4 написанный тест) Проверяем невозможность получить api key с невалидным паролем и получение
    статуса 403"""

    #Запрашиваем auth_key с невалидным паролем
    status, result = pf.get_api_key(email, password)

    # Сверяем полученный статус с ожидаемым
    assert status == 403

def test_add_new_pet_with_not_valid_age(name='Барбоскин', animal_type='двортерьер',
                                     age='fdf', pet_photo='images/cat1.jpg'):
    """(5 написанный тест) Проверяем невозможность добавления нового питомца с некорректными
     данными (не числовой формат возраста) и получение статуса 400 The error code means
     that provided data is incorrect"""

    #Получаем путь до изображения, получаем auth_key и добавляем нового питомца с некорректным возрастом
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    #Сверяем полученный статус с ожидаемым
    assert status == 400

def test_get_all_pets_with_not_valid_key_and_email(filter=''):
    """(6 написанный тест) Проверяем возможность получения ответа 403 The error code means that
    provided combination of user email and password is incorrect при получении списка
    всех питомцев с некорректным api key"""

    #Получаем auth_key, создаем некорректный auth_key, запрашиваем список всех питомцев с некорректным auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    not_valid_auth_key = {'key': auth_key['key'] + '123'}
    status, result = pf.get_list_of_pets(not_valid_auth_key, filter)

    #Сверяем полученный статус с ожидаемым
    assert status == 403

def test_delete_pet_with_incorrect_auth_key():
    """(7 написанный тест) Проверяем возможность получения ответа 403 при
    удалении питомца c некорректным Api key"""

    #Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

     #Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    #Берём id первого питомца из списка и отправляем запрос на удаление с not_valid_auth_key != auth_key
    pet_id = my_pets['pets'][0]['id']
    not_valid_auth_key = {'key': auth_key['key'] + '123'}
    status, _ = pf.delete_pet(not_valid_auth_key, pet_id)

    # Проверяем что статус ответа равен 403
    assert status == 403


def test_delete_pet_with_incorrect_pet_id():
    """(8 написанный тест) Проверяем получение статуса с ошибкой (!=200) при удалении
    питомца с айди, которого не существует"""

    #Получаем ключ auth_key, запрашиваем список своих питомцев,
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

     #Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")


    #Берём id первого питомца из списка и отправляем запрос на удаление с not_valid_pet_id
    pet_id = my_pets['pets'][0]['id']
    not_valid_pet_id = pet_id + "пампампам"
    status, _ = pf.delete_pet(auth_key, not_valid_pet_id)

    # Проверяем что статус ответа !=200
    assert status != 200

def test_add_pet_with_invalid_photo_format(pet_photo='images/tekst_vmesto_photo.docx'):
    """(9 написанный тест) Проверяем возможность добавления файла в формате .docx вместо фото
    и статус ответа !=200"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем добавить фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа != 200
        assert status != 200
    else:
        # если спиcок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_update_self_pet_info_with_negative_age(name='Мурзик', animal_type='Котэ', age=-5):
    """(10 написанный тест) Проверяем возможность изменения возраста на отрицательное значение и
    получение статуса !=200"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа != 200
        assert status != 200
    else:
         #если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")