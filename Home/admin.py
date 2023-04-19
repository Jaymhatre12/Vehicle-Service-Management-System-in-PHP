import site
from django.contrib import admin
from Home.models import Signup
from Home.models import SignupEWC
# Register your models here.
admin.site.register(Signup)
admin.site.register(SignupEWC)