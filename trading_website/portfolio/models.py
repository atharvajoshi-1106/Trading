from django.db import models

class Investment(models.Model):
    stock_name = models.CharField(max_length=100)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.stock_name} - Invested: {self.amount_invested}, P/L: {self.profit_loss}"


# Create your models here.
