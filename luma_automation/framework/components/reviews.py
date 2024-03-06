from framework.components import button, base_component


class ReviewsLocators:
    rating_result_locator = '//div[@class="rating-result"]'
    reviews_locator = '//a[@class="action view"]'
    add_review_locator = '//a[@class="action add"]'


class Reviews(ReviewsLocators, base_component.BaseComponent):
    def __init__(self, locator):
        super().__init__(locator=locator)
        self.rating_result = base_component.BaseComponent(locator=f'{self._locator}{self.rating_result_locator}')
        self.reviews = button.Button(locator=f'{self._locator}{self.reviews_locator}')
        self.add_review = button.Button(locator=f'{self._locator}{self.add_review_locator}')

    def get_rating(self):
        return self.rating_result.title

    def get_reviews_count(self):
        return self.reviews.text
