import random
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, EditProfileForm, QSMemoryForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from django.shortcuts import render
from .models import QS_MEMORY

def HomePage(request):
    return render(request,"index.html")
def user_login(request):
    if request.user.is_authenticated:
       return redirect('user_profile')
    else:
      if request.method == 'POST':
       username= request.POST.get('username')
       password= request.POST.get('password')

       user = authenticate(request, username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('home')
       else:
        messages.info(request,'username or Password incorrect')
          
    return render(request,"login.html")
def reg(request):
    if request.user.is_authenticated:
       return redirect('home')
    else:
      form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
         user = form.save()
         userd = form.cleaned_data.get('username')
         
         login(request,user)
         return redirect('creating_profile')
    context ={'form':form}
    return render(request,"reg.html",context)

def logoutuser(request):
   logout(request)
   return redirect('home')

#@login_required(login_url='user_login')
def services(request):
    return render(request,"services.html")

#@login_required(login_url='user_login')
def games(request):
    return render(request,"games.html")

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Create a UserProfile object for the user if it doesn't exist
        user_profile = UserProfile.objects.create(
            user=request.user,
            name=request.user.username,
            email=request.user.email,
            # Add other fields as needed
            gender='',  # You may need to adjust this based on how you handle gender
            age=0,      # You may need to adjust this based on how you handle age
           
        )
    
    context = {
        'user_profile': user_profile,
    }
    return render(request, "userProfile.html", context)

@login_required
def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Associate with the logged-in user
            user_profile.save()
            return redirect('user_profile')  # Redirect to the user's profile detail page after successful form submission
    else:
        form = UserProfileForm()
    return render(request, 'create_user_profile.html', {'form': form})


@login_required
def edit_user_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Adjust the redirect URL as needed
    else:
        form = EditProfileForm(instance=user_profile)
    return render(request, 'edit_user_profile.html', {'form': form})

login_required(login_url='user_login')
def create_question(request):
    if request.method == 'POST':
        form = QSMemoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to a success page after saving the form
    else:
        form = QSMemoryForm()
    return render(request, 'add_qs_memory.html', {'form': form})

login_required(login_url='user_login')
def display_qs_ans(request):
    questions = QS_MEMORY.objects.all()[:10]  # Assuming you want to display 5 questions initially
    return render(request, 'display_qs_ans.html', {'questions': questions})



def answer_page(request):
    # Retrieve questions from the database
    questions = QS_MEMORY.objects.all()[:10]  # Assuming you want to display 5 questions

    # Mix the order of answers for each question
    for question in questions:
        answers = [question.ans, question.w_ans, question.w2_ans]
        random.shuffle(answers)
        question.ans, question.w_ans, question.w2_ans = answers

    return render(request, 'answer_page.html', {'questions': questions})



from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, QS_MEMORY

@login_required
def calculate_score(request):
    if request.method == 'POST':
        # Retrieve user's answers from the form
        user_answers = {}
        for key, value in request.POST.items():
            if key.startswith('answer_'):
                question_id = key.split('_')[1]
                user_answers[question_id] = value

        # Calculate score
        score = 0
        for question_id, user_answer in user_answers.items():
            question = QS_MEMORY.objects.get(id=question_id)
            if user_answer == question.ans:
                score += 1

        try:
            # Update user profile with the score
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.memoeui_de_last_6 = user_profile.memoeui_de_last_5
            user_profile.memoeui_de_last_5 = user_profile.memoeui_de_last_4
            user_profile.memoeui_de_last_4 = user_profile.memoeui_de_last_3
            user_profile.memoeui_de_last_3 = user_profile.memoeui_de_last_2
            user_profile.memoeui_de_last_2 = user_profile.memoeui_de_last_1
            user_profile.memoeui_de_last_1 = score

            user_profile.memoeui_de_avareg_last_5 = (
                (user_profile.memoeui_de_last_1 + user_profile.memoeui_de_last_2 + user_profile.memoeui_de_last_3 +user_profile.memoeui_de_last_4 +user_profile.memoeui_de_last_5) / 5)
            
            user_profile.memoeui_de_previous_s_rate = user_profile.memoeui_de_present_s_rate
            
            user_profile.memoeui_de_present_s_rate = (
                (user_profile.memoeui_de_avareg_last_5/10 ) * 100)
            
            if user_profile.memoeui_de_high_score < score:
                user_profile.memoeui_de_high_score = score
            user_profile.save()
        except UserProfile.DoesNotExist:
            # Handle the case where UserProfile does not exist for the user
            return redirect('error_page')
        except Exception as e:
            # Handle other exceptions
            print(f"An error occurred: {e}")
            return redirect('error_page')

        # Redirect to the score page with the score as a parameter
        return redirect('score_page', score=score)

    # Handle invalid request method or other errors
    return redirect('error_page')  # Redirect to an error page if needed


def score_page(request, score):
    return render(request, 'score_page.html', {'score': score})

@login_required(login_url='user_login')
def display_qs_ans_all(request):
    questions = QS_MEMORY.objects.all()  # Assuming you want to display 5 questions initially
    return render(request, 'display_qs_ans_all.html', {'questions': questions})


