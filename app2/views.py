from django.http import request
from django.shortcuts import redirect, render
from app2.models import user
# Create your views here.
def home(request):
    return render(request,'home.html')
def homee(request):
    return render(request,'home.html')
def signup(request):
    return render(request,'signup.html')
def sign(request):
    return render(request,'sign.html')
def register(request):
    data=user(uname=request.POST['fname'],email=request.POST['email'],password=request.POST['pswd'])
    data.save()
    return render(request,'sign.html')
def home1(request):
    return redirect('/')
def signup1(request):
    return redirect('/signup')
def sign1(request):
    return redirect('/sign')
def login(request):
    if request.method=='POST':
        if user.objects.filter(email=request.POST['mail'],password=request.POST['pswd']).exists():
            data=user.objects.get(email=request.POST['mail'],password=request.POST['pswd'])
            return render(request,'explore.html',{'vars':data})
        else:
            return render(request,'sign.html')
    else:
        return render(request,'sign.html')
def reg(request):
    return redirect('/signup')
def home3(request):
    return redirect('/')
def signup3(request):
    return redirect('/signup')
def sign3(request):
    return redirect('/sign')
def home4(request):
    return redirect('/')
def signup4(request):
    return redirect('/signup')
def sign4(request):
    return redirect('/sign') 
def tvm(request,id):
    data=user.objects.get(id=id)
    return render(request,'tvm.html',{'vars':data})
def alpi(request,id):
    data=user.objects.get(id=id)
    return render(request,'alappuzha.html',{'vars':data})   
def klm(request,id):
    data=user.objects.get(id=id)
    return render(request,'kollam.html',{'vars':data})
def erkm(request,id):
    data=user.objects.get(id=id)
    return render(request,'erkm.html',{'vars':data})
def idki(request,id):
    data=user.objects.get(id=id)
    return render(request,'idukki.html',{'vars':data})
def trsr(request,id) :
    data=user.objects.get(id=id)
    return render(request,'thrissur.html',{'vars':data})
def kzkod(request,id):
    data=user.objects.get(id=id)
    return render(request,'kzkod.html',{'vars':data})
def ksrgd(request,id):
    data=user.objects.get(id=id)
    return render(request,'kasrgod.html',{'vars':data})
def home5(request):
    return redirect('/')
def signup5(request):
    return redirect('/signup')
def sign5(request):
    return redirect('/sign')
def explore1(request,id):
    data=user.objects.get(id=id)
    return render(request,'explore.html',{'vars':data})
def home6(request):
    return redirect('/')
def signup6(request):
    return redirect('/signup')
def sign6(request):
    return redirect('/sign')
def explore2(request,id):
    data=user.objects.get(id=id)
    return render(request,'explore.html',{'vars':data})
def home7(request):
    return redirect('/')
def signup7(request):
    return redirect('/signup')
def sign7(request):
    return redirect('/sign')
def explore3(request,id):
    data=user.objects.get(id=id)
    return render(request,'explore.html',{'vars':data})
def home8(request):
    return redirect('/')
def signup8(request):
    return redirect('/signup')
def sign8(request):
    return redirect('/sign')
def explore4(request,id):
    data=user.objects.get(id=id)
    return render(request,'explore.html',{'vars':data})
def home9(request):
    return redirect('/')
def signup9(request):
    return redirect('/signup')
def sign9(request):
    return redirect('/sign')
def explore5(request,id):
    data=user.objects.get(id=id)
    return render(request,'explore.html',{'vars':data})
def home10(request):
    return redirect('/')
def signup10(request):
    return redirect('/signup')
def sign10(request):
    return redirect('/sign')
def explore6(request,id):
    data=user.objects.get(id=id)
    return render(request,'explore.html',{'vars':data})
def home11(request):
    return redirect('/')
def signup11(request):
    return redirect('/signup')
def sign11(request):
    return redirect('/sign')
def explore7(request,id):
    data=user.objects.get(id=id)
    return render(request,'explore.html',{'vars':data})
def home12(request):
    return redirect('/')
def signup12(request):
    return redirect('/signup')
def sign12(request):
    return redirect('/sign')
def explore8(request,id):
    data=user.objects.get(id=id)
    return render(request,'explore.html',{'vars':data})
def profile(request,id): 
    data=user.objects.get(id=id)
    return render(request,'profile.html',{'vars':data})
def orgin(request):
    return redirect('/')
def delete(request,id):
    data=user.objects.get(id=id)
    data.delete()
    return redirect('/')
def edit(request,id):
    data=user.objects.get(id=id)
    return render(request,'edit.html',{'vars':data})
def orgin1(request):
    return redirect('/')
def update(request,id):
    data=user.objects.get(id=id)
    data.uname=request.POST.get('name')
    data.email=request.POST.get('mail')
    data.password=request.POST.get('pswd')
    data.save()

    return render(request,'profile.html',{'vars':data})
    