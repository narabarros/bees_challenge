from behave import given, when

from pages.LoginPage import LoginPage


@given("User open bees web page")
def open_page(context):
    context.login_page = LoginPage(context.driver)


@when('User sign in as "email" and "password"')
def sign_in(context):
    context.login_page.sign_in('narabarroscruz@gmail.com', '141094a@n')


@when("User click in submit button")
def click_submit(context):
    context.login_page.click_submit()
