from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms 
from .models import QS_MEMORY, UserProfile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','gender', 'age', 'job', 'language', 'education', 'image']
        exclude = ['percentage']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','gender', 'age', 'job', 'language', 'education', 'image']

class QSMemoryForm(forms.ModelForm):
    class Meta:
        model = QS_MEMORY
        fields = ['qs', 'ans','w_ans','w2_ans']
        labels = {
            'qs': 'Question',
            'ans': 'Answer',
            'w_ans':'wrong1',
            'w_ans':'wrong2',
        }

