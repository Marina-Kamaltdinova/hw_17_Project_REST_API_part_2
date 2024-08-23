import allure
from selene import browser, have
from utils.methods import add_product_to_cart, clear_cart


def test_add_laptop_to_cart(auth_with_api):
    with allure.step('Вход на сайт авторизованным пользователем'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_with_api})
        browser.open('/')

    with allure.step('Проверка статуса добавления товара в корзину'):
        response_code = add_product_to_cart(product_url='/addproducttocart/details/31/1', cookie=auth_with_api)
        assert response_code == 200

    with allure.step('Переход в корзину'):
        browser.element('.ico-cart .cart-label').click()

    with allure.step('Отображение товара в корзине'):
        browser.element('.product-name').should(have.text('14.1-inch Laptop'))

    clear_cart()


def test_add_sneaker_to_cart(auth_with_api):
    with allure.step('Вход на сайт авторизованным пользователем'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_with_api})
        browser.open('/')

    with allure.step('Проверка статуса добавления товара в корзину'):
        response_code = add_product_to_cart(product_url='/addproducttocart/details/28/1', cookie=auth_with_api, data={
            'product_attribute_28_7_10': 25,
            'product_attribute_28_1_11': 29
        })
        assert response_code == 200

    with allure.step('Переход в корзину'):
        browser.element('.ico-cart .cart-label').click()

    with allure.step('Отображение товара в корзине'):
        browser.element('.product-name').should(have.text('Blue and green Sneaker'))

    clear_cart()
