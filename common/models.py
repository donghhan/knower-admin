from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트 날짜")

    class Meta:
        abstract = True
