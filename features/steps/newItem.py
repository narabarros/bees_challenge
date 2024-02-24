from behave import given, when

from pages.LoginPage import LoginPage
from pages.NewItemPage import NewItemPage


@when("User open the new item page")
def open_new_item_page(context):
    context.new_item_page = NewItemPage(context.driver)


@when("User insert in the form")
def fill_form(context):
    for row in context.table:
        name = row['name']
        height = row['height']
        width = row['width']
        weight = row['weight']
        context.new_item_page.fill_form(name, height, width, weight)


@when("User click in create item button")
def click_create_item(context):
    context.new_item_page.click_create_item()
