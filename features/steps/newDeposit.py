from behave import given, when

from pages.LoginPage import LoginPage
from pages.NewDepositPage import NewDepositPage


@when("User open the new deposit page")
def open_new_deposit_page(context):
    context.new_deposit_page = NewDepositPage(context.driver)


@when("I insert in the form")
def fill_form(context):
    for row in context.table:
        name = row['name']
        address = row['address']
        city = row['city']
        state = row['state']
        zipcode = row['zipcode']
        context.new_deposit_page.fill_form(name, address, city, state, zipcode)


@when("User click in create deposit button")
def click_create_deposit(context):
    context.new_deposit_page.click_create_deposit()
