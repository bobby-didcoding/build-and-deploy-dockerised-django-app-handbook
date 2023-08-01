# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import os
import json

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from ecommerce.models import Price, Product

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from dotenv import load_dotenv
load_dotenv()


User = get_user_model()


class DBConfig:

    def manage_super_user(self)-> User:

        user = User.objects.filter(email = os.environ.get("DOCKER_CONTAINER_EMAIL"))
        if user.exists():
            pass
        else:
            user = User.objects.create(
                email=os.environ.get("DOCKER_CONTAINER_EMAIL"), 
                password=make_password(os.environ.get("DOCKER_CONTAINER_PASSWORD")),
                first_name='Dev',
                last_name='User',
                is_staff = True,
                is_active=False,
                is_superuser = True
                )
        user.is_active = True
        user.save()
        return user

    def manage_site(self):
        site = Site.objects.first()
        site.name = "Main"
        match settings.PRODUCTION:
            case 0:
                site.domain = f"localhost:{settings.RUN_SERVER_PORT}"
            case 1:
                os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")[0]
        site.save()

    def get_object(self, name):
        name = name.split(".")
        app_name = name[0]
        model_name = name[1]
        obj = apps.get_model(app_label=app_name, model_name=model_name)
        return obj
    
    def manage_kwargs(self, my_dict:dict) ->dict:
        for key, value in my_dict.items():

            if key == "price":
                obj = Price.objects.get(id = value)
                my_dict[key] = obj
        
        return my_dict



    def create_object(self, my_dict:dict):
        try:
            model = self.get_object(my_dict["model"])
            fields = self.manage_kwargs(my_dict["fields"])
            if "id" in fields.keys():
                obj = model.objects.filter(id = fields["id"])
                if obj.exists():
                    pass
                else:
                    model.objects.create(**fields)
            else:
                obj, created = model.objects.get_or_create(**fields)
            return obj
        except KeyError:
            raise Exception("'model' keyword is required")

def run():
    db_config = DBConfig()
    db_config.manage_site()
    with open('scripts/config.json',"r",encoding='utf-8') as json_data:
        data = json.load(json_data)
        for c in data:
            db_config.create_object(c)
    db_config.manage_super_user()
