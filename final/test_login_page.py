from .pages.login_page import LoginPage

def test_guest_should_see_authorization_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()