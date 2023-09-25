import pytest


@pytest.fixture
def browser():
    print('Выполняюсь перед тестом')

    yield

    print('Выполняюсь после теста')

@pytest.fixture
def main_page(browser):
    print('Выполняю main_page')


@pytest.fixture
def user():
    print('Тестовый юзер перед тестом')

    yield

    print('Откат тестового юзера после теста')


def test_first(browser, user, main_page):
    pass
