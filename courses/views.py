from typing import Any
from django.db import models
from django.shortcuts import render , get_object_or_404, redirect
from .models import Course, Comment, Category, Reply
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import CommentForm, ReplyForm
from django.contrib import messages
from root.models import NewsLetter
from root.forms import NewsLetterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .cart import Cart




class DeleteCommentView(LoginRequiredMixin,DeleteView):
    model = Comment
    template_name = 'course/comment_confirm_delete.html'
    success_url = '/courses/'
 



class CommentEditView(LoginRequiredMixin,UpdateView):
    template_name = 'course/edit.html'
    model = Comment
    fields = ['which_course', 'name', 'email', 'subject', 'message']
    success_url = '/courses/'
    context_object_name = 'comment'

        
class ReplyView(LoginRequiredMixin,DetailView):
    template_name = 'course/reply.html'
    model = Comment
    context_object_name = 'comment'

    def post(self, request, *args, **kwargs):
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path_info)



class CourseListView(ListView):
    
    template_name = 'course/courses.html'
    context_object_name = 'courses'
    paginate_by = 2

    def get_queryset(self):
        if self.kwargs.get('cat'):
            return Course.objects.filter(category__name=self.kwargs.get('cat'))
        elif self.kwargs.get('teacher'):
            return Course.objects.filter(teacher__info__email = self.kwargs.get('teacher'))
        elif self.request.GET.get('search'):
            return Course.objects.filter(content__contains = self.request.GET.get('search'))
        else:
            return Course.objects.filter(status=True) 
    def post(self, request, *args, **kwargs):
        post_detail = CourseDetailView()
        return post_detail.post(request,*args,**kwargs)
    

    
class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course-details.html'
    context_object_name = 'course'

    
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        
        if 'id' in request.POST :
            product = get_object_or_404(Course, id=request.POST['id'])    
            cart.delete_from_cart(product)
            
        else:
            product = get_object_or_404(Course, id=request.POST['pk'])
        quantity = request.POST.get('quantity', 1)
        cart.add_to_cart_some_quantity(product,quantity)
        return redirect(request.path_info)

    
class PaymentView(TemplateView):
    template_name = 'course/cart.html'

    