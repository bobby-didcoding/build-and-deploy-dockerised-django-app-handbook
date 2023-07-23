# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.test import TestCase
from django.test.client import Client

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import get_random_string, get_random_email

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Blog, Policy, Portfolio


class CoreViewTestBase:

    def setUp(self):

        self.client = Client()
        self.blog = Blog.objects.create(title="Test blog")
        self.portfolio = Portfolio.objects.create(title="Test portfolio")
        self.policy = Policy.objects.create(title="Test policy")

class HomeViewTestCase(CoreViewTestBase, TestCase):
    """
    Test suite for HomeView
    """

    def test_home_view_get_request(self):
        client = self.client
        response = client.get("/")
        
        self.assertEqual(response.status_code, 200)

    def test_home_view_post_request(self):
        client = self.client
        response = client.post("/")
        
        self.assertEqual(response.status_code, 405)

    def test_home_view_put_request(self):
        client = self.client
        response = client.put("/")
        
        self.assertEqual(response.status_code, 405)

    def test_home_view_delete_request(self):
        client = self.client
        response = client.delete("/")
        
        self.assertEqual(response.status_code, 405)


class BlogsViewTestCase(CoreViewTestBase, TestCase):
    """
    Test suite for BlogsView
    """

    def test_blogs_view_get_request(self):
        client = self.client
        response = client.get("/blog/")
        
        self.assertEqual(response.status_code, 200)

    def test_blogs_view_post_request(self):
        client = self.client
        response = client.post("/blog/")
        
        self.assertEqual(response.status_code, 405)

    def test_blogs_view_put_request(self):
        client = self.client
        response = client.put("/blog/")
        
        self.assertEqual(response.status_code, 405)

    def test_blogs_view_delete_request(self):
        client = self.client
        response = client.delete("/blog/")
        
        self.assertEqual(response.status_code, 405)


class BlogViewTestCase(CoreViewTestBase, TestCase):
    """
    Test suite for BlogView
    """

    def test_blog_view_get_request(self):
        client = self.client
        response = client.get(f'{self.blog.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 200)

    def test_blog_view_post_request(self):
        client = self.client
        response = client.post(f'{self.blog.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 405)

    def test_blog_view_put_request(self):
        client = self.client
        response = client.put(f'{self.blog.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 405)

    def test_blog_view_delete_request(self):
        client = self.client
        response = client.delete(f'{self.blog.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 405)


class PoliciesViewTestCase(CoreViewTestBase, TestCase):
    """
    Test suite for PoliciesView
    """

    def test_policies_view_get_request(self):
        client = self.client
        response = client.get("/policies/")
        
        self.assertEqual(response.status_code, 200)

    def test_policies_view_post_request(self):
        client = self.client
        response = client.post("/policies/")
        
        self.assertEqual(response.status_code, 405)

    def test_policies_view_put_request(self):
        client = self.client
        response = client.put("/policies/")
        
        self.assertEqual(response.status_code, 405)

    def test_policies_view_delete_request(self):
        client = self.client
        response = client.delete("/policies/")
        
        self.assertEqual(response.status_code, 405)


class PolicyViewTestCase(CoreViewTestBase, TestCase):
    """
    Test suite for Policy
    """

    def test_policy_view_get_request(self):
        client = self.client
        response = client.get(f'{self.policy.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 200)

    def test_policy_view_post_request(self):
        client = self.client
        response = client.post(f'{self.policy.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 405)

    def test_policy_view_put_request(self):
        client = self.client
        response = client.put(f'{self.policy.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 405)

    def test_policy_view_delete_request(self):
        client = self.client
        response = client.delete(f'{self.policy.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 405)


class PortfoliosViewTestCase(CoreViewTestBase, TestCase):
    """
    Test suite for PortfoliosView
    """

    def test_portfolio_view_get_request(self):
        client = self.client
        response = client.get("/portfolio/")
        
        self.assertEqual(response.status_code, 200)

    def test_portfolio_view_post_request(self):
        client = self.client
        response = client.post("/portfolio/")
        
        self.assertEqual(response.status_code, 405)

    def test_portfolio_view_put_request(self):
        client = self.client
        response = client.put("/portfolio/")
        
        self.assertEqual(response.status_code, 405)

    def test_portfolio_view_delete_request(self):
        client = self.client
        response = client.delete("/portfolio/")
        
        self.assertEqual(response.status_code, 405)


class PortfolioViewTestCase(CoreViewTestBase, TestCase):
    """
    Test suite for Portfolio
    """

    def test_portfolio_view_get_request(self):
        client = self.client
        response = client.get(f'{self.portfolio.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 200)

    def test_portfolio_view_post_request(self):
        client = self.client
        response = client.post(f'{self.portfolio.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 405)

    def test_portfolio_view_put_request(self):
        client = self.client
        response = client.put(f'{self.portfolio.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 405)

    def test_portfolio_view_delete_request(self):
        client = self.client
        response = client.delete(f'{self.portfolio.get_absolute_url()}/')
        
        self.assertEqual(response.status_code, 405)
