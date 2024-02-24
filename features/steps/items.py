from behave import *

from pages.ItemsPage import ItemsPage

use_step_matcher("re")


@when("User open items page")
def open_page(context):
    context.items_page = ItemsPage(context.driver)


@when("User click in new item button")
def click_new_item(context):
    context.items_page.click_new_item()
