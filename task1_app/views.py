from django.shortcuts import render,redirect
from.models import User
from django.contrib import messages

# Create your views here.
def intro(request):
    return render(request,'intro.html')
def signup(request):
    return render(request,'signup.html')
def log(request):
    return render(request,'login.html')

def reg(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        type = request.POST.get('type')
        password = request.POST.get('password')
        retype_password = request.POST.get('retype_password')
        address_line1 = request.POST.get('address_line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        profile = request.FILES.get('profile')
        print(username)
        print(email)

        
        if password != retype_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')
         
        user = User(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=email,
            type=type,
            password=password,  
            address_line1=address_line1,
            city=city,
            state=state,
            pincode=pincode,
            profile=profile
        )
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('log') 

    return render(request, 'signup.html')

def dash(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email not registered.")
            return redirect('login')

    
        if user.password != password:  
            messages.error(request, "Incorrect password.")
            return redirect('login')
        return render(request, 'dashboard.html', {'user': user})

    return render(request, 'login.html')
       



