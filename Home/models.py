from msilib.schema import MsiPatchHeaders


# username:MP
# password:54321
from django.db import models

# Create your models here.
class Signup(models.Model):
    u_name = models.CharField(max_length=122)
    u_email = models.CharField(max_length=122)
    u_password = models.CharField(max_length=122)
    u_rpassword = models.CharField(max_length=122)

    def __str__(self):
        return self.u_name

class SignupEWC(models.Model):
    d_name = models.CharField(max_length=122)
    d_email = models.CharField(max_length=122)
    d_password = models.CharField(max_length=122)
    d_rpassword = models.CharField(max_length=122)

    def __str__(self):
        return self.d_name