from django.shortcuts import render,redirect
from . forms import UserSignUpForm

# Create your views here.
def signUp(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    form = UserSignUpForm()
    return render(request, 'registration/sign-up.html', {'form':form})

