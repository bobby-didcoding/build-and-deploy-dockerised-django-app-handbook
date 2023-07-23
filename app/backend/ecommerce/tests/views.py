# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import get_random_string, get_random_email
from users.tests import BaseTestCustomUser
from ecommerce.models import Customer, Cart

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Product, Price, Session

@override_settings(SUSPEND_SIGNALS=True)
class EcommerceViewTestBase(BaseTestCustomUser, TestCase):

    def setUp(self):

        self.user = self.get_test_active_user()
        self.customer = Customer.objects.create(user = self.user)
        self.cart = Cart.objects.create(customer = self.customer)
        self.session = Session.objects.create(customer = self.customer)

        self.price, created = Price.objects.get_or_create(amount=10.0)
        self.product, created = Product.objects.get_or_create(
            title="Test product",
            description="Test description",
            price = self.price,
            )
        self.product2, created = Product.objects.get_or_create(
            title="Test product2",
            description="Test description",
            price = self.price,
            )
        
        self.cart.products.add(self.product)
        self.cart.save()
        
        self.client = Client()
        

class CartViewTestCase(EcommerceViewTestBase):
    """
    Test suite for CartView
    """

    def test_cart_view_get_request(self):
        self.client.force_login(self.user)
        response = self.client.get("/cart/")
        
        self.assertEqual(response.status_code, 200)

    def test_cart_view_put_request(self):
        self.client.force_login(self.user)
        response = self.client.put("/cart/")
        
        self.assertEqual(response.status_code, 405)

    def test_cart_view_delete_request(self):
        self.client.force_login(self.user)
        response = self.client.delete("/cart/")
        
        self.assertEqual(response.status_code, 405)


