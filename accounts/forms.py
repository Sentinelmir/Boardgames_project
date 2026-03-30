from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "nickname", "email", "profile_picture", "password1", "password2",)
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "nickname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nickname"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].help_text = "Required. Up to 150 characters."
        self.fields["nickname"].help_text = "Required. Between 2 and 30 characters."
        self.fields["email"].required = True

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Repeat password"}
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("nickname", "email", "profile_picture")
        widgets = {
            "nickname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nickname"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }

    def clean_nickname(self):
        nickname = self.cleaned_data["nickname"].strip()
        if len(nickname) < 2:
            raise forms.ValidationError("Nickname must contain at least 2 characters.")
        return nickname