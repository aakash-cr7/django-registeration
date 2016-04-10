from django import forms
from django.contrib.auth import authenticate
from material import Layout, Row, Span6
from .models import CustomUser

'''
    Login form
'''
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': ''}))

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username = username, password = password)
            if self.user_cache is None:
                raise forms.ValidationError('Invalid username or password')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('User is not Active')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

'''
    Sign up form. Check if both password entered are same, set is_active = False on succesfull signup
'''
class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput, help_text = 'Should be same as Password')
    '''
        django-material stuff. To organise the various signup fields
    '''
    layout = Layout(
        Row(Span6('first_name'), Span6('last_name')),
        Row('username'),
        Row(Span6('email'), Span6('mobile_number')),
        Row(Span6('password1'), Span6('password2')),
    )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def clean_password2(self):
        data_password1 = self.cleaned_data.get('password1')
        data_password2 = self.cleaned_data.get('password2')

        if data_password1 and data_password2 and data_password1 != data_password2:
            raise forms.ValidationError('Passwords don\'t match')
        if len(data_password2) < 6:
            raise forms.ValidationError('Password is too short (minimum is 6 characters) ')

        return data_password2

    def save(self, commit = True):
        user = super(SignupForm, self).save(commit = False)
        user.set_password(self.cleaned_data.get('password1'))
        user.is_active = False
        if commit == True:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile_number']

'''
    Forgot password form. Check if the email entered is valid and in the database
'''
class ForgotPasswordForm(forms.Form):
   email = forms.EmailField(max_length = 254)

   def clean_email(self):
       data_email = self.cleaned_data.get('email')
       if data_email and CustomUser.objects.filter(email = data_email).count() == 0:
           raise forms.ValidationError('Can\'t find that email, sorry')
       return data_email

'''
    Reset password form
'''
class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput, help_text = 'Should be same as Password')

    def clean_password2(self):
        data_password1 = self.cleaned_data['password1']
        data_password2 = self.cleaned_data['password2']

        if data_password1 and data_password2 and data_password1 != data_password2:
            raise forms.ValidationError('Passwords don\'t match')
        if len(data_password2) < 6: # Password should be of min length 6 
            raise forms.ValidationError('Password is too short (minimum is 6 characters) ')
        return data_password2

