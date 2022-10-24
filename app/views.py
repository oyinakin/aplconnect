import traceback
import json
from datetime import date, datetime
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import views, login, authenticate,logout
from .forms import LoginForm, ResolutionLogForm, ComplaintsForm, TaskForm, EditTaskForm, NewUserForm, MessageForm, User, ChangePasswordForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse,JsonResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Tenant, User, Complaint, Building, Task, Message, TaskComments,Reply, UserSeen, TimeLog
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder


def default(o):
    if isinstance(o, type(datetime.date)):
        return o.isoformat
def password_reset(request):
    return HttpResponseRedirect(reverse('password_reset_confirm'))

def password_reset_confirm(request):
    pass        

def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render({},request))

def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
            
        if user is None:
            form = LoginForm()
            return render(request, 'log-in.html', {'form':form, 'error_message':'Invalid email or password'})
        else:
            login(request, user)
            try:
                log = TimeLog.objects.get(Q(user=user) & Q(date_of_log=date.today()))
                print(log)
                log.most_recent_login = timezone.now()
                log.save()
            except:
                TimeLog.objects.create(
                    user=request.user
                )
            if  password=="apl@12345":
                print(password)
                cpwordform = ChangePasswordForm()
                return render(request, 'set_new_password.html', {'cpwordform':cpwordform})
            # Redirect to a success page.
            request.session['user'] = request.POST
            request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
            return HttpResponseRedirect(reverse('dashboard'))

    else:
        form = LoginForm()
        return render(request, 'log-in.html', {'form':form})
		

def contact(request):
	template = loader.get_template('contact-us.html')
	return HttpResponse(template.render({},request))


