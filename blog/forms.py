from django import forms
from django.contrib.auth import authenticate
from .models import User, Resource


# ----------------------
# Register Form
# ----------------------
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ["name", "email"]

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")

        if p1 and p2 and p1 != p2:
            self.add_error("password2", "Passwords do not match.")

        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


# ----------------------
# Login Form
# ----------------------
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )

    def clean(self):
        cleaned = super().clean()
        email = cleaned.get("email")
        password = cleaned.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise forms.ValidationError("Invalid email or password.")

        cleaned["user"] = user
        return cleaned


# ----------------------
# Resource Upload Form
# ----------------------
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ["title", "description", "subject", "year_group", "file"]
