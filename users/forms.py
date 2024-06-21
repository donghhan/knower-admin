from django import forms
from django.contrib.auth import forms as auth_form
from django.core.exceptions import ValidationError
from users.models import User


class LoginForm(auth_form.AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_staff:
            raise ValidationError(
                "어드민 계정만 로그인이 가능합니다", code="NOT_STAFF_ERROR"
            )


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "is_active",
            "is_staff",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "이름"}),
            "last_name": forms.TextInput(attrs={"placeholder": "성"}),
            "email": forms.EmailInput(
                attrs={"placeholder": "이메일", "disabled": "true", "id": "user_email"}
            ),
            "phone_number": forms.TextInput(attrs={"placeholder": "전화번호"}),
        }