def dashboard(request):
  try:
    if request.method == 'POST':
        pass
    else: 	
        staffuserview = User.objects.exclude(user_type__gte = 3)
        users = User.objects.all()
        allusers = []
        for user in users:
            allusers.append({user.id:user.first_name + ' ' + user.last_name})
        allcomplaintsview = Complaint.objects.all()
        alltasksview = Task.objects.all()
        usertasksview = Task.objects.filter(assigned_to=request.user)
        usercomplaintsview= Complaint.objects.filter(user=request.user)
        
        allpending = Task.objects.filter(status=1)
        allinprogress  = Task.objects.filter(status=2)
        userpending = Task.objects.filter(Q(assigned_to=request.user) & Q(status=1))
        userinprogress = Task.objects.filter(Q(assigned_to=request.user) & Q(status=2))
        
        today= date.today()
        this_week = date.today().strftime('%U')
        
        all_pending_today = Task.objects.filter(Q(status=1) & Q(date_assigned__year=today.year) & 
                            Q(date_assigned__month=today.month) &
                            Q(date_assigned__day=today.day))
        all_in_progress_today  = Task.objects.filter(Q(status=2) & Q(date_in_progress__year=today.year) & 
                            Q(date_in_progress__month=today.month) &
                            Q(date_in_progress__day=today.day))
        all_completed_today = Task.objects.filter(Q(status=3) & Q(date_completed__year=today.year) & 
                            Q(date_completed__month=today.month) &
                            Q(date_completed__day=today.day))
        
        user_pending_today = Task.objects.filter(Q(assigned_to=request.user) & Q(status=1)& Q(date_assigned__year=today.year) & 
                            Q(date_assigned__month=today.month) &
                            Q(date_assigned__day=today.day))
        user_in_progress_today = Task.objects.filter(Q(assigned_to=request.user) & Q(status=2)& Q(date_in_progress__year=today.year) & 
                            Q(date_in_progress__month=today.month) &
                            Q(date_in_progress__day=today.day))
        user_completed_today = Task.objects.filter(Q(assigned_to=request.user) & Q(status=3)& Q(date_completed__year=today.year) & 
                            Q(date_completed__month=today.month) &
                            Q(date_completed__day=today.day))
        today_stats = [len(all_pending_today), len( all_in_progress_today), len(all_completed_today),
                        len(all_pending_today)+ len( all_in_progress_today)+len(all_completed_today),
                        len(user_pending_today), len( user_in_progress_today), len(user_completed_today),
                        len(user_pending_today)+ len( user_in_progress_today)+ len(user_completed_today)]
        
        all_pending_this_week = Task.objects.filter(Q(status=1) & Q(date_assigned__year=today.year) & 
                            Q(date_assigned__week=this_week))
        all_in_progress_this_week  = Task.objects.filter(Q(status=2) & Q(date_in_progress__year=today.year) & 
                            Q(date_in_progress__week=this_week))
        all_completed_this_week = Task.objects.filter(Q(status=3) & Q(date_completed__year=today.year) & 
                            Q(date_completed__week=this_week))
        
        user_pending_this_week = Task.objects.filter(Q(assigned_to=request.user) & Q(status=1)& Q(date_assigned__year=today.year) & 
                            Q(date_assigned__week=this_week))
        user_in_progress_this_week = Task.objects.filter(Q(assigned_to=request.user) & Q(status=2)& Q(date_in_progress__year=today.year) & 
                            Q(date_in_progress__week=this_week))
        user_completed_this_week = Task.objects.filter(Q(assigned_to=request.user) & Q(status=3)& Q(date_completed__year=today.year) & 
                            Q(date_completed__week=this_week))
        weekly_stats = [len(all_pending_this_week), len( all_in_progress_this_week), len(all_completed_this_week),
                        len(all_pending_this_week)+len( all_in_progress_this_week)+len(all_completed_this_week),
                        len(user_pending_this_week), len( user_in_progress_this_week), len(user_completed_this_week),
                        len(user_pending_this_week)+ len( user_in_progress_this_week)+len(user_completed_this_week)]
        
        
        all_pending_this_month = Task.objects.filter(Q(status=1) & Q(date_assigned__year=today.year) & 
                            Q(date_assigned__month=today.month))
        all_in_progress_this_month  = Task.objects.filter(Q(status=2) & Q(date_in_progress__year=today.year) & 
                            Q(date_in_progress__month=today.month))
        all_completed_this_month = Task.objects.filter(Q(status=3) & Q(date_completed__year=today.year) & 
                            Q(date_completed__month=today.month))
        
        user_pending_this_month = Task.objects.filter(Q(assigned_to=request.user) & Q(status=1)& Q(date_assigned__year=today.year) & 
                            Q(date_assigned__month=today.month))
        user_in_progress_this_month = Task.objects.filter(Q(assigned_to=request.user) & Q(status=2)& Q(date_in_progress__year=today.year) & 
                            Q(date_in_progress__month=today.month))
        user_completed_this_month = Task.objects.filter(Q(assigned_to=request.user) & Q(status=3)& Q(date_completed__year=today.year) & 
                            Q(date_completed__month=today.month))
        monthly_stats = [len(all_pending_this_month), len( all_in_progress_this_month), len(all_completed_this_month),
                        len(all_pending_this_month)+len( all_in_progress_this_month)+len(all_completed_this_month),
                        len(user_pending_this_month), len( user_in_progress_this_month), len(user_completed_this_month),
                        len(user_pending_this_month)+ len( user_in_progress_this_month)+len(user_completed_this_month)]
                        
        allmessages= Message.objects.all()
        userseen = UserSeen.objects.filter(receiver=request.user)
        user_messages = []
        for message in allmessages:
            listr = list(message.receiver)
            if message.sender==request.user:
                user_messages.append(message)    
            else:
                for i in listr:
                    if i != ',' and request.user.id == int(i):
                        user_messages.append(message)
                
        usermessages = []
        user_details = request.user.first_name + " " + request.user.last_name
            
        for message in user_messages:
            receiver_list = [User.objects.get(id=int(u)).first_name + " " + User.objects.get(id=int(u)).last_name for u in list(message.receiver) if u != ',']
            try:
                seen = UserSeen.objects.get(Q(message=message.id) & Q(receiver=request.user))
            except:    
                seen = None
            m = {'id': message.id,
            'sender': message.sender, 
            'receiver_list': receiver_list, 
            'subject': message.subject, 
            'body': message.body, 
            'seen': seen , 
            'date_created': message.date_created.strftime('%d-%m-%Y %H:%M'),
            'recent_reply_id':message.recent_reply_id
            }
            usermessages.append(m)
        unread =  [message for message in userseen if message.seen==False]
        
        allids = [msg["id"] for msg in usermessages]
        stats = [len(allpending), len(allinprogress), len(userpending), len(userinprogress) ]
        replies = Reply.objects.filter(message__in=allids)
        if replies:
            pass
        else:
            replies = None
        contractorcomplaintsview = Complaint.objects.filter(assigned_to=request.user)
        cpwordform = ChangePasswordForm()
        newuserform = NewUserForm()
        complaintsform = ComplaintsForm()
        messageform = MessageForm()
        taskform = TaskForm()
        edittaskform = EditTaskForm()
        request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        return render(request, 'dashboard.html', {'cpwordform':cpwordform,'staffuserview':staffuserview,
            'newuserform':newuserform, 'complaintsform':complaintsform, 'taskform':taskform,
            'messageform':messageform, 'allcomplaintsview':allcomplaintsview,
            'usercomplaintsview':usercomplaintsview, 'contractorcomplaintsview':contractorcomplaintsview,
            'alltasksview':alltasksview, 'usertasksview':usertasksview, 'edittaskform':edittaskform,
            'allusers':allusers, 'usermessages':usermessages, 'count_unread':len(unread), 'all_replies':replies,
            'stats':stats, 'today_stats':today_stats, 'weekly_stats':weekly_stats, 'monthly_stats':monthly_stats,
            'user_details':user_details} )
  except: 
        print(traceback.format_exc())
        return HttpResponseRedirect('signin', {'error_message': "An error occured. Contact your Administrator"})        
def signout(request):
    try:
        log = TimeLog.objects.get(Q(user=request.user) & Q(date_of_log=date.today()))
        log.last_logout = datetime.now()
        log.save()
        del request.session['user']
    except:
        print(traceback.format_exc())
        print("del issue")
        pass
    logout(request)
    return HttpResponseRedirect('signin', {'error_message': "You are signed out"})

@login_required
def save_task(request):
    data = request.POST
    task_assigned_to = User.objects.filter(id=data['task_assigned_to'])
    Task.objects.create(
      title = data["task_title"],
      description = data["task_description"],
      assigned_by = request.user,
      assigned_to = task_assigned_to[0],
      )	
    jsondata = {
        'status_message':"Task saved successfully",
    }
    request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    return JsonResponse(jsondata)

@login_required
def retrieve_task(request):
   
    data = request.POST
    task = Task.objects.filter(id=data['task_id']).values()
    comments = list(TaskComments.objects.filter(task=task[0]['id']).values())
    comments_list = []
    if comments:
        for comment in comments:
            sender = User.objects.filter(id=comment['sender_id']).values()
            if sender[0] == request.user:
                is_sender = "yes"
            else:
                is_sender = "no"    
                
            sender_name = sender[0]['first_name'] + ' ' + sender[0]['last_name']
            date = comment['date_created'].strftime('%d-%m-%Y %H:%M')
            body = comment['body']
            comments_list.append({
                'id':comment['id'],
                'sender':sender_name,
                'body':body,
                'date':date,
                'is_sender':is_sender
                })
    jsondata = {
    'task':list(task),
    'comments':comments_list
    }
    
    request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    return JsonResponse(jsondata)
    
   
def edit_task(request):
    data = request.POST
    task = Task.objects.get(id=data['task_id'])
    task.status = int(data['task_status'])
    if data['task_status'] == "2":
        task.date_in_progress = datetime.now()
    if data['task_status'] == "3":
        task.date_completed = datetime.now()
    comment = data['comment']
    if comment.strip() != "":
        TaskComments.objects.create(
            task = task,  
            sender = request.user,
            body = comment.strip()
        )
    task.save()
    jsondata = {
        'status_message':"Task updated successfully",
    }
    request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    return JsonResponse(jsondata)    
 
 
def add_message(request):
    data = request.POST
    receiver_list = data.get('receiver')
    receiver_list = receiver_list.replace(', ',',')
    split_list = receiver_list.strip().split(",")
    recipient_list = []
    for recipient in split_list:
        split_name = recipient.strip().split(" ")
        if len(split_name) > 1:
            first_name = recipient.strip().split(" ")[0]
            last_name = recipient.strip().split(" ")[1]
            to = User.objects.filter(Q(first_name=first_name) & Q(last_name=last_name))
            
            recipient_list.append(str(to[0].id))
    m = Message.objects.create(
        sender = request.user,
        receiver = ",".join(recipient_list),
        subject = data['subject'],
        body = data['body'],
        )	
    for recipient in recipient_list:
        UserSeen.objects.create(
            message = m,
            receiver = User.objects.get(id=int(recipient)),
            seen = False
            )
    jsondata = {
        'status_message':"Message sent successfully",
    }
    request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    return JsonResponse(jsondata)    
    
def retrieve_message(request):
    data = request.POST
    message = Message.objects.get(id=data['message_id'])
    if data['seen'] == "1":
        try:
            us = UserSeen.objects.get(Q(message=data['message_id']) & Q(receiver=request.user))
            us.seen = True
            us.save()
        except:    
            pass
        
    message = Message.objects.filter(id=data['message_id']).values()
    replies = Reply.objects.filter(message=message[0]['id'])
    sender = User.objects.filter(id=message[0]['sender_id']).values()
    sender_name = sender[0]['first_name'] + ' ' + sender[0]['last_name']
    if replies:
        replies_list = []
        for reply in list(replies.values()):
            reply_sender = User.objects.filter(id=reply['sender_id']).values()
            if reply_sender[0] == request.user:
                is_sender = "yes"
            else:
                is_sender = "no"    
                
            reply_sender_name = reply_sender[0]['first_name'] + ' ' + reply_sender[0]['last_name']
            date = reply['date_created'].strftime('%d-%m-%Y %H:%M')
            body = reply['body']
            replies_list.append({
                'id':reply['id'],
                'sender':reply_sender_name,
                'body':body,
                'date':date,
                'is_sender':is_sender
                })
        jsondata = {
            'message':message[0],
            'sender':sender_name,
            'replies':replies_list
        }
    else:
        jsondata = {
            'message':message[0],
            'sender':sender_name,
            
        }
    request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    return JsonResponse(jsondata)
    
    
    
def update_message(request):
    data = request.POST
    message = Message.objects.get(id=data['id'])
    reply = Reply.objects.create(
        message=message,
        sender=request.user,
        body=data["body"]  
    )
    
    if request.user != message.sender:
        try:
            initial_sender = UserSeen.objects.get(Q(message=message.id) & Q(receiver=message.sender))
        except:
            UserSeen.objects.create(
                message = message,
                receiver = message.sender,
                seen = False
                )
    
    us = UserSeen.objects.filter(message=message.id)
    for k in us:
        k.seen = False
        k.save()
    message.recent_reply_id = reply.pk
    message.seen = False
    message.save()
    jsondata = {
            'status':"Message Sent",
    }
    request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    return JsonResponse(jsondata)   
    
    
def check_session_validity(request):
    if request.method=='GET':
        ls = request.session['last_activity']
        print(ls)
        ls = ls.replace('"','')
        last_activity = datetime.strptime(ls, '%Y-%m-%dT%H:%M:%S.%f')
        now = datetime.strptime(datetime.now().strftime('%d/%m/%y %H:%M'),'%d/%m/%y %H:%M')
        print("last_activity is ")
        print(last_activity)
        if int(str(now-last_activity).split(":",2)[1]) > 1:
            # Do logout / expire session
            # and then...
            try:
                del request.session['user']
            except KeyError:
                print("del issue")
                pass
            logout(request)
            return HttpResponseRedirect('signin', {'error_message': "You are signed out"})
    request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    print("done dat")
    return JsonResponse({"status":"OK"}) 
    
    
def change_password(request):
    data=request.POST
    if(data['new_password']==data['confirm_new_password']):
        user = authenticate(request, username=request.user.username, password = data['old_password'])
        if user == request.user:
            u = User.objects.get(id=request.user.id)
            u.set_password(data['new_password'])
            u.save()
            return JsonResponse({"status":"Password Changed Sucecssfully"})
        else:    
            return JsonResponse({"status":"You entered a wrong old password"})
          
    return  JsonResponse({"status":"New password and confirm new password do not match"})
    
    