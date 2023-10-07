from selene.support.shared import browser
from selene import be, have

def test_form():
    browser.open('https://demoqa.com/text-box')
    browser.element('#userName').type('Marina')
    browser.element('#userEmail').type('name@name.com')
    browser.element('#currentAddress-wrapper #currentAddress').type('New York')
    browser.element('#permanentAddress-wrapper #permanentAddress').type('Moscow')
    browser.element('#submit').click()
    browser.element('#name').should(have.text('Marina'))
    browser.element('#email').should(have.text('name@name.com'))
    browser.element('#output #currentAddress').should(have.text('New York'))
    browser.element('#output #permanentAddress').should(have.text('Moscow'))
    browser.element('#output').should(be.visible)