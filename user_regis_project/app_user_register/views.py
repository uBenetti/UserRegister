from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'users/home.html')
    
def users(request):
    # saving data in DB 
    new_user=User()
    new_user.name = request.POST.get('name')
    new_user.age = request.POST.get('age')
    new_user.save()
    # Showing all user already register in a new page
    users = {
        'users': User.Object.all()
    }

    

    # Return data to the Users List page
    return render(request, 'users/users.html', usuarios)