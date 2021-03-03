from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class MainPage(Page):
    ORDERS_LINK = (By.XPATH, "//a[contains(@href, 'order-history?ref_=nav_orders_first')]")
    CART_ICON = (By.ID, "nav-cart")
    SIGN_IN_TEXT = (By.XPATH, "//h1")
    CART_EMPTY_TEXT = (By.XPATH, "//div[contains(@class, 'sc-your-amazon-cart-is-empty')]//h2")
    SEARCH_BAR = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    SEARCH_RESULT = (By.XPATH, "//a[@class='a-link-normal a-text-normal']//span")
    ADD_TO_CART_BT = (By.ID, "add-to-cart-button")
    ITEM = (By.XPATH, "//span[@class='a-size-medium sc-product-title a-text-bold']")
    POPOVER = (By.XPATH, "//button[contains(@id,'NoCoverage-announce')]")
    CLOSE_BT = (By.XPATH, "//a[contains(@class, 'close-button')]")

    def open_main_page(self):
        self.open_page("https://www.amazon.com")

    def click_orders(self):
        self.click(*self.ORDERS_LINK)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def verify_sign_in_page(self, text):
        self.verify_text(text, *self.SIGN_IN_TEXT)

    def verify_shopping_cart(self, text):
        self.verify_text(text, *self.CART_EMPTY_TEXT)

    def search_product(self, product_name):
        self.input_text(product_name, *self.SEARCH_BAR, enter=True)

    def verify_search_result(self, product_name):
        self.verify_list_has_value(product_name, *self.SEARCH_RESULT)

    def verify_add_to_cart_button(self):
        bt = self.find_elements(*self.ADD_TO_CART_BT)
        assert bt, "There's no Add to Cart button"

    def verify_cart_has_item(self, product_name):
        self.verify_list_has_value(product_name, *self.ITEM)

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BT)
        try:
            self.wait_for_element_click(*self.POPOVER)
            self.wait_for_element_click(*self.CLOSE_BT)
        except TimeoutException:
            pass

    def click_the_largest_reviews(self, product_name):
        results = self.find_elements(*self.SEARCH_RESULT)
        # Create a list having elements containing product name
        links = [p for p in results if all(item in p.text.lower().split() for item in product_name.lower().split())]
        # Create an empty list to store the number of reviews
        reviews = []

        for p in links:
            try:
                # Store the number of reviews to the list
                reviews.append(
                    int(p.find_element(By.XPATH, "./../../../..//span[@class='a-size-base']").text.replace(",", "")))
            # if there's no review, append 0
            except NoSuchElementException:
                reviews.append(0)

        # click the link that has the largest number of reviews
        links[reviews.index(max(reviews))].click()
