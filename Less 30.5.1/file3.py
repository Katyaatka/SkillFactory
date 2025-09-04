import re
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def open_browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get('https://petfriends.skillfactory.ru/')


    browser.find_element(By.XPATH, '(//button[@class = "btn btn-success"])').click()

    browser.find_element(By.LINK_TEXT, 'У меня уже есть аккаунт').click()

    field_login = browser.find_element(By.CSS_SELECTOR, 'input#email')
    field_login.clear()
    field_login.send_keys('katyaatka181001@gmail.com')

    field_pass = browser.find_element(By.CSS_SELECTOR, 'input#pass')
    field_pass.clear()
    field_pass.send_keys('Katyaatja')

    browser.find_element(By.XPATH, '(//button[@class = "btn btn-success"])').click()

    yield browser

    browser.quit()

def test_pf(open_browser):
    '''Проверка, что все питомцы отображаются на странице'''

    browser = open_browser

    click_button = browser.find_element(By.LINK_TEXT, 'Мои питомцы')
    click_button.click()
    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "all_my_pets")))

    pets = browser.find_elements(By.CSS_SELECTOR, 'tbody > tr')
    number = browser.find_element(By.XPATH, "//div[contains(., 'Питомцев')]").text
    pets_number = re.search(r'\d+', number).group()
    print(pets_number)

    assert len(pets) == int(pets_number), "Не все питомцы отображаются на странице"

def test_pet_photo(open_browser):
    '''Проверка того, что количество питомцев с фото больше, чем количество питомцев без фото'''

    browser = open_browser

    click_button = browser.find_element(By.LINK_TEXT, 'Мои питомцы')
    click_button.click()

    elements = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'tbody th'))
    )

    with_photo = []
    with_no_photo = []

    pet_cards = browser.find_elements(By.CSS_SELECTOR, 'tbody > tr')
    for pet in pet_cards:

        image = pet.find_element(By.TAG_NAME, 'img')
        src = image.get_attribute('src')

        if src != '':
            with_photo.append(src)
        else:
            with_no_photo.append(src)

    assert len(with_photo) > len(with_no_photo), "Количество питомцев с фото не больше количества питомцев без фото"

def test_name_age_type(open_browser):
    '''Проверка того, что у всех питомцев есть имя, порода, возраст'''

    browser = open_browser


    click_button = browser.find_element(By.LINK_TEXT, 'Мои питомцы')
    click_button.click()

    elements = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'tbody tr'))
    )

    checked_pets = []


    pet_cards = browser.find_elements(By.CSS_SELECTOR, 'tbody tr')
    for pet in pet_cards:
        tds = pet.find_elements(By.TAG_NAME, 'td')
        td_text = [td.text.strip() for td in tds]
        if all(td_text):
            checked_pets.append(td_text)


    assert len(checked_pets) == len(pet_cards), "Не у всех питомцев есть имя/порода/возраст"

def test_different_name(open_browser):
    '''Проверка того, что у всех питомцев разные имена'''

    browser = open_browser

    click_button = browser.find_element(By.LINK_TEXT, 'Мои питомцы')
    click_button.click()

    elements = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr/td[1]'))
    )

    all_names = []

    pet_cards = browser.find_elements(By.CSS_SELECTOR, 'tbody tr')
    for pet in pet_cards:
        first_td = pet.find_element(By.TAG_NAME, 'td')

        all_names.append(first_td.text)
    names = set(all_names)

    # print(all_names)
    # print(names)

    assert len(names) == len(all_names), "Есть одинаковые имена"

def test_unique_pets(open_browser):
    '''Проверка того, что нет повторяющихся питомцев'''

    browser = open_browser

    click_button = browser.find_element(By.LINK_TEXT, 'Мои питомцы')
    click_button.click()

    elements = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.ID, 'all_my_pets')))

    all_names = []
    names = set()

    pet_cards = browser.find_elements(By.CSS_SELECTOR, 'tbody tr')
    for pet in pet_cards:
        tds = pet.find_elements(By.TAG_NAME, 'td')
        td_text = [td.text.strip() for td in tds]
        all_names.append(tuple(td_text))
        names.add(tuple(td_text))

    print(all_names)
    print(names)

    assert len(names) == len(all_names), "Есть повторяющиеся питомцы"