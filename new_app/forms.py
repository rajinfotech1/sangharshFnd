import unicodedata
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

from django.contrib.auth import authenticate, get_user_model, password_validation
from django.utils.text import capfirst
from django.core.exceptions import ValidationError

# Create your forms here.


UserModel = get_user_model()

class emailField(forms.EmailField):
    def to_python(self, value):
        return unicodedata.normalize("NFKC", super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            "autocapitalize": "none",
            "autocomplete": "email",
        }

# new user create form
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = CustomUser
		fields = ("email", "name", "blood_group", "father_name", "mobile_nomber", "alternet_mobile_nomber", "profile", "is_member", "staff", "address", "password1", "password2")

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user
 
 
# class CustomAuthenticationForm(forms.Form):
#     """
#     Base class for authenticating users. Extend this to get a form that accepts
#     email/password logins.
#     """

#     email = forms.EmailField(widget=forms.EmailField(attrs={"autofocus": True}))
#     password = forms.CharField(
#         label=("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
#     )

#     error_messages = {
#         "invalid_login": (
#             "Please enter a correct %(email)s and password. Note that both "
#             "fields may be case-sensitive."
#         ),
#         "inactive": ("This account is inactive."),
#     }

#     def __init__(self, request=None, *args, **kwargs):
#         """
#         The 'request' parameter is set for custom auth use by subclasses.
#         The form data comes in via the standard 'data' kwarg.
#         """
#         self.request = request
#         self.user_cache = None
#         super().__init__(*args, **kwargs)

#         # Set the max length and label for the "email" field.
#         self.email_field = UserModel._meta.get_field(UserModel.email_FIELD)
#         email_max_length = self.email_field.max_length or 254
#         self.fields["email"].max_length = email_max_length
#         self.fields["email"].widget.attrs["maxlength"] = email_max_length
#         if self.fields["email"].label is None:
#             self.fields["email"].label = capfirst(self.email_field.verbose_name)

#     def clean(self):
#         email = self.cleaned_data.get("email")
#         password = self.cleaned_data.get("password")

#         if email is not None and password:
#             self.user_cache = authenticate(
#                 self.request, email=email, password=password
#             )
#             if self.user_cache is None:
#                 raise self.get_invalid_login_error()
#             else:
#                 self.confirm_login_allowed(self.user_cache)

#         return self.cleaned_data

#     def confirm_login_allowed(self, user):
#         """
#         Controls whether the given User may log in. This is a policy setting,
#         independent of end-user authentication. This default behavior is to
#         allow login by active users, and reject login by inactive users.

#         If the given user cannot log in, this method should raise a
#         ``ValidationError``.

#         If the given user may log in, this method should return None.
#         """
#         if not user.is_active:
#             raise ValidationError(
#                 self.error_messages["inactive"],
#                 code="inactive",
#             )

#     def get_user(self):
#         return self.user_cache

#     def get_invalid_login_error(self):
#         return ValidationError(
#             self.error_messages["invalid_login"],
#             code="invalid_login",
#             params={"email": self.email_field.verbose_name},
#         )

