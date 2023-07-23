# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.tests.models import(
    PriceTestCase,
    ProductTestCase,
    CustomerTestCase,
    CartTestCase,
    SessionItemTestCase,
    SessionTestCase
)

from ecommerce.tests.views import(
    CartViewTestCase,
    ManageCartViewTestCase,
    SessionCreateViewTestCase,
    SessionSuccessViewTestCase,
    SessionCancelViewTestCase,
    ProductsViewTestCase,
    ProductViewTestCase
)


__all__ = [

    PriceTestCase,
    ProductTestCase,
    CustomerTestCase,
    CartTestCase,
    SessionItemTestCase,
    SessionTestCase,
    CartViewTestCase,
    ManageCartViewTestCase,
    SessionCreateViewTestCase,
    SessionSuccessViewTestCase,
    SessionCancelViewTestCase,
    ProductViewTestCase,
    ProductsViewTestCase
]
