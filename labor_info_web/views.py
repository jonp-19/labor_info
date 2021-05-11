from django.shortcuts import render, redirect

from .models import BlogPost, ContactRequest
from .forms import BlogForm, ContactRequestForm
from django.http import Http404, HttpResponse 
from django.core.mail import send_mail, BadHeaderError

# Helper function
def send_data(request):
    form = ContactRequestForm(request.POST)
    if form.is_valid():
        subject = "Website Inquiry" 
        body = {
        'first_name': form.cleaned_data['first_name'], 
        'last_name': form.cleaned_data['last_name'],
        'last_4_SSN': form.cleaned_data['last_4_SSN'], 
        'email': form.cleaned_data['email'],
        'phone': form.cleaned_data['phone'], 
        'comment':form.cleaned_data['comment'], 
        }
        message = "\n".join(body.values())

        try:
            send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

def index(request):
    """The home page for labor_info_web."""
    return render(request, 'labor_info_web/index.html')

def news(request):
    """Page for news updates"""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'labor_info_web/news.html', context)

def contact_request(request):
    """Page for completing labor info contact request."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ContactRequestForm()
    else:
        # POST data submitted; process data.
        form = ContactRequestForm(data=request.POST)
        if form.is_valid():
            form.save()
            send_data(request)
            return redirect('/submitted')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'labor_info_web/contact_request.html', context)

def submitted(request):
    """View for submission confirmation"""
    return render(request, 'labor_info_web/submitted.html')

def unemployment(request):
    """View for unemployment assistance page"""
    return render(request, 'labor_info_web/unemployment.html')

def wages(request):
    """View for wage info"""
    return render(request, 'labor_info_web/wages.html')

def workplace(request):
    """View for workplace issues"""
    return render(request, 'labor_info_web/workplace.html')

def other(request):
    """View for workplace issues"""
    return render(request, 'labor_info_web/other_resources.html')

def training(request):
    """View for workplace issues"""
    return render(request, 'labor_info_web/training.html')
