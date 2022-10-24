from django import forms
from django.forms import ModelForm,HiddenInput, TextInput, DateInput, NumberInput, Select

from functools import partial
from datetime import datetime
from django.contrib.auth.models import User

from .models import Building, User
from django.core.validators import validate_email


STATUS = (
      (1, 'Pending'),
      (2, 'Escalated'),
      (3, 'Resolved'),
      (4, 'Closed'),)

TASK_STATUS = (
      (1, 'Pending'),
      (2, 'In Progress'),
      (3, 'Completed'),
      (4, 'Closed'),)

class LoginForm(forms.Form):
	email = forms.EmailField(widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'Email'}))
	password  = forms.CharField(widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'password','placeholder':'Password'}))

class NewUserForm(forms.Form):
	USER_TYPES_ALLOWED = ((1, 'Tenant'), (2, 'Contractor'),)
	first_name = forms.CharField(label='First Name', widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'First Name'}))
	last_name = forms.CharField(label='Last Name',widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'Last Name'}))
	email = forms.EmailField(label='Email',widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'e.g abc@example.com'}))
	phone  = forms.CharField(widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'07012345678'}))
	user_type = forms.ChoiceField(label="User Category", widget=forms.Select(attrs={'class': 'form-control p-2', 'onchange':'hideBuilding()'}), choices = USER_TYPES_ALLOWED)
	building = forms.ModelChoiceField(queryset =Building.objects.all(), empty_label='--Select--', widget=forms.Select(attrs={'class': 'form-control p-2'}),label='Building',)
	

class ComplaintsForm(forms.Form):
	title = forms.CharField(label='Title', widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'Title'}))
	description = forms.CharField(label='Description',widget = forms.Textarea(attrs = {'class':'form-control p-2', 'cols':40,'rows':6,'placeholder':'Short Explanation of issue'}))
	reportedby = forms.ModelChoiceField(queryset =User.objects.all().exclude(is_staff=True), empty_label='--Select--', widget=forms.Select(attrs={'class': 'form-control p-2'}))

class ResolutionLogForm(forms.Form):
	title = forms.CharField(label='Title', widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':''}))
	description = forms.CharField(label='Description',widget = forms.Textarea(attrs = {'class':'form-control p-2', 'cols':40,'rows':6,'placeholder':'Short Explanation of issue'}))
	date_of_action = forms.DateField(label='Date Action Taken', widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'dd/mm/yyyy'}))
	time_of_action = forms.TimeField(label='Time of Action', widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'dd/mm/yyyy'}))
	status = forms.ChoiceField(label='Status', widget=forms.Select(attrs={'class': 'form-control'}), choices = STATUS)

class TaskForm(forms.Form):
    task_title = forms.CharField(label='Title', widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'Title'}))
    task_description = forms.CharField(label='Description',widget = forms.Textarea(attrs = {'class':'form-control p-2', 'cols':40,'rows':3,'placeholder':'Short Explanation of issue'}))
    task_assigned_to = forms.ModelChoiceField(queryset =User.objects.all().exclude(user_type__lte = 2 ), empty_label='--Assign Task To--', widget=forms.Select(attrs={'class': 'form-control p-2'}))


class EditTaskForm(forms.Form):
    task_title = forms.CharField(label='Title', widget = forms.TextInput(attrs = {'class':'form-control p-2', 'type':'text','placeholder':'Title'}))
    task_description = forms.CharField(label='Description',widget = forms.Textarea(attrs = {'class':'form-control p-2', 'cols':40,'rows':3,'placeholder':'Short Explanation of issue'}))
    status = forms.ChoiceField(label='Status', widget=forms.Select(attrs={'class': 'form-control'}), choices = TASK_STATUS)

class MessageForm(forms.Form):
    receiver = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control p-2','type':'text','placeholder':'Enter Recipient(s)'}))
    subject = forms.CharField(label='subject', widget=forms.TextInput(attrs={'class': 'form-control p-2','type':'text','placeholder':'Subject'}))
    body= forms.CharField(label='body', widget=forms.Textarea(attrs={'class': 'form-control','cols':40,'rows':6, 'placeholder':'Type your message'}))

    
class ChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(label='Old Password', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','type':'password','placeholder':'Old Password'}))
    newpassword = forms.CharField(label='New Password', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','type':'password','placeholder':'New Password'}))
    confirmnewpassword = forms.CharField(label='Confirm New Password', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','type':'password','placeholder':'Confirm New Password'}))
	