from pytest_bdd import scenarios, parsers, given, when, then
from pytest_bdd_template.cucumbers import CucumberBasket


EXTRA_TYPES = {
    'Number': int,
}

scenarios('../features')


@given(parsers.cfparse('the basket has {initial:d} cucumbers', extra_types=EXTRA_TYPES), target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('{some:d} cucumbers are added to the basket', extra_types=EXTRA_TYPES))
def add_cucumbers(basket, some):
    basket.add(some)


@when(parsers.cfparse('{some:d} cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the basket contains {total:d} cucumbers', extra_types=EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total, "the number of remaining baskets was calculated incorrectly"