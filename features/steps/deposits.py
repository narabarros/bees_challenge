from behave import given, when

from pages.DepositPage import DepositPage


@when("User open the deposit page")
def open_deposit_page(context):
    context.deposits_page = DepositPage(context.driver)


@when("User click in new deposit button")
def click_new_deposit(context):
    context.deposits_page.click_new_deposit()


