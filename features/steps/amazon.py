from behave import given, then, when


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.main_page.open_main_page()


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.app.main_page.click_orders()


@then("Verify '{text}' page is opened")
def verify_sign_in_page(context, text):
    context.app.main_page.verify_sign_in_page(text)


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.app.main_page.click_cart()


@then("Verify '{text}' text present")
def verify_cart_is_empty(context, text):
    context.app.main_page.verify_shopping_cart(text)


@when('The search phrase "{product_name}" is entered')
def search_for_product(context, product_name):
    context.app.main_page.search_product(product_name)


@then('Results containing "{product_name}" are shown')
def results_containing_product(context, product_name):
    context.app.main_page.verify_search_result(product_name)


@when('Click on one containing "{product_name}", which has the largest number of reviews')
def click_the_largest_reviews(context, product_name):
    context.app.main_page.click_the_largest_reviews(product_name)


@then('The product page is shown, and it has an add to cart button')
def product_page(context):
    context.app.main_page.verify_add_to_cart_button()


@then('Click on the Add to Cart button')
def click_add_to_cart(context):
    context.app.main_page.click_add_to_cart()


@when('Click on the Cart icon')
def click_cart(context):
    context.app.main_page.click_cart()


@then('Verify "{product_name}" is in the cart')
def verify_cart(context, product_name):
    context.app.main_page.verify_cart_has_item(product_name)
