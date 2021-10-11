# from django.db.models import fields
from django.forms import ModelForm,widgets,Form
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Book,Author

class AuthorForm(ModelForm):
    class Meta:
        model= Author
        fields = "__all__"
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
        
    def clean_email(self): # validation cho thuộc tính của author
        input_email = self.cleaned_data['email']
        try:
            Author.objects.get(email=input_email) # Lấy report theo email
        except Author.DoesNotExist:
            return input_email
        raise ValidationError(f"{input_email} đã tồn tại. Mời bạn nhập mail khác")

class Bookform(ModelForm):
    class Meta:
        model= Book
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'pub_date':forms.DateInput(attrs={'class':'form-control','type' : 'date'}),
            'author':forms.Select(attrs={'class':'form-control'}),
        }

class RegisterForm(Form):
    first_name = forms.CharField(
        label="Tên",
        widget=forms.TextInput(
             attrs={
                'class':'form-control',
                'id':'first_name'
            }
        )
    )

    last_name = forms.CharField(
        label="Họ",
        widget=forms.TextInput(
             attrs={
                'class':'form-control',
                'id':'last_name'
            }
        )
    )

    username = forms.CharField(
        label="Tên Đăng Nhập",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'username'
            }
        )
    )

    password = forms.CharField(
        label="Mật Khẩu",
        widget=forms.PasswordInput(
             attrs={
                'class':'form-control',
                'id':'password'
            }
        )
    )

    confirm_password = forms.CharField(
        label="Nhập Lại Mật Khẩu",
        widget=forms.PasswordInput(
             attrs={
                'class':'form-control',
                'id':'confirm_password'
            }
        )
    )
  
    email = forms.EmailField(
        label="Email Đăng Ký",
        widget=forms.EmailInput(
             attrs={
                'class':'form-control',
                'id':'email'
            }
        )
    )


# Validation :username , email không được trùng có sẵn trong DB
# password và confirm_password là phải giống nhau(Kiểm tra ở phí client, javascrip)
# Ta tạo hàm
    def clean_username(self):
        inputed_username = self.cleaned_data['username']
        try:
            User.objects.get(username=inputed_username)
            raise ValidationError(f"{inputed_username} đã tồn tại")
        except User.DoesNotExist:
            return inputed_username
    def clean_email(self):
        inputed_email = self.cleaned_data['email']
        try:
            User.objects.get(email=inputed_email)
            raise ValidationError(f"{inputed_email} đã tồn tại")
        except User.DoesNotExist:
            return inputed_email
    def clean_confirm_password(self):
        inputed_password=self.cleaned_data['password']
        inputed_confirm_password= self.cleaned_data['confirm_password']
        if inputed_password != inputed_confirm_password:
            raise ValidationError(f"Mật khẩu không khớp")
        return inputed_confirm_password

    def save_user(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email = self.cleaned_data['email'],
            first_name= self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name']
        )

class LoginForm(Form):
    username = forms.CharField(
        label="Tên Đăng Nhập",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'username'
            }
        )
    )

    password = forms.CharField(
        label="Mật Khẩu",
        widget=forms.PasswordInput(
             attrs={
                'class':'form-control',
                'id':'password'
            }
        )
    )

   