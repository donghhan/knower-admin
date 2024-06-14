from django.contrib.auth import forms
from django.core.exceptions import ValidationError
from users.models import User


class LoginForm(forms.AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_staff:
            raise ValidationError(
                "어드민 계정만 로그인이 가능합니다", code="NOT_STAFF_ERROR"
            )
