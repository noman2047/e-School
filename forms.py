from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import CharField
from app_users.models import UserProfileInfo

class UserForm(UserCreationForm):
    username = forms.CharField(label="ইউজারের নাম লিখো", required=True)
    first_name = forms.CharField(label="তোমার নাম লিখো",required=True)
    email = forms.EmailField(label="তোমার ইমেইল ঠিকানা লিখো",required=True)
    password1 = forms.CharField(label="পাসওয়ার্ড দাও",widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="পাসওয়ার্ডটি পুনরায় দাও",widget=forms.PasswordInput,required=True)
    

    class Meta():
        model = User
        fields = ('username','first_name','email', 'password1', 'password2')

        # widgets = {
        # "password":"forms.PasswordInput()",
        # }

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(label="জীবন বৃত্তান্ত লিখো", required=True)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (student, 'ছাত্রছাত্রী'),
        (parent, 'পিতা-মাতা'),
        (teacher,'শিক্ষক/শিক্ষিকা'),
    ]
    user_type = forms.ChoiceField(label="ব্যবহারকারীর ধরণ", required=True, choices=user_types)
    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'profile_pic', 'user_type')
