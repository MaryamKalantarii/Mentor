from django.shortcuts import render,redirect
from .models import Services,NewsLetter
from courses.models import Course,Trainer
from courses.models import Category
from accounts.models import CustomeUser
from .forms import NewsLetterForm,ContactUsForm
from django.contrib import messages

# Create your views here.



def home (request):
    if request.method == 'GET':
        service_count = Services.objects.filter(status = True).count()
        course_count = Course.objects.filter(status = True).count()
        trainer_count = Trainer.objects.filter(status = True).count()
        
        category = Category.objects.all()

        services = Services.objects.filter(status=True)
        last_three_course = Course.objects.filter(status=True)[:3]
        last_three_trainer = Trainer.objects.filter(status=True)[:3]
        context = {
            'service':services,
            'course':last_three_course,
            'trainer':last_three_trainer,
            'category':category,
            'sc':service_count,
            'cc':course_count,
            'tc':trainer_count,
        }
        return render(request,"root/index.html" , context=context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('root:home')
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:home')


def about (request):
    if request.method == 'GET':
        category = Category.objects.all()
        context = {
            'category':category,
        }
        return render(request,"root/about.html", context=context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('root:about')
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:about')


def contact(request):
    if request.method =='GET':
        category = Category.objects.all()
        context = {
            'category':category,
        }
        return render(request,"root/contact.html",context=context)
    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:contact')
        
    elif request.method == 'POST' and len(request.POST) > 2 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you as soon')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')

def trainer(request):
    if request.method == 'GET':
        category = Category.objects.all()
        
        last_three_trainer = Trainer.objects.filter(status=True)[:3]
        context = {
            
            
           
            'trainer':last_three_trainer,
            'category':category,
            
            
           
            
        }
        return render(request,"root/trainers.html", context=context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('root:trainer')
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:trainer')


def course_detail(request,id):
    if request.method == 'GET':
        try:
            course = Course.objects.get(id=id)
            id_list = []
            courses = Course.objects.filter(status=True)
            for cr in courses:
                id_list.append(cr.id)

            id_list.reverse()
            
            if id_list[0] == id :
                next_course = Course.objects.get(id = id_list[1])
                previous_course = None

            elif id_list[-1] == id :
                next_course = None
                previous_course = Course.objects.get(id = id_list[-2])

            else:
                next_course = Course.objects.get(id=id_list[id_list.index(id)+1])
                previous_course = Course.objects.get(id=id_list[id_list.index(id)-1])




            course.counted_views +=1
            course.save()
        
            context ={"course": course,
                    'next_course': next_course,
                    'previous_course': previous_course,
            }
            return render(request,'course/course-details.html',context=context)
        except:
            return render(request,'course/404.html')
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('root:course_detail')
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:course_detail')
