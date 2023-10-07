from selene.support.shared import browser
from selene import be, have, query
import pytest


def test_search_yashaka(browser_init):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('selene: User-oriented Web UI browser'))


def test_search_none(browser_init):
    browser.element('[name="q"]').should(be.blank).type('12345678(*&^%$#@WERHJNBVCX').press_enter()
    browser.element('#extabar #result-stats').should(have.text('Результатов: примерно 0'))
