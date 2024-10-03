from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Groceries', 'Groceries'),
        ('Leisure', 'Leisure'),
        ('Electronics', 'Electronics'),
        ('Utilities', 'Utilities'),
        ('Clothing', 'Clothing'),
        ('Health', 'Health'),
        ('Others', 'Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Monto del gasto
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Categoría del gasto
    description = models.TextField(blank=True)  # Descripción opcional del gasto
    date = models.DateField()  # Fecha del gasto

    def __str__(self):
        return f"{self.user.username} - {self.category}: {self.amount}"