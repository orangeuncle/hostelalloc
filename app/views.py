from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, FormView
from django.urls import reverse_lazy
from .forms import *
from .models import Hostel
from .models import Student


# HttResponse Handle's responses and requests
# Render returns a rendered template takes the first argument as a request. By default it searches the templates folder.


# Create your views here as functions.

# These functions handle traffic directed towards them

hostel_list = Hostel.objects.order_by('name')


# class Home(FormView):
#     hostel_list = Hostel.objects.all()[:5]
#     form_class = InputData
#     template_name = 'blog/home.html'
#     success_url = reverse_lazy('search')


def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PaymentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            rqst = request.POST
            stdDetails = {}
            for key in rqst:
                if key == 'name' or key == 'sex' or key == 'regNo' or key == 'Payment':
                    stdDetails[key] = rqst[key]

            stdUpdate = Student(name=stdDetails['name'],regNo=stdDetails['regNo'],sex=stdDetails['sex'])
            stdUpdate.save()
            return HttpResponseRedirect('/search/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaymentForm()

    return render(request, 'blog/home.html', {'form':form})

def search(request):
    form = SearchForm
    context = {
        'hostel_list': hostel_list,
        'form':form
    }
    if request.method == 'POST':
        
        form = SearchForm(request.POST)

        if form.is_valid():

            rqst = request.POST
            
            pullSearch = Student.objects.filter(regNo=rqst['regNo'])
            print("Yo yo yo")
            print(pullSearch)
            first = {'pullSearch':pullSearch}
            return HttpResponseRedirect('/about/')
        else:
            form = SearchForm()

    return render(request, 'blog/search.html', context)

def about(request):

    form = SearchForm
    context = {
        'hostel_list': hostel_list,
        'form':form
    }
    if request.method == 'POST':
        
        form = SearchForm(request.POST)

        if form.is_valid():

            rqst = request.POST

            pullSearch = Student.objects.filter(regNo=rqst['regNo'])
            print("Yo yo yo")
            print(pullSearch)
    
        else:
            form = SearchForm()
    def runsom():
        first = {'pullSearch':pullSearch}
        return first

    return render(request, 'blog/search.html', context)

    # return render(request, 'blog/about.html', {'title': 'about'})