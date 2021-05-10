from django.shortcuts import render, redirect, get_object_or_404

from .models import BlogPost, ContactRequest
from .forms import BlogForm, ContactRequestForm
from django.http import Http404


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
