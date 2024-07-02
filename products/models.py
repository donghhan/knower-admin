from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from common.models import TimeStampModel


class Product(TimeStampModel):
    name = models.CharField(max_length=128, unique=True, verbose_name="상품명")
    price = models.PositiveSmallIntegerField(
        verbose_name="상품가",
        validators=[MinValueValidator(10), MaxValueValidator(1000000)],
    )
    is_discount = models.BooleanField(default=False, verbose_name="할인중")
    discount_price = models.PositiveSmallIntegerField(
        verbose_name="할인가",
        null=True,
        blank=True,
        validators=[MinValueValidator(10), MaxValueValidator(1000000)],
    )
    detail = models.CharField(
        max_length=256, help_text="상품 디테일: 소재 등", verbose_name="디테일"
    )
    description = models.TextField(verbose_name="상품설명", null=True, blank=True)
    thumbnail = models.URLField(
        verbose_name="썸네일",
        default="https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("products:product_update", kwargs={"pk": self.pk})

    def clean(self):
        if self.discount_price:
            if self.discount_price >= self.price:
                raise ValidationError("할인가는 정가보다 작아야 합니다")
        super().clean()

    class Meta:
        db_table = "products"
        verbose_name = "상품"
        verbose_name_plural = "상품"


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="상품",
        related_name="product_sizes",
    )
    size = models.CharField(
        max_length=10, verbose_name="사이즈", help_text="대문자로 자동 저장"
    )

    def __str__(self):
        return self.size

    def save(self, *args, **kwargs):
        self.size = self.size.upper()
        return super(ProductSize, self).save(*args, **kwargs)

    class Meta:
        db_table = "product_sizes"
        verbose_name = "사이즈"
        verbose_name_plural = "사이즈"


class ProductColor(models.Model):
    product = models.ManyToManyField(
        Product, verbose_name="상품", related_name="products"
    )
    color = models.CharField(max_length=32, verbose_name="컬러", help_text="상품 컬러")
    hex_code = models.CharField(
        max_length=7, verbose_name="HEX코드", help_text="# 없이 6자리 코드만 기입"
    )

    def __str__(self):
        return self.color

    def save(self, *args, **kwargs):
        self.hex_code = "#" + self.hex_code.upper()
        return super(ProductColor, self).save(*args, **kwargs)

    class Meta:
        db_table = "product_colors"
        verbose_name = "컬러"
        verbose_name_plural = "컬러"


class ProductPhoto(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="상품",
        related_name="product_photos",
    )
    photo_file = models.FileField()
    photo_url = models.URLField(verbose_name="사진", null=True, blank=True)

    def __str__(self):
        return f"{self.product.name}"

    class Meta:
        db_table = "product_photos"
        verbose_name = "사진"
        verbose_name_plural = "사진"
