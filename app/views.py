from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, FormView
from django.urls import reverse_lazy
from .forms import *
from .models import Hostel
from .models import Student
from .actions import totalNumberStudents


# HttResponse Handle's responses and requests
# Render returns a rendered template takes the first argument as a request. By default it searches the templates folder.


# Create your views here as functions.

# These functions handle traffic directed towards them

# hostel_list = Hostel.objects.order_by('name')
hostel_list = Hostel.objects.order_by('hostel_id')

# Creation of the allocation action function
def allocationAction(studentData,hListArray):

    hostelName = ""
    roomNumber = 0
    hList = hListArray


    for h in hList:
        baseroom_size = h.roomBaseSize
        hostelName = h.name
        if h.rooms > 0:
            if h.room_size > 0:
                roomNumber = h.rooms

                print("You are in room ", h.rooms, " in ", hostelName," hostel")
                assigned = 1
                h.room_size -= 1
                print("layer 1")

                # works when room size is 0 after allocation
                if h.room_size == 0 and h.rooms > 0 and h.rooms-1 != 0:
                    h.room_size = h.roomBaseSize
                    h.rooms -= 1
                    print("layer 2")
                elif h.room_size == 0 and h.rooms-1 == 0:
                    h.rooms = 0
                h.save()
                break
        elif h.rooms == 0 and h.room_size == 0:
            print("this guy")
        elif h.rooms == 0:
            continue
    

    # Update the hostel and room data of the student entry
    studentData['allocated'] = 1
    studentData['room'] = roomNumber
    studentData['hostel'] = hostelName


    updStd = Student(name=studentData['name'],regNo=studentData['regNo'],sex=studentData['sex'],allocated=studentData['allocated'],room=studentData['room'],hostel=studentData['hostel'])
    # Update student table by creating student data 
    updStd.save()
    print("layer 4")
    return "You are in room ", roomNumber, " of %s hostel", hostelName


# Checks if there is available rooms in the hostel
def availableRoomCalc(hostelListQuery):
    num = 0
    val = 0
    
    print(hostelListQuery[0].rooms)
    print(hostelListQuery[1].rooms)
    print(hostelListQuery[2].rooms, " \n")
    
    print(hostelListQuery[0].room_size)
    print(hostelListQuery[1].room_size)
    print(hostelListQuery[2].room_size, " \n")
    
    for i in hostelListQuery:
        val += i.rooms

    num += val
    print("num : ", num)
    return num









# ===================================     VIEWS    ===========================================


def home(request):
    
    roomcount = availableRoomCalc(hostel_list)

    hostelFull = "Sorry you can't pay for hostel. The hostel is full"
    
    # if this is a POST request we need to process the form data
    hList = Hostel.objects.all()
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
            print(rqst['Payment'].lower())
            for key in rqst:
                    if key == 'name' or key == 'sex' or key == 'regNo' or key == 'Payment':
                        stdDetails[key] = rqst[key].lower()

            # If payed full or accomodation run this
            if stdDetails['Payment'] == "full":

                # Run allocation function
                allocationAction(stdDetails,hostel_list)
            else:
                return render(request,'blog/search.html', {'noHostelPay':"You didn't pay for hostel"})


        return HttpResponseRedirect('/search/', {'noHostelPay':"You didn't pay for hostel"})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaymentForm()
        if availableRoomCalc(hostel_list) <= 0:

            return render(request, 'blog/home.html', {'form':form, 'hostelFullMessage':hostelFull}) 
        else:

            return render(request, 'blog/home.html', {'form':form, 'Space':"Available rooms",'roomcount':roomcount})

def search(request):
    link = render(request, 'blog/hostelOccupancy.html')
    form = SearchForm

    context = {
        'hostel_list': hostel_list,
        'form': form,
        'numStudentsTotal': totalNumberStudents()
    }

    if request.method == 'POST':
        
        form = SearchForm(request.POST)

        if form.is_valid():


            rqst = request.POST
            
            try:
                pullSearch = Student.objects.get(regNo=rqst['regNo'])
            except:
                context['error'] = "There's a problem with your entry, check it and try again!"
                return render(request, 'blog/search.html', context)
            
            context['pullSearchName'] = pullSearch.name
            context['pullSearchRegNo'] = pullSearch.regNo
            context['pullSearchRoom'] = pullSearch.room
            context['pullSearchHostel'] = pullSearch.hostel
            print(context)
            return render(request, 'blog/search.html', context)


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

def playground(request):
    return render(request, 'blog/playground.html')

def hostelOccupancy(request):
    link = render(request, 'blog/hostelOccupancy.html')
    form = HostelSearchForm
    context = {
        'hostel_list': hostel_list,
        'form': form,
    }

    if request.method == 'POST':
        
        form = HostelSearchForm(request.POST)

        if form.is_valid():


            rqst = request.POST
            
            try:
                pullSearch = Hostel.objects.get(name=rqst['Hostel_Name'].capitalize())
            except:
                context['error'] = "There's a problem with your entry, check it and try again!"
                return render(request, 'blog/hostelOccupancy.html', context)
            
            context['pullSearchName'] = pullSearch.name
            context['pullSearchRoomBaseSize'] = pullSearch.roomBaseSize
            context['pullSearchRooms'] = pullSearch.rooms
            print(context)
            return render(request, 'blog/hostelOccupancy.html', context)


        else:
            form = HostelSearchForm()

    return render(request, 'blog/hostelOccupancy.html', context)



# ===============================  Temp. BackUps  ===================================