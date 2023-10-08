from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function')
def browser_init():
    print('Открываю браузер')
    browser.config.window_width = 1024
    browser.config.window_height = 780
    browser.open('https://google.com')

    yield

    print('Закрываю браузер')
    browser.quit()