from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User
# from .models import Myuser

from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
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
    return render(request,'../templates/마이_적금카드상품확인.html')

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

# # 회원가입 페이지를 보여주기 위한 함수
# def register(request):   
#     if request.method == "GET":
#         return render(request, '../templates/회원가입.html')

#     elif request.method == "POST":
#         username = request.POST.get['username',None]   # 딕셔너리형태
#         password = request.POST.get['password',None]
#         re_password = request.POST.get['re_password',None]
#         res_data = {} 
#         if not (username and password and re_password) :
#             res_data['error'] = "모든 값을 입력해야 합니다."
#         if password != re_password :
#             # return HttpResponse('비밀번호가 다릅니다.')
#             res_data['error'] = '비밀번호가 다릅니다.'
#         else :
#             user = User(username=username, password=make_password(password))
#             user.save()
#         return render(request, '../templates/회원가입.html', res_data) # register를 요청받으면 register.html 로 응답.

# # 로그인
# def login(request):
#     response_data = {}

#     if request.method == "GET" :
#         return render(request, '../templates/로그인.html')

#     elif request.method == "POST":
#         login_username = request.POST.get('username', None)
#         login_password = request.POST.get('password', None)


#         if not (login_username and login_password):
#             response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
#         else : 
#             myuser = User.objects.get(username=login_username) 
#             #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
#             if check_password(login_password, myuser.password):
#                 request.session['user'] = myuser.id 
#                 #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
#                 #세션 user라는 key에 방금 로그인한 id를 저장한것.
#                 return redirect('/')
#             else:
#                 response_data['error'] = "비밀번호를 틀렸습니다."

#         return render(request, '../templates/로그인.html',response_data)

# # # HOME 함수
# # def home(request):
# #     user_id = request.session.get('user')
# #     if user_id :
# #         myuser_info = User.objects.filter(pk=user_id)  #pk : primary key
# #         return HttpResponse(myuser_info.username)   # 로그인을 했다면, username 출력

# #     return HttpResponse('로그인을 해주세요.') #session에 user가 없다면, (로그인을 안했다면)
    
# # 로그아웃 함수
# def logout(request):
#     request.session.pop('user')
#     return redirect('/')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# 회원 가입
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, '../templates/회원가입.html')

# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, '../templates/로그인.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, '../templates/로그인.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, '../templates/로그인.html')