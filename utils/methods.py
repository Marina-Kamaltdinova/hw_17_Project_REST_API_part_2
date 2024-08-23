import os
import logging
import allure
from allure_commons.types import AttachmentType
import requests
from selene import browser


def add_product_to_cart(product_url, cookie, data=False):
    with allure.step('Добавление товара в корзину через API'):
        url = os.getenv('URL')
        response = requests.post(
            url=url + product_url,
            data=data,
            cookies={"NOPCOMMERCE.AUTH": cookie},
            allow_redirects=False
        )
        allure.attach(body=response.text, name='Response', attachment_type=AttachmentType.TEXT, extension='.txt')
        logging.info(response.status_code)
        logging.info(response.text)
        return response.status_code


def clear_cart():
    with allure.step('Очистить корзину'):
        browser.element('.qty-input').set_value('0').press_enter()
