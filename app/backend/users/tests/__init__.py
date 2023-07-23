# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.tests.base import BaseTestCustomUser
from users.tests.models import CustomUserTestCase
# from users.tests.signals import CustomUserSignalTestCase
from users.tests.forms import (
    LoginFormTestCase,
    SignupFormTestCase,
    RequestPasswordFormTestCase
)
from users.tests.views import (
    SignupTestCase,
    LoginTestCase,
    ForgottenPasswordTestCase,
    LogoutViewTestCase
)


__all__ = [
    BaseTestCustomUser,
    CustomUserTestCase,
    # CustomUserSignalTestCase,
    LoginFormTestCase,
    SignupFormTestCase,
    RequestPasswordFormTestCase,
    SignupTestCase,
    LoginTestCase,
    ForgottenPasswordTestCase,
    LogoutViewTestCase
]
