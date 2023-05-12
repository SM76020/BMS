from django.db import models

# Create your models here.
class Registration(models.Model):
    fullname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phonenumber = models.IntegerField()
    password = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    gender = models.CharField(max_length=8)
    class Meta:
        db_table='Registration'

class Accholder(models.Model):
    fullname=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    accno=models.CharField(max_length=15)
    number=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    pin=models.CharField(max_length=6)
    dob=models.CharField(max_length=10)
    typeac=models.CharField(max_length=10)
    accbal=models.CharField(max_length=8, null=True)

    class Meta:
        db_table="Accholders"

class Transaction(models.Model):
    account_number = models.CharField(max_length=20)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    )
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="Transactions"