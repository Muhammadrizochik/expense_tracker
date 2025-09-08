from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField()
    user = models.ForeignKey(User)


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE())
    amount = models.DecimalField()
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)    