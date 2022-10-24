from django.contrib import admin
from django.contrib.auth.admin  import  UserAdmin
from .models import User, Complaint, Tenant, Building,ResolutionLog, Reply, Message, Task, TaskComments, UserSeen,TimeLog



# Show custom fields in Admin Panel
fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')})
fields[2] = ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'user_type')})
UserAdmin.fieldsets = tuple(fields) 

# Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(Complaint)
admin.site.register(Tenant)
admin.site.register(Building)
admin.site.register(ResolutionLog)
admin.site.register(Reply)
admin.site.register(Message)
admin.site.register(Task)
admin.site.register(TaskComments)
admin.site.register(UserSeen)
admin.site.register(TimeLog)	