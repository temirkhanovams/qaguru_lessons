from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function')
def browser_init():
    print('\nОткрываю браузер')
    browser.config.window_width = 1024
    browser.config.window_height = 780
    browser.open('https://google.com')

    yield

    print('\nЗакрываю браузер')
    browser.quit()