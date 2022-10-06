from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'../templates/index.html')

def home(request):
    return render(request,'../templates/Home.html')

def login(request):
    return render(request,'../templates/로그인.html')

def 소비(request):
    return render(request,'../templates/마이_개인소비성향.html')

def 자산(request):
    return render(request,'../templates/마이_개인자산상태.html')

def 적금카드(request):
    return render(request,'../templates/적금카드.html')

def my(request):
    return render(request,'../templates/마이페이지.html')

def 주거(request):
    return render(request,'../templates/부동산_맞춤주거지역.html')
def 실거래가(request):
    return render(request,'../templates/부동산_실거래가조회.html')
def 부동산(request):
    return render(request,'../templates/부동산.html')
def 설명회(request):
    return render(request,'../templates/설명회정보.html')
def 주식(request):
    return render(request,'../templates/주식.html')
def 회원가입(request):
    return render(request,'../templates/회원가입.html')

#def first_view(request):
#    return render(request,'../templates/index.html')
    