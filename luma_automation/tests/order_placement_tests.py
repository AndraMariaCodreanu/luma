import time

import pytest

from framework.pages.confirmation import ConfirmationPage
from framework.pages.landing import LandingPage
from framework.pages.product_page import ProductPage
from framework.pages.reviews_and_payments import ReviewAndPaymentsPage
from framework.pages.shipping_address import ShippingAddressPage
from framework.pages.shoping_cart import ShoppingCart
from framework.pages.woman import WomanPage

landing_page = LandingPage()

woman_page = WomanPage()
product_page = ProductPage()
shopping_cart_page = ShoppingCart()
shipping_address_page = ShippingAddressPage()
review_page = ReviewAndPaymentsPage()
confirmation_page = ConfirmationPage()


@pytest.mark.e2e
def test_e2e_place_order_already_logged_in(base_ui):
    base_ui.navigate_to_woman_page()
    woman_page.side_bar.tops_category.click()
    assert woman_page.page_title.wait_until_is_displayed()
    time.sleep(3)
    woman_page.select_tees_category_and_select_one_item()
    product_page.enter_product_details_and_add_to_cart()
    shopping_cart_page.get_items_from_cart_from_row(row_number=1)
    assert shopping_cart_page.cart_summary.proceed_to_checkout.wait_until_is_displayed(), \
        'Fail proced to checkout button is not displayed'
    shopping_cart_page.cart_summary.proceed_to_checkout.click()
    assert shipping_address_page.next.wait_until_is_displayed(), \
        'Fail, Next button is not displayed'
    shipping_address_page.next.click()
    assert review_page.place_order.wait_until_is_displayed(), \
        'Fail, Place order button is not displayed'
    review_page.place_order.click()
    assert confirmation_page.page_title.wait_until_is_displayed(), \
        'Fail, Confirmation messag is not displayed'
    assert confirmation_page.continue_shopping.wait_until_is_displayed(), \
        'Fail, Continue shopping button is not displayed'
