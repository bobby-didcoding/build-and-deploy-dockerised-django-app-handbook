# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.test import TestCase


# --------------------------------------------------------------
# App Party imports
# --------------------------------------------------------------
from core.models import (
    Blog,
    Certificate,
    Contact,
    NewsLetter,
    Policy,
    Portfolio,
    Skill,
    Testimonial,
)


class BlogTestCase(TestCase):
    """
    Test suite for Blog
    """

    def create_obj(self):
        obj, created = Blog.objects.get_or_create(
            title="Test blog", description="This is a test"
        )
        return obj

    def test_blog_creation(self):
        obj = self.create_obj()
        self.assertTrue(isinstance(obj, Blog))
        self.assertEqual(obj.__str__(), "Test blog")
        self.assertEqual(obj.status, 1)
        self.assertEqual(obj.slug, "test-blog")

    def test_blog_get_absolute_url_method(self):
        obj = self.create_obj()
        self.assertEqual(obj.get_absolute_url(), "/blog/test-blog")


class PolicyTestCase(TestCase):
    """
    Test suite for Policy
    """

    def create_obj(self):
        obj, created = Policy.objects.get_or_create(
            title="Test policy", description="This is a test"
        )
        return obj

    def test_policy_creation(self):
        obj = self.create_obj()
        self.assertTrue(isinstance(obj, Policy))
        self.assertEqual(obj.__str__(), "Test policy")
        self.assertEqual(obj.status, 1)
        self.assertEqual(obj.slug, "test-policy")

    def test_policy_get_absolute_url_method(self):
        obj = self.create_obj()
        self.assertEqual(obj.get_absolute_url(), "/policy/test-policy")


class PortfolioTestCase(TestCase):
    """
    Test suite for Portfolio
    """

    def create_obj(self):
        obj, created = Portfolio.objects.get_or_create(
            title="Test portfolio", description="This is a test"
        )
        return obj

    def test_portfolio_creation(self):
        obj = self.create_obj()
        self.assertTrue(isinstance(obj, Portfolio))
        self.assertEqual(obj.__str__(), "Test portfolio")
        self.assertEqual(obj.status, 1)
        self.assertEqual(obj.slug, "test-portfolio")

    def test_portfolio_get_absolute_url_method(self):
        obj = self.create_obj()
        self.assertEqual(obj.get_absolute_url(), "/portfolio/test-portfolio")


class CertificateTestCase(TestCase):
    """
    Test suite for Certificate
    """

    def create_obj(self):
        obj, created = Certificate.objects.get_or_create(
            title="Test certificate", description="This is a test"
        )
        return obj

    def test_certificate_creation(self):
        obj = self.create_obj()
        self.assertTrue(isinstance(obj, Certificate))
        self.assertEqual(obj.__str__(), "Test certificate")
        self.assertEqual(obj.status, 1)
        self.assertEqual(obj.slug, "test-certificate")


class SkillTestCase(TestCase):
    """
    Test suite for Skill
    """

    def create_obj(self):
        obj, created = Skill.objects.get_or_create(
            title="Test skill", description="This is a test", score=90
        )
        return obj

    def test_skill_creation(self):
        obj = self.create_obj()
        self.assertTrue(isinstance(obj, Skill))
        self.assertEqual(obj.__str__(), "Test skill")
        self.assertEqual(obj.status, 1)
        self.assertEqual(obj.slug, "test-skill")


class TestimonialTestCase(TestCase):
    """
    Test suite for Testimonial
    """

    def create_obj(self):
        obj, created = Testimonial.objects.get_or_create(
            title="Test testimonial", description="This is a test"
        )
        return obj

    def test_testimonial_creation(self):
        obj = self.create_obj()
        self.assertTrue(isinstance(obj, Testimonial))
        self.assertEqual(obj.__str__(), "Test testimonial")
        self.assertEqual(obj.status, 1)
        self.assertEqual(obj.slug, "test-testimonial")


class ContactTestCase(TestCase):
    """
    Test suite for Contact
    """

    def create_obj(self):
        obj, created = Contact.objects.get_or_create(
            name="Test Contact", email="contact@test.com", message="This is a test"
        )
        return obj

    def test_contact_creation(self):
        obj = self.create_obj()
        self.assertTrue(isinstance(obj, Contact))
        self.assertEqual(obj.__str__(), "Test Contact")
        self.assertEqual(obj.status, 1)


class NewsLetterTestCase(TestCase):
    """
    Test suite for NewsLetter
    """

    def create_obj(self):
        obj, created = NewsLetter.objects.get_or_create(nl_email="newsletter@test.com")
        return obj

    def test_newsletter_creation(self):
        obj = self.create_obj()
        self.assertTrue(isinstance(obj, NewsLetter))
        self.assertEqual(obj.__str__(), "newsletter@test.com")
        self.assertEqual(obj.status, 1)
