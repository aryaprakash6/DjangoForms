from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def djforms(request):
    ESFO = Schoolform()
    d= {'ESFO': ESFO}
    if request.method == 'POST':
        SFDO = Schoolform(request.POST)
        sn=SFDO.cleaned_data['Sname']   
        sp=SFDO.cleaned_data['Sprincipal']
        sl=SFDO.cleaned_data['Slocation']
        e=SFDO.cleaned_data['email']
        r=SFDO.cleaned_data['renteremail']
        SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sl,email=e,renteremail=r)[0]
        SO.save()
        if SFDO.is_valid():
            return HttpResponse('School is created')

        else:

            return HttpResponse('invalid data')

    return render(request, 'djforms.html',d)