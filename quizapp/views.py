
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


from .forms import Regi
from django.shortcuts import redirect, render
from django.contrib import messages
from quizapp.forms import addform
from .models import Questionpage
# Create your views here.
@login_required
def home(request):
   
    if request.method == 'POST':
        data=Questionpage.objects.all()
        score=0
        attempt=0
        wrong=0
        correct=0
        total=0
        for x in data:
            total+=1
            if x.ans == request.POST.get(x.questiontext):
                score+=10
                correct+=1
                
            else:
                wrong+=1
                
               
                print(request.POST.get(x.questiontext))
        percent = score/(total*10) *100
        context={
            'score':score,
            'wrong':wrong,
            'attempt':attempt,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions=Questionpage.objects.all()
        context = {
            'data':questions
        }
    return render(request,'home.html',context)
@login_required
def addq(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form=addform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'added successfully')
            return redirect('/addq')
    else:
        form=addform()
    return render(request,'addquestion.html',{'form':form})
@login_required
def register(request):
    if request.method  == 'POST':
        reform=Regi(request.POST)
        if reform.is_valid():
            messages.success(request,'account has been created')
            messages.error(request,'account has been created')
            reform.save()
            return redirect('/register')
    reg=Regi()
    return render(request,'register.html',{'reg':reg})
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
    else:
        return render(request,'login.html')
@login_required
def logoutpage(request):
    logout(request)
    return redirect('loginPage')