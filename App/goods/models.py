from typing import Literal
from django.db import models
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.CharField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="url"
    )

    class Meta:
        db_table: str = "category"
        verbose_name: str = "Категорию"
        verbose_name_plural: str = "Категории"

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.CharField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="url"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name: str = "Продукт"
        verbose_name_plural: str = "Продукты"
        ordering: tuple[Literal["id"]] = ("id",)

    def __str__(self) -> str:
        return f"{self.name} Количество - {self.quantity}"

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self) -> str:
        return f"{self.id:05}"

    def sell_price(self) -> str:
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price