class ManageCartViewTestCase(EcommerceViewTestBase):
    """
    Test suite for ManageCartView
    """

    def test_manage_cart_view_get_request(self):
        product = self.product
        self.client.force_login(self.user)
        response = self.client.get(f"/manage-cart/{product.id}/'add'/")
        
        self.assertEqual(response.status_code, 200)
    
    def test_manage_cart_view_put_request(self):
        product = self.product
        self.client.force_login(self.user)
        response = self.client.put(f"/manage-cart/{product.id}/add/")
        
        self.assertEqual(response.status_code, 200)

    def test_manage_cart_view_delete_request(self):
        product = self.product
        self.client.force_login(self.user)
        response = self.client.delete(f"/manage-cart/{product.id}/add/")
        
        self.assertEqual(response.status_code, 200)

    def test_manage_cart_view_post_request(self):
        product = self.product
        self.client.force_login(self.user)
        response = self.client.post(f"/manage-cart/{product.id}/add/")
        self.assertEqual(self.cart.products.all().count(),1)
        self.assertEqual(response.status_code, 200)

    def test_manage_cart_view_post_request_add_product_with_ajax(self):
        product = self.product2
        self.client.force_login(self.user)
        cart = self.cart
        self.assertEqual(cart.products.all().count(),1)
        response = self.client.post(f"/manage-cart/{product.id}/add/", HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(cart.products.all().count(),2)

    def test_manage_cart_view_post_request_remove_product_with_ajax(self):
        product = self.product
        self.client.force_login(self.user)
        cart = self.cart
        self.assertEqual(cart.products.all().count(),1)
        response = self.client.post(f"/manage-cart/{product.id}/remove/", HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(cart.products.all().count(),0)


class SessionCreateViewTestCase(EcommerceViewTestBase):
    """
    Test suite for SessionCreateView
    """

    def test_create_session_view_get_request(self):
        self.client.force_login(self.user)
        response = self.client.get(f"/session-create/")
        
        self.assertEqual(response.status_code, 200)
    
    def test_create_session_view_put_request(self):
        self.client.force_login(self.user)
        response = self.client.put(f"/session-create/")
        
        self.assertEqual(response.status_code, 200)

    def test_create_session_view_delete_request(self):
        self.client.force_login(self.user)
        response = self.client.delete(f"/session-create/")
        
        self.assertEqual(response.status_code, 200)

    def test_create_session_view_post_request(self):
        self.client.force_login(self.user)
        response = self.client.post(f"/session-create/")
        self.assertEqual(response.status_code, 200)

    def test_create_session_view_post_request_with_ajax(self):
        self.client.force_login(self.user)
        response = self.client.post(f"/session-create/", HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

class SessionSuccessViewTestCase(EcommerceViewTestBase):
    """
    Test suite for SessionSuccessView
    """

    def test_session_success_view_get_request(self):
        self.client.force_login(self.user)
        session = self.session
        response = self.client.get(f"/session-success/{session.id}/")
        
        self.assertEqual(response.status_code, 200)
    
    def test_session_success_view_put_request(self):
        self.client.force_login(self.user)
        session = self.session
        response = self.client.put(f"/session-success/{session.id}/")
        
        self.assertEqual(response.status_code, 405)

    def test_session_success_view_delete_request(self):
        self.client.force_login(self.user)
        session = self.session
        response = self.client.delete(f"/session-success/{session.id}/")
        
        self.assertEqual(response.status_code, 405)

    def test_session_success_view_post_request(self):
        self.client.force_login(self.user)
        session = self.session
        response = self.client.post(f"/session-success/{session.id}/")
        self.assertEqual(response.status_code, 405)


class SessionCancelViewTestCase(EcommerceViewTestBase):
    """
    Test suite for SessionCancelView
    """

    def test_session_cancel_view_get_request(self):
        self.client.force_login(self.user)
        session = self.session
        response = self.client.get(f"/session-cancelled/{session.id}/")
        
        self.assertEqual(response.status_code, 200)
    
    def test_session_cancel_view_put_request(self):
        self.client.force_login(self.user)
        session = self.session
        response = self.client.put(f"/session-cancelled/{session.id}/")
        
        self.assertEqual(response.status_code, 405)

    def test_session_cancel_view_delete_request(self):
        self.client.force_login(self.user)
        session = self.session
        response = self.client.delete(f"/session-cancelled/{session.id}/")
        
        self.assertEqual(response.status_code, 405)

    def test_session_cancel_view_post_request(self):
        self.client.force_login(self.user)
        session = self.session
        response = self.client.post(f"/session-cancelled/{session.id}/")
        self.assertEqual(response.status_code, 405)


class ProductsViewTestCase(EcommerceViewTestBase):
    """
    Test suite for Products
    """

    def test_products_view_get_request(self):
        client = self.client
        response = client.get("/products/")
        
        self.assertEqual(response.status_code, 200)

    def test_products_view_post_request(self):
        client = self.client
        response = client.post("/products/")
        
        self.assertEqual(response.status_code, 405)

    def test_products_view_put_request(self):
        client = self.client
        response = client.put("/products/")
        
        self.assertEqual(response.status_code, 405)

    def test_products_view_delete_request(self):
        client = self.client
        response = client.delete("/products/")
        
        self.assertEqual(response.status_code, 405)


class ProductViewTestCase(EcommerceViewTestBase):
    """
    Test suite for Product
    """

    def test_product_view_get_request(self):
        client = self.client
        response = client.get(self.product.get_absolute_url())
        
        self.assertEqual(response.status_code, 200)

    def test_product_view_post_request(self):
        client = self.client
        response = client.post(self.product.get_absolute_url())
        
        self.assertEqual(response.status_code, 405)

    def test_product_view_put_request(self):
        client = self.client
        response = client.put(self.product.get_absolute_url())
        
        self.assertEqual(response.status_code, 405)

    def test_product_view_delete_request(self):
        client = self.client
        response = client.delete(self.product.get_absolute_url())
        
        self.assertEqual(response.status_code, 405)

