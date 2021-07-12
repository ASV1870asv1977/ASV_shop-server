from django.db import models

from users.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        '''Метод вычисления суммы стоимости одного товара'''
        return self.quantity * self.product.price

    def total_quantity(self):
        '''Метод вычисления общего количества товаров в корзине'''
        basket_user = Basket.objects.filter(user=self.user)
        count = 0
        for unit in basket_user:
            count += unit.quantity
        return count

    def total_sum(self):
        '''Метод вычисления общей стоимости всех товаров в корзине'''
        basket_user = Basket.objects.filter(user=self.user)
        sum = 0
        for unit in basket_user:
            sum += unit.sum()
        return sum
