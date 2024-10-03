import uuid
from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=False,blank=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    age = models.PositiveIntegerField(blank=True)

    job_choices = [
        ('Engineer', 'Engineer'),
        ('Doctor', 'Doctor'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
        ('Other', 'Other'),
    ]
    job = models.CharField(max_length=50, choices=job_choices, blank=True)
    
    language_choices = [
        ('English', 'English'),]
    language = models.CharField(max_length=50, choices=language_choices, blank=True)
    
    education_choices = [
        ('High School', 'High School'),
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('PhD', 'PhD'),
        ('Other', 'Other'),
    ]
    education = models.CharField(max_length=50, choices=education_choices, blank=True)
    
    
    # Image field
    image = models.ImageField(upload_to='user_profile_images/', blank=True, null=True)

    condition_choices= [
        ('Worst', 'Worst'),
        ('Bad', 'Bad'),
        ('Medium', 'Medium'),
        ('Good', 'Good'),
        ('Excellent', 'Excellent'),
    ]
    condition = models.CharField(max_length=50, choices=condition_choices, blank=True)
    
    percentage = models.DecimalField(max_digits=5, decimal_places=2,blank=False,null=False, default=0.0)

    memoeui_de_score = models.IntegerField(default=0,blank=False)
    memoeui_de_high_score=models.IntegerField(default=0,blank=False)
    memoeui_de_avareg_last_5=models.IntegerField(default=0,blank=False)
    memoeui_de_previous_s_rate=models.IntegerField(default=0,blank=False)
    memoeui_de_present_s_rate=models.IntegerField(default=0,blank=False)
    memoeui_de_last_1=models.IntegerField(default=0,blank=False)
    memoeui_de_last_2=models.IntegerField(default=0,blank=False)
    memoeui_de_last_3=models.IntegerField(default=0,blank=False)
    memoeui_de_last_4=models.IntegerField(default=0,blank=False)
    memoeui_de_last_5=models.IntegerField(default=0,blank=False)
    memoeui_de_last_6=models.IntegerField(default=0,blank=False)


    BraiQui_de_score = models.IntegerField(default=0,blank=False)
    BraiQui_de_high_score=models.IntegerField(default=0,blank=False)
    BraiQui_de_avareg_last_5=models.IntegerField(default=0,blank=False)
    BraiQui_de_previous_s_rate=models.IntegerField(default=0,blank=False)
    BraiQui_de_present_s_rate=models.IntegerField(default=0,blank=False)
    BraiQui_de_last_1=models.IntegerField(default=0,blank=False)
    BraiQui_de_last_2=models.IntegerField(default=0,blank=False)
    BraiQui_de_last_3=models.IntegerField(default=0,blank=False)
    BraiQui_de_last_4=models.IntegerField(default=0,blank=False)
    BraiQui_de_last_5=models.IntegerField(default=0,blank=False)
    BraiQui_de_last_6=models.IntegerField(default=0,blank=False)

    def __str__(self):
        return self.user.username if self.user else ""  # Handling the case where user is None



class QS_MEMORY(models.Model):
    qs_id = models.CharField(max_length=36, blank=False, unique=True, default=uuid.uuid4, editable=False)
    qs = models.TextField(blank=False)
    ans = models.CharField(max_length=25, blank=False)
    w_ans = models.CharField(max_length=25, blank=False)
    w2_ans = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return f"Question ID: {self.qs_id}"

class ReactionTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    best_time = models.FloatField(null=True, blank=True)
    last_ten_games_average = models.FloatField(null=True, blank=True)
    last_game_average = models.FloatField(null=True, blank=True)
    overall_average = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


