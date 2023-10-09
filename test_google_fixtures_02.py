from selene.support.shared import browser
from selene import be, have


def test_search_yashaka(browser_init):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser'))


def test_search_none(browser_init):
    browser.element('[name="q"]').should(be.blank).type('12345678(*&^%$#@WERHJNBVCX').press_enter()
    browser.element('#extabar #result-stats').should(have.text('Результатов: примерно 0'))
    browser.element('p[role="heading"]').should(have.text(r'По запросу 12345678(*&^%$#@WERHJNBVCX ничего не найдено.'))
