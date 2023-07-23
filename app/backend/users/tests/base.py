# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseTestCustomUser:
    def get_test_active_user(self):
        active_user = User.objects.filter(email="test_active@test.com")
        if active_user.exists():
            active_user = active_user.first()
        else:
            active_user = User.objects.create(
                email="test_active@test.com",
                first_name="Test",
                last_name="Case",
                password=make_password("fredfred1"),
                is_active=True,
            )
        return active_user

    def get_test_inactive_user(self):
        inactive_user = User.objects.filter(email="test_inactive@test.com")
        if inactive_user.exists():
            inactive_user = inactive_user.first()
        else:
            inactive_user = User.objects.create(
                email="test_inactive@test.com",
                first_name="Test",
                last_name="Case",
                password=make_password("fredfred1"),
            )
        return inactive_user

    def get_test_superuser(self):
        superuser = User.objects.filter(email="test_superuser@test.com")
        if superuser.exists():
            superuser = superuser.first()
        else:
            superuser = User.objects.create(
                email="test_superuser@test.com",
                first_name="Test",
                last_name="Case",
                password=make_password("fredfred1"),
                is_superuser=True,
                is_staff=True,
                is_active=True,
            )
        return superuser

    def get_test_staff(self):
        staff_user = User.objects.filter(email="test_staff@test.com")
        if staff_user.exists():
            staff_user = staff_user.first()
        else:
            staff_user = User.objects.create(
                email="test_staff@test.com",
                first_name="Test",
                last_name="Case",
                password=make_password("fredfred1"),
                is_staff=True,
                is_active=True,
            )
        return staff_user
