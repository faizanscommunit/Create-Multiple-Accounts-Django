def signup_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        account_type = request.POST.get('acc_type')
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            # Through an ERROR, "User already exists!"
            pass
        else:
            # Create a new user 
            if account_type == "admin":
                new_user = User.objects.create_superuser(first_name=first_name, last_name=last_name, username=username, password=password)
                new_user.save()
                messages.success(request, 'Admin Account created successfully!')
            elif account_type == 'staff':
                new_user = User.objects.create(first_name=first_name, last_name=last_name, username=username, password=password, is_staff=True)
                new_user.save()
                messages.success(request, 'Staff Account created successfully!')
            else:
                new_user = User.objects.create(first_name=first_name, last_name=last_name, username=username, password=password)
                new_user.save()
                messages.success(request, 'Employee Account created successfully!')
            return redirect('home')


    return render(request, 'signup.html')
