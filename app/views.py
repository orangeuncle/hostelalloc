from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, FormView
from django.urls import reverse_lazy
from .forms import PaymentForm
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
            return HttpResponseRedirect('/search/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaymentForm()

    return render(request, 'blog/home.html', {'form': form})



# def home(request):
#     context = {
#         'posts': posts
#     }
#     form_class = InputData
#     template_name = 'blog/home.html'
#     return render(request, 'blog/home.html', context)
    # success_url = reverse_lazy(app)


    # return render(request, 'blog/home.html', context)
    # form = InputData(request.POST)
    # if form.is_valid():
    #     print('lolololo')
    #     return redirect('search')
    # return render(request, 'blog/home.html', { 'form' : form})
    # 
    #  
    # def get(self, request, *args, **kwargs):
    #     return render(request, 'blog/home.html', context)   # context is an argument that passes data in context dict into page

    # def post(self, request, *args, **kwargs):
    #     form = InputData(request.POST)
    #     if form.is_valid():
    #         print('lolololo')
    #         return redirect('search')
    #     return render(request, 'blog/home.html', { 'form' : form}) 
        


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})

def search(request):
    context = {
        'hostel_list': hostel_list
    }
    return render(request, 'blog/search.html', context)