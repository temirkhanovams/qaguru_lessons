from selene.support.shared import browser
from selene import be, have, query
import pytest




@pytest.fixture
def browser_init():
    print('Открываю браузер')
    browser.config.window_width = 1024
    browser.config.window_height = 780
    browser.open('https://google.com')

    yield

    print('Закрываю браузер')
    browser.quit()



def test_search_wrong(browser_init):
    browser.element('[name="q"]').should(be.blank).type('12345678(*&^%$#@WERHJNBVCX').press_enter()
    browser.element('#extabar #result-stats').should(have.text('Результатов: примерно 0'))
