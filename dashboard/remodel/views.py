from django.shortcuts import render,get_list_or_404
from .models import Vhigh,Med,High
# Create your views here.

from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/index.html')

def index1(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/charts-chartjs.html')
def index2(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-accordions.html')
def index3(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-calendar.html')
def index4(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-carousel.html')
#def index5(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
 #   return render(request, 'remodel/components-carousel.html')

def index6(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-modals.html')
def index7(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-notifications.html')
def index8(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-pagination.html')
def index9(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-progress-bar.html')
def index10(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-scrollable-elements.html')

def index11(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-tabs.html')
def index12(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/components-tooltips-popovers.html')
def index13(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/dashboard-boxes.html')
def index14(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/elements-badges-labels.html')
def index15(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/elements-buttons-standard.html')
def index16(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/elements-cards.html')
def index17(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/elements-dropdowns.html')

def index18(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/elements-icons.html')

def index19(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/elements-list-group.html')

def index20(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/elements-navigation.html')
def index21(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/elements-utilities.html')

def index22(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/forms-controls.html')
def index23(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/forms-layouts.html')

def index24(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/forms-validation.html')
def index25(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'remodel/tables-regular.html')

def table(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == 'POST':
        #print(request.POST.get('select'))
        #print(type(request.POST.get('select2')))
        sup = request.POST.get('select')
        support = 0
        #item = request.POST.get('select2')
        if sup == 'A':
           support = 1
        elif sup == 'B':
            support = 1.5
        else:
            support = 1.8
        data = High.objects.filter(sup__gte = support) #.filter(sup__lte = 1.90)
        stu = {'data': data}
        print("hi")
        print(data)
        for d in data:
            print(d.sup)
            
        #print(stu)
        
        return render(request, 'remodel/123.html',stu)
    
def off_res(request, ans):
    print(ans)
    print(type(ans))



