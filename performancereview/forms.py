from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import PerformanceReview, Employee


class RegistrationForm(UserCreationForm):
    employeeID = forms.CharField(label="Employee ID", max_length=25)
    first_name = forms.CharField(label="Employee First Name", max_length=50)
    last_name = forms.CharField(label="Employee Last Name", max_length=50)
    email = forms.EmailField(label="Employee Work Email", max_length=100)
    position_choices = [
        ('Sales', 'Sales'),
        ('Foreman', 'Foreman'),
        ('Accounting', 'Accounting'),
        ('Warehouse', 'Warehouse'),
        ('Reception', 'Reception'),
        ('BranchManager', 'BranchManager'),
        ('HR', 'HR'),
        ('CEO', 'CEO'),
    ]
    position = forms.ChoiceField(choices=position_choices)
    hire_date = forms.DateField(label="Hire Date", widget=forms.DateInput(attrs={'type': 'date'}))
    # image = forms.ImageField(label="Employee Image", required=False)

    class Meta:
        model = User
        fields = ('employeeID', 'first_name', 'last_name', 'email', 'position', 'hire_date', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['employeeID']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        position = self.cleaned_data['position']
        if position in ['BranchManager', 'HR', 'CEO']:
            user.is_staff = True
            user.is_superuser = True

        if commit:
            user.save()

            # Check if an Employee already exists for this User
            if not Employee.objects.filter(user=user).exists():
                Employee.objects.create(
                    user=user,
                    employeeID=self.cleaned_data['employeeID'],
                    first_name=self.cleaned_data['first_name'],
                    last_name=self.cleaned_data['last_name'],
                    email=self.cleaned_data['email'],
                    position=self.cleaned_data['position'],
                    hireDate=self.cleaned_data['hire_date'],
                    # image=self.cleaned_data['image']
                )
        return user





class PerformanceReviewForm(forms.ModelForm):
    dateOfReview = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    timeOfReview = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))
    
    class Meta:
        model = PerformanceReview
        fields = [
            'employeeName', 
            'employeeID', 
            'position', 
            'dateOfReview', 
            'timeOfReview',
            'jobKnowledge', 
            'workQuality', 
            'initiative', 
            'communication', 
            'dependability', 
            'overallFeedback'
        ]
        widgets = {
            'employeeName': forms.TextInput(attrs={'class': 'form-control'}),
            'employeeID': forms.Select(attrs={'class': 'form-control'}),  # This is a dropdown select box
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'jobKnowledge': forms.Select(attrs={'class': 'form-control'}),
            'workQuality': forms.Select(attrs={'class': 'form-control'}),
            'initiative': forms.Select(attrs={'class': 'form-control'}),
            'communication': forms.Select(attrs={'class': 'form-control'}),
            'dependability': forms.Select(attrs={'class': 'form-control'}),
            'overallFeedback': forms.Textarea(attrs={'class': 'form-control'}),
        }



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

