from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import TimeStampModel


class User(AbstractUser, TimeStampModel):
    username = None
    phone_number = models.CharField(
        max_length=128,
        verbose_name="전화번호",
        help_text="휴대전화 번호를 가급적이면 선호",
    )
    email = models.EmailField(unique=True, verbose_name="E-mail")

    REQUIRED_FIELDS = ["phone_number"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.get_full_name()

    class Meta:
        db_table = "users"
        verbose_name = "회원"
        verbose_name_plural = "회원"
