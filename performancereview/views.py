from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, PerformanceReview
#Django already has login and logout functionality
from django.contrib.auth import authenticate, login, logout
#Displays error messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from django.db.models import Q
from .forms import PerformanceReviewForm
from django.http import HttpResponseForbidden

#Kalebh 'froms'
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Employee
from django.contrib.auth.decorators import user_passes_test




#Prevents unaurhtorized access
def is_superuser(user):
    return user.is_superuser


@user_passes_test(is_superuser) #prevents regular users from accessing admin only pages
@login_required #prevents anyone from accessing the website pages
# performancereview/views.py
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            # Check if User already exists
            existing_user = User.objects.filter(username=form.cleaned_data['employeeID']).first()
            if existing_user:
                form.add_error('employeeID', 'A user with this Employee ID already exists.')
                return render(request, 'register.html', {'form': form})

            user.save()
            
            # Check if Employee already exists for the user
            if not Employee.objects.filter(user=user).exists():
                Employee.objects.create(
                    user=user,
                    employeeID=form.cleaned_data['employeeID'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    position=form.cleaned_data['position'],
                    hireDate=form.cleaned_data['hire_date'],
                    # image=form.cleaned_data['image']
                )
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})





def update_user(request):
	return render(request, 'update_user.html', {})


@user_passes_test(is_superuser)
@login_required
def performancereviewform(request):
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST)
        if form.is_valid():
            employeeID = form.cleaned_data['employeeID']
            employee = get_object_or_404(Employee, employeeID=employeeID)
            
            # Create a new performance review object using the cleaned data
            newPR = PerformanceReview(
                employeeName=form.cleaned_data['employeeName'],
                employeeID=employee,  # Assign the Employee instance
                position=form.cleaned_data['position'],
                dateOfReview=form.cleaned_data['dateOfReview'],
                timeOfReview=form.cleaned_data['timeOfReview'],
                jobKnowledge=form.cleaned_data['jobKnowledge'],
                workQuality=form.cleaned_data['workQuality'],
                initiative=form.cleaned_data['initiative'],
                communication=form.cleaned_data['communication'],
                dependability=form.cleaned_data['dependability'],
                overallFeedback=form.cleaned_data['overallFeedback'],
            )
            newPR.save()
            messages.success(request, "Successfully created Performance Review")
            # return redirect('performancereviewform')
            return redirect('performancereviewform')
        else:
            messages.error(request, "There was an error. Please try again.")
            return redirect('performancereviewform')
    else:
        form = PerformanceReviewForm()
    
    return render(request, 'performancereviewform.html', {'form': form})





@user_passes_test(is_superuser)
@login_required
def edit_performance_review(request, id):
    performance_review = get_object_or_404(PerformanceReview, id=id)

    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST, instance=performance_review)
        if form.is_valid():
            form.save()
            messages.success(request, "Performance review updated successfully")
            return redirect('performancereviewdisplay', id=performance_review.id)
        else:
            messages.error(request, "There was an error updating the performance review")
    else:
        form = PerformanceReviewForm(instance=performance_review)

    return render(request, 'edit_performance_review.html', {'form': form, 'performance_review': performance_review})




@login_required
def employee(request, employeeID):
    # Get the employee object by employeeID
    employee = get_object_or_404(Employee, employeeID=employeeID)
    
    # Check if the logged-in user is a superuser or the user associated with the employee object
    if request.user.is_superuser or employee.user == request.user:
        # Get all performance reviews for the specific employee, ordered by review date
        performancereviews = PerformanceReview.objects.filter(employeeID=employee).order_by('-dateOfReview')
        
        return render(request, 'employee.html', {
            'employee': employee,
            'performancereviews': performancereviews
        })
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")




@login_required
def performancereviewdisplay(request, id):
    performancereview = get_object_or_404(PerformanceReview, id=id)
    return render(request, 'performancereviewdisplay.html', {
        'performancereview': performancereview
    })


@login_required
def home(request):
	# employees = Employee.objects.all()
	# employees = Employee.objects.all().order_by('first_name', 'last_name')
	# return render(request, 'home.html', {'employees':employees})

    # Assuming you are fetching performance reviews in the home view
    # performancereviews = PerformanceReview.objects.all()
    # return render(request, 'home.html', {'performancereviews': performancereviews})
    
    return render(request, 'home.html', {})

# def employees1(request):
# 	employees = Employee.objects.all().order_by('first_name', 'last_name')
# 	return render(request, 'employees1.html', {'employees':employees})



@login_required
def employees1(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        ).order_by('first_name', 'last_name')
    else:
        employees = Employee.objects.all().order_by('first_name', 'last_name')
    
    if request.user.is_superuser:
        employees = Employee.objects.all()
    else:
        employees = Employee.objects.filter(user=request.user)

    return render(request, 'employees1.html', {'employees': employees, 'query': query})






@login_required
def about(request):
	return render(request, 'about.html', {})



def login_user(request):
    if request.method == "POST":
        employeeID = request.POST['employeeID']
        password = request.POST['password']
        user = authenticate(request, username=employeeID, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error. Please try again."))
            return redirect('login')
    else:
        return render(request, 'Login.html', {})



def logout_user(request):
	logout(request)
	# messages.success(request, ("Successfully logged out."))
	return redirect('login')





