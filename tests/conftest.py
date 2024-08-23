import pytest

from dotenv import load_dotenv
import os
from selene import browser
import allure
import requests
from allure_commons.types import AttachmentType


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True)
def setup_browser():
    with allure.step('Конфигурация браузера'):
        browser.config.base_url = os.getenv('URL')
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    yield

    with allure.step('Закрытие браузера'):
        browser.quit()


@pytest.fixture()
def auth_with_api():
    with allure.step('Авторизация'):
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        url = os.getenv('URL')
        response = requests.post(
            url=url + "/login",
            data={"Email": login, 'Password': password},
            allow_redirects=False
        )
        cookie = response.cookies.get('NOPCOMMERCE.AUTH')
        allure.attach(body=response.text, name='Response', attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=cookie, name='Cookie', attachment_type=AttachmentType.TEXT, extension='.txt')
        return cookie
