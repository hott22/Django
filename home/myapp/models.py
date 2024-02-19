from django.db import models
from random import choice, randint


# Create your models here.


class ClientModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.TextField()
    date_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Клиент: id:{self.pk} имя: {self.name}, номер телефона: {self.phone_number}'


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    date_addition = models.DateField(auto_now_add=True)
    photo = models.ImageField(default=None)

    def __str__(self):
        return f'Продукт: название: {self.title}, цена: {self.price}, ' \
               f'количество: {self.quantity}'


class OrderModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductModel, related_name='comments')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    registration_date = models.DateField()

    def __str__(self):
        return f'Заказ: {self.client}, продукт: {self.product}, общая сумма заказа:' \
               f' {self.total_amount}\n'



