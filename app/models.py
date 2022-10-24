from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, IntegerField , F, ExpressionWrapper
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
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


class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'Tenant'),
      (2, 'Contractor'),
      (3, 'Data Officer'),
      (4, 'Admin'),
      (5, 'Manager'),
  )
  phone_number =  PhoneNumberField(blank=True)
  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
  def __str__(self):
     return self.first_name + " " + self.last_name
  
class Building(models.Model):
	name= models.CharField(max_length = 300)
	def __str__(self):
		return self.name

class Tenant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'user_type': 1},)
    building =  models.ForeignKey(Building, on_delete=models.CASCADE)

    
class ComplaintManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().annotate(report_id=ExpressionWrapper(10000 + F('id'),output_field=IntegerField()))
        return qs

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'user_type': 1}, related_name = "user")
    building =  models.ForeignKey(Building, on_delete=models.CASCADE)
    date_reported = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS, default = 1)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'user_type': 2}, blank =True, null =True, related_name = "assigned_to")
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, blank =True, null =True, related_name = "assigned_by")
    objects = models.Manager()	
    report_id_objects = ComplaintManager()
    def __str__(self):
      return self.id
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.TextField()
    subject = models.CharField(max_length=450)
    body = models.TextField()
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    recent_reply_id = models.IntegerField(default=0)
    last_modified  = models.DateTimeField(auto_now=True)  
    class Meta:
        ordering = ("-last_modified",)

class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    def photo_dir(self):
        return str(self.complaint)
    
    complaint = models.ForeignKey(
        Complaint, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to=f'complaints/photos/{photo_dir}', null=False, blank=False)

class Video(models.Model):
    def video_dir(self):
        return str(self.complaint)
    slug = models.SlugField(unique=True)
    complaint = models.ForeignKey(
        Complaint, on_delete=models.CASCADE, null=False, blank=False)
    videofile= models.FileField(upload_to=f'complaints/videos/{video_dir}')
        
class ResolutionLog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	date_of_action  = models.DateTimeField()
	time_of_action  = models.TimeField()
	date_logged = models.DateTimeField(auto_now_add=True)
	status = models.PositiveSmallIntegerField(choices=STATUS, default = 1)
        
      
class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.PositiveSmallIntegerField(choices=TASK_STATUS, default=1)
    assigned_to = models.ForeignKey(User, related_name="task_assigned_to",on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, related_name="task_assigned_by", on_delete=models.CASCADE)
    date_assigned = models.DateTimeField(auto_now_add=True)
    date_in_progress = models.DateTimeField(blank=True, null=True )
    date_completed = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.id 
    class Meta:
        ordering = ("-date_assigned",)   
      
class Reply(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)   
    sender = models.ForeignKey(User, related_name="reply_sender", on_delete=models.CASCADE)
    #receiver = models.ForeignKey(User, related_name="reply_receiver", on_delete=models.CASCADE)
    body = models.TextField()
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_created",)   

class UserSeen(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)   
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("date_created",)   
        
class TaskComments(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)   
    sender = models.ForeignKey(User, related_name="task_comment_sender", on_delete=models.CASCADE)
    body = models.TextField()
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_created",)  
        
class TimeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_log = models.DateField(auto_now_add=True)
    first_login  = models.DateTimeField(auto_now_add=True)
    last_logout = models.DateTimeField(null=True,blank=True)
    most_recent_login = models.DateTimeField(null=True,blank=True)
    class Meta:
        ordering = ("-date_of_log",)  
        