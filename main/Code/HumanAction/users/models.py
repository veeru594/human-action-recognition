from django.db import models

# Create your models here.
class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'UserRegistrations'

class UserActionsModel(models.Model):
    name = models.CharField(max_length=100)
    login_user = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    actions = models.CharField(max_length=100)
    c_date = models.DateTimeField()
    def __str__(self):
        return self.login_user
    class Meta:
        db_table = 'UserActions'

