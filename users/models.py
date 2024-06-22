from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from common.models import TimeStampModel


class KnowerUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password=None):
        """
        Create and saves user with the required fields stated in parameters.
        """

        if not email:
            raise ValueError("이메일을 입력해주세요")
        if not first_name:
            raise ValueError("이름을 입력해주세요")
        if not last_name:
            raise ValueError("성을 입력해주세요")
        if not phone_number:
            raise ValueError("전화번호를 입력해주세요")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, phone_number, password=None
    ):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStampModel):
    email = models.EmailField(max_length=128, verbose_name="이메일", unique=True)
    first_name = models.CharField(max_length=32, verbose_name="이름")
    last_name = models.CharField(max_length=32, verbose_name="성")
    phone_number = models.CharField(
        max_length=128,
        verbose_name="전화번호",
        help_text="휴대전화 번호를 가급적이면 선호",
    )
    is_active = models.BooleanField(verbose_name="활동여부", default=True)
    is_admin = models.BooleanField(verbose_name="어드민", default=False)

    objects = KnowerUserManager()

    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("users:user_update", kwargs={"pk": self.pk})

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = "users"
        verbose_name = "회원"
        verbose_name_plural = "회원"
