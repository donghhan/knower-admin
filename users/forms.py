from django import forms
from users.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "E-mail"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            existing_user = User.objects.get(email=email)
            if existing_user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("비밀번호가 일치하지 않습니다")
                )
        except User.DoesNotExist:
            self.add_error(
                "email", forms.ValidationError("해당 이메일을 가진 유저가 없습니다")
            )
