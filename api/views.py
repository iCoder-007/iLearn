
from django.shortcuts import render
from .serializers import LoginSerializer 
from rest_framework.parsers import FileUploadParser
from .serializers import CategorySerializer ,CreateCourseSerializer,VideoSerializer,AnswerQuerySerializer,GetVideosSerializer,AddCartSerializer,HomeTutorSerializer,RemoveCartSerializer,GetHomeTutorSerializer,ADDMYCOURSESSerializer,ContactUs,TestResultSerializer,GetQuizeResultSerializer,TestAllSerializer,AddTestCartSerializer,TestCart,RemoveTestCartSerializer,TestSerializer,EditHomeTutorSerializer,GetPaidVideosSerializer,GetUrlSerializer,AddTestSerializer,TestResultSerializer,GDSerializer,WatchedSerializer,ADDMYCOURSESFreeSerializer,RemoveMyTestSerializer,NewDoubtSerializer,LikeSerializer,DRSerializer,BookMarkSerializer,ReplyDSerializer,WalletSerializer,ReportSerializer,ADForMQSerializer,WinnerMQSerializers,AddReviewSerializers,asknewquerySerializers,GNSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import generics
from home.models import Categories,Courses,HomeTutor,Courses,Videos,WatchedVideos,Cart,MyCourses,Contact,Test,TestResult,MyTest,InstructorAddedTest,TestCategories,HomeTutorDemo,WatchedVideos,TeachCategories,Doubt,Doubtliked,DoubtReply,Updates,BookMark,DoubtReply,SratchCard,wallet,MegaQuizInstruction,Megaquiz,AccountDetailsForMQ,MegaquizResult,ReviewCourse,GeneralNotify,Notes,Feed,SavedFeed,FeedComment,WordoftheDay,FeedLike,FeedShare,Practice,PracticeEnglish,Stories,MegaQuizEnglish,MegaQuizHindi,PreviousPaper,alert,alertrecieved
from mutagen.mp4 import MP4
from django.shortcuts import render
from PayTm import Checksum
from django.http import JsonResponse
import boto3
from datetime import datetime
from django.contrib.postgres.search import SearchVector, SearchQuery
# from moviepy.editor import *
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


from django.db.models import Q
MERCHANT_KEY = '&WgbAKt0koh9BCFx'
session = boto3.session.Session()
key='W55UFC7TLFNFFNAFPCSX'
secret='Nb0GaC9os1fQlYVxJpP4y5wpTLZdQUctR1fTHqle+aI'
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def geturl(request):
    serializer = GetUrlSerializer(data=request.data)
    file=request.data['url']
    client=session.client('s3',region_name='sgp1',endpoint_url='https://sgp1.digitaloceanspaces.com',aws_access_key_id=key,aws_secret_access_key=secret)
    urli=client.generate_presigned_url(ClientMethod='get_object',Params={'Bucket':'cognedu-spaces','Key':file},ExpiresIn=3600)
    return Response({'data':urli})

@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) != None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)

        username = request.data.get('username', '0')
        if validate_username(username) != None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            return Response(data)

        serializer = RegistrationSerializer(data=request.data)
        did=request.data.get('deviceId')
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user'
            data['email'] = account.email
            data['role'] = account.first_name
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
                
        else:
            data = serializer.errors
        return Response(data)

def validate_email(email):
    account = None
    try:
        account =   User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    if account != None:
        return email

def validate_username(username):
    account = None
    try:
        account = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    if account != None:
        return username



class ObtainAuthTokenView(APIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context = {}
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key,'role':user.first_name}, status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def logout(request):
    try:
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    except(AttributeError):
       return Response(status=status.HTTP_200_OK)
@api_view(['POST', ])
@permission_classes(())
@authentication_classes([])
def categories(request):
    cat=list(TeachCategories.objects.all().values().order_by('timeStamp'))
    tcat=list(TestCategories.objects.all().values())
    serializer_class=CategorySerializer
    course=set()    
    sub_cat=set()
    sub_cat2=set()
    tcourse=set()
    tsub_cat=set()
    tsub_cat2=set()
    for cours in cat:
        course.add(cours['category'])
        sub_cat.add((cours['sub_category'],cours['category']))
        sub_cat2.add((cours['sub_category'],cours['sub_category2']))
    for coursi in tcat:
        tcourse.add(coursi['category'])
        tsub_cat.add((coursi['sub_category'],coursi['category']))
        tsub_cat2.add((coursi['sub_category'],coursi['sub_category2']))
   
    return Response({'categories':cat,'course':course,'sub_cat':sub_cat,'sub_cat2':sub_cat2,'tcategories':tcat,'tcourse':tcourse,'tsub_cat':tsub_cat,'tsub_cat2':tsub_cat2},status=200)
@api_view(['POST', ])
@permission_classes(())
@authentication_classes([])
def categoriesu(request):
    cat=list(Categories.objects.all().values())
    tcat=list(TestCategories.objects.all().values())
    serializer_class=CategorySerializer
    course=set()    
    sub_cat=set()
    sub_cat2=set()
    tcourse=set()
    tsub_cat=set()
    tsub_cat2=set()
    for cours in cat:
        course.add(cours['category'])
        sub_cat.add((cours['sub_category'],cours['category']))
        sub_cat2.add((cours['sub_category'],cours['sub_category2']))
    for coursi in tcat:
        tcourse.add(coursi['category'])
        tsub_cat.add((coursi['sub_category'],coursi['category']))
        tsub_cat2.add((coursi['sub_category'],coursi['sub_category2']))
   
    return Response({'categories':cat,'course':course,'sub_cat':sub_cat,'sub_cat2':sub_cat2,'tcategories':tcat,'tcourse':tcourse,'tsub_cat':tsub_cat,'tsub_cat2':tsub_cat2},status=200)

@api_view(['POST', ])
@permission_classes(())
@authentication_classes([])
def courses(request):
    serializer = CategorySerializer(data=request.data)
    cat=request.data.get('s')
    scat=request.data.get('sc')
    scat2=request.data.get('sc2')
    courses=list(Courses.objects.filter(category=cat).filter(sub_category=scat).filter(sub_category2=scat2).filter
    (verified="True").values().order_by('category'))
    print(courses)
    return Response({'courses':courses},status=200)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def reghometutor(request):
    serializer = HomeTutorSerializer(data=request.data)
    name=request.data.get('name')
    email=request.data.get('email')
    phone=request.data.get('phone')
    age=request.data.get('age')
    gender=request.data.get('gender')
    pin=request.data.get('pin')
    state=request.data.get('state')
    district=request.data.get('district')
    subject=request.data.get('subject')
    classes=request.data.get('classes')
    disc=request.data.get('discription')
    salaryL=request.data.get('salaryL')
    id_proof=request.data.get('id_proof')
    salaryH=request.data.get('salaryH')
    salaryL=int(salaryL.split('.')[0])
    salaryH=int(salaryH.split('.')[0])
    print(name,email,phone,age,gender,pin,district,subject,classes)
    if  len(name)>4 and len(age)!=0 and len(gender)!=0 and len(phone)>9 and len(email)>0 and len(pin)==6 and len(district)>0 and len(state)>0 and len(subject)>0 and len(classes)>0 and len(disc)>0 and (salaryL)>0 and (salaryH)>0:
        ht=HomeTutor(user=request.user,name=name,age=age,gender=gender,phone=phone,email=email,pin=pin,district=district,
                state=state,subject=subject,classes=classes,discription=disc,salaryL=salaryL,salaryH=salaryH,registered_for='Home Tutor',verified='False',id_proof=id_proof)
        ht.save()
        return Response({'Response':'OK'},status=200)
    else:
        return Response({'Response':'Error'},status=204)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def edithometutor(request):
    serializer = HomeTutorSerializer(data=request.data)
    sno=request.data.get('sno')
    name=request.data.get('name')
    email=request.data.get('email')
    phone=request.data.get('phone')
    age=request.data.get('age')
    gender=request.data.get('gender')
    pin=request.data.get('pin')
    state=request.data.get('state')
    district=request.data.get('district')
    subject=request.data.get('subject')
    classes=request.data.get('classes')
    disc=request.data.get('discription')
    salaryL=request.data.get('salaryL')
    id_proof=request.data.get('id_proof')
    salaryH=request.data.get('salaryH')
    salaryL=int(salaryL.split('.')[0])
    salaryH=int(salaryH.split('.')[0])
    ht=HomeTutor.objects.get(sno=int(sno))
    ht.name=name
    ht.age=age
    ht.gender=gender
    ht.phone=phone
    ht.email=email
    ht.pin=pin
    ht.district=district
    ht.state=state
    ht.subject=subject
    ht.classes=classes
    ht.discription=disc
    ht.salaryL=salaryL
    ht.salaryH=salaryH
    ht.id_proof=id_proof
    ht.save()
        
    return Response({'Response':'OK'},status=200)


class Createcourse(APIView):
    parser_class=(FileUploadParser,)
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = CreateCourseSerializer(data=request.data)
        title=request.data.get('title')
        category=request.data.get('category')
        sub_category=request.data.get('sub_category')
        sub_category2=request.data.get('sub_category2')
        courseThumbnail=request.data.get('courseThumbnail')
        discription=request.data.get('discription')
        language=request.data.get('language')
        pricing=request.data.get('pricing')
        c=Courses(title=title,category=category,sub_category=sub_category,sub_category2=sub_category2,language=language,courseThumbnail=courseThumbnail,discription=discription,pricing=pricing,creater_name=request.user.username,creater=request.user)
        c.save()
        print(courseThumbnail,request.user.username)
        return Response({'Response':'Done'},status=200)


class AddVideo(APIView):
    parser_class=(FileUploadParser,)
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = VideoSerializer(data=request.data)
        videoTitle=request.data.get('videoTitle')
        videofile=request.data.get('videofile')
        thumbnail=request.data.get('thumbnail')
        resource=request.data.get('resource')
        videoOfCourse=request.data.get('videoOfCourse')
        v=Courses.objects.get(sno=int(videoOfCourse))
        c=Videos(videoTitle=videoTitle,videofile=videofile,thumbnail=thumbnail,resource=resource,videoOfCourse=v,creater=request.user)
        c.save()
        return Response({'Response':'Done'},status=200)
class GetVideo(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = GetVideosSerializer(data=request.data)
        videoOfCourse=request.data.get('videoOfCourse')
        c=Courses.objects.get(sno=int(videoOfCourse))
        v=list(Videos.objects.filter(videoOfCourse=c).order_by('timeStamp').values())
        print(v)
        
        return Response({'Response':v},status=200)




@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def createdcourses(request):
    courses=list(Courses.objects.filter(creater=request.user).values().order_by('category'))
    return Response({'courses':courses},status=200)

    
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def performance(request):
    courses=list(Courses.objects.filter(creater=request.user).values().order_by('category'))
    if len(courses) > 0:
        return Response({'courses':courses},status=200)
    else :
        return Response({'courses':""},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def studentquery(request):
    courses=list(WatchedVideos.objects.filter(creater=request.user.id).values().order_by('timeStamp'))
    q=[]
    for item in courses:
        if(len(item['answer'])<2):
            user=User.objects.get(id=int(item['user_id']))
            q.append([item,user.username])
 
    return Response({'query':q},status=200)

class AnswerQuery(APIView):
    parser_class=(FileUploadParser,)
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = AnswerQuerySerializer(data=request.data)
        answer=request.data.get('answer')
        id=request.data.get('id')
        c=WatchedVideos.objects.get(sno=int(id))
        c.answer=answer
        c.save()
        return Response({'Response':'Done'},status=200)
class AddCart(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = AddCartSerializer(data=request.data)
        id=request.data.get('course')
        c=Courses.objects.get(sno=int(id))
        cart=Cart(course=c,user=request.user)
        cart.save()
        return Response({'Response':'done'},status=200)
class AddTestCart(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = AddTestCartSerializer(data=request.data)
        id=request.data.get('test')
        c=Test.objects.get(sno=int(id))
        cart=TestCart(test=c,user=request.user)
        cart.save()
        return Response({'Response':id},status=200)
class RemoveCart(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = RemoveCartSerializer(data=request.data)
        id=request.data.get('sno')
        print(id)
        try:
            c=Cart.objects.filter(course_id=int(id)).filter(user=request.user)
            c.delete()
        except:
            pass
        return Response({'Response':'done'},status=200)
class RemoveTestCart(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = RemoveTestCartSerializer(data=request.data)
        id=request.data.get('sno')
        
        try:
            c=TestCart.objects.filter(test_id=int(id)).filter(user=request.user)
            c.delete()
        except:
            pass
        return Response({'Response':'done'},status=200)
class GetCart(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        c=list(Cart.objects.filter(user=request.user).order_by().values())
        
        return Response({'Response':(c)},status=200)
class GetDetailedCart(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        c=list(Cart.objects.filter(user=request.user).order_by())
        t=list(TestCart.objects.filter(user=request.user).order_by())
        cartItems=[]
        carttItems=[]
        ct=[]
        print(t)
        for item in c:
            cartItems.append([(Courses.objects.filter(sno=item.course_id).values()),item.sno])
        for item in t:
            
            carttItems.append([(Test.objects.filter(sno=item.test_id).values()),item.sno])
            print(carttItems)
        ct.append(cartItems)
        ct.append(carttItems)

        return Response({'Response':ct},status=200)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def checkhreg(request):
    htp=''
    htp=list(HomeTutor.objects.filter(user=request.user).values())
    return Response({'courses':htp},status=200)

@api_view(['POST', ])
@permission_classes(( ))
@authentication_classes([])
def gethomet(request):
    serializer = GetHomeTutorSerializer(data=request.data)
    pin=request.data.get('pin')
    classes=request.data.get('classes')
    sub=request.data.get('sub')
    htp=(HomeTutor.objects.filter(pin=int(pin)).values())
    result=Q()
    result1=Q()
    for i in classes:
        result=result | Q(classes__icontains=str(i).split(' ')[1])
    for i2 in sub:
        result1=result1 | Q(subject__icontains=str(i2))
    htp=htp.filter(result)
    htp=htp.filter(result1)
    return Response({'courses':htp},status=200)
@csrf_exempt
def buynow(request):
    if request.method=='POST':
        cid=[]
        cid1=[]
        
        if len(request.POST.get('cid'))>2:
            cid=request.POST.get('cid')[1:-1].split(',')
        else:
            cid=[]
        if len(request.POST.get('cid2'))>2: 
            cid1=request.POST.get('cid2')[1:-1].split(',')
        else:
            cid1=[]
        try:
            offer=request.POST.get('offer')
        except:
           offer=0
        if offer == None:
           offer=0
        cs=request.POST.get('cso')
        l=0
        id=''
        if(len(cid)>1 or  cid!=''):
            for item in cid:
                id=id+str(Courses.objects.get(sno=int(item)).sno)+'H'
                l+=int(Courses.objects.get(sno=int(item)).pricing)
        if( len(cid1)>1 or cid1!=''):
            for item in cid1:
                id=id+str(Test.objects.get(sno=int(item)).sno)+'H'
                l+=int(Test.objects.get(sno=int(item)).Price)
        param_dict = {

                    'MID':'pKZNZu37586797634551',
                    'ORDER_ID': cs,
                    'TXN_AMOUNT':str(int(l)-int(offer)),
                    'CUST_ID': 'ssygi0007@gmail.com',
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': 'WEBSTAGING',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL':'https://cognedu.com/api/handleRequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request,'home/paytm.html',{'param_dict':param_dict})
    
    return redirect('/cart')
def payment(request):
    return render(request,'home/paymentStatus.html')
@csrf_exempt
def handleRequest(request):
    form = request.POST
    response_dict = {}
    stat=1
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
            stat=0
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            status='TXN_SUCCESS'
            
        else:
            status="TXN_FAILURE"
    return JsonResponse({'data':response_dict,'status':stat})


class AddToMyCourses(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = ADDMYCOURSESSerializer(data=request.data)
        c=request.data.get('course')
        t=request.data.get('test')
        cs=request.data.get('cartid')
        cs1=cs.split('HT')
        offer=request.data.get('offer')
        try:
            wlt=wallet.objects.filter(user=request.user).values()[0]
            wlt.remaining=str(int(wlt.remaining)-int(offer))
            wlt.save()
        except:
            pass
        cso=cs1[0].split('H')
        if len(cs1)>1:
            cso1=cs1[1].split('T')
        for item in range(len(cso)-1):
            m=MyCourses(course=Courses.objects.get(sno=int(c[item])),order_id=int(cso[item]),user=request.user)
            m.save()
            c=Cart.objects.get(sno=int(cso[item]))
            c.delete()
        if len(cs1)>1:
            cso1=cs1[1].split('T')
            for item in range(len(cso1)-1):
                
                m=MyTest(test=Test.objects.get(sno=int(t[item])),order_id=int(cso1[item]),user=request.user)
                m.save()
                c=TestCart.objects.get(sno=int(cso1[item]))
                c.delete()

        return Response({'Response':'cartItems'},status=200)
class Contactus(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = ContactUs(data=request.data)
        name=request.data.get('name')
        email=request.data.get('email')
        query=request.data.get('query')
        c=Contact(name=name,username=request.user.username,email=email,user=request.user,content=query)
        c.save()
        return Response({'Response':'Ok'},status=200)
class Quize(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = TestSerializer(data=request.data)
        id=request.data.get('id')
        q=list(Test.objects.filter(sno=id).values())
        
        return Response({'Response':q},status=200)
class SubmitQuize(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = TestResultSerializer(data=request.data)
        test=request.data.get('test')
        answer=request.data.get('answer')
        correct=request.data.get('correct')
        t=Test.objects.get(sno=int(test))
        st=TestResult(user=request.user,test=t,useranswer=answer,correct=int(correct))
        st.save()
        return Response({'Response':'Ok'},status=200)
class GetQuizeResult(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = GetQuizeResultSerializer(data=request.data)
        test=request.data.get('id')
        t=TestResult.objects.filter(test_id=int(test)).filter(user=request.user).values()
        gt=Test.objects.filter(sno=int(t[0]['test_id'])).values()
        allt=TestResult.objects.all()
        avg=0
        maxm=0
        for item in allt:
            if item.correct>maxm:
                maxm=item.correct
            avg+=item.correct
        avg/=len(allt)
        l=[]
        l.append((t))
        l.append(avg)
        l.append(maxm)
        l.append(gt)
        return Response({'Response':l},status=200)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def testall(request):
    serializer = TestAllSerializer(data=request.data)
    cat=request.data.get('s')
    scat=request.data.get('sc')
    scat2=request.data.get('sc2')
    v=cat+'/'+scat+'/'+scat2
    courses=(Test.objects.filter(category__icontains=v).values().order_by('category'))
    c=[]
    for item in courses:
        print(item['sno'])
        q=TestCart.objects.filter(user=request.user).filter(test_id=item['sno'])
        if len(q)>0:
            c.append([item,1])
        else:
            c.append([item,0])
    return Response({'courses':c},status=200)

class GetMyTest(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        t=list(MyTest.objects.filter(user=request.user).order_by())
        carttItems=[]
        for item in t:
            y=TestResult.objects.filter(test_id=item.test_id).filter(user=request.user).values()
            
            if len(y)>0:
                time=y[0]['timeStamp']
                st='given'
            else:
                time=''
                st='notgiven'
            carttItems.append([(Test.objects.filter(sno=item.test_id).values()),item.sno,item.timeStamp,st,time])
        return Response({'Response':carttItems},status=200)
class GetMyCourse(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        t=list(MyCourses.objects.filter(user=request.user).order_by())
        r=ReviewCourse.objects.filter(username=request.user.username).values()
        carttItems=[]
        for item in t:
            carttItems.append(Courses.objects.filter(sno=item.course_id).values())
        return Response({'Response':carttItems,'review':r},status=200)
class GetPaidVideos(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = GetPaidVideos(data=request.data)
        id=request.data.get('sno')
        t=list(Videos.objects.filter(videoOfCourse_id=int(id)).order_by('timeStamp').values())
        w=list(WatchedVideos.objects.filter(user=request.user).order_by('timeStamp').values())
        carttItems=[]
        c=0
        i1=''
        for item in t:
            urli=item['videofile']
            c+=1
            for i in w:
                if(str(item['sno'])==str(i['watched_id'])):
                    i1=1
                else:
                    i1=0
                
            if c==1:
                file='media/'+item['videofile']
                client=session.client('s3',region_name='sgp1',endpoint_url='https://sgp1.digitaloceanspaces.com',aws_access_key_id=key,aws_secret_access_key=secret)
                urli=client.generate_presigned_url(ClientMethod='get_object',Params={'Bucket':'cognedu-spaces','Key':file},ExpiresIn=300)            
            carttItems.append([item,urli,i1])
            
        return Response({'Response':carttItems},status=200)
class GetFeaturedVideos(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        c=(Courses.objects.filter(Marked='featured').order_by('-timeStamp').values())
        t=(Courses.objects.filter(Marked='popular').order_by('-timeStamp').values())
        carttItems=[]
        carttItems.append(c)
        carttItems.append(t)
        return Response({'Response':carttItems},status=200)
class AddVideo(APIView):
    parser_class=(FileUploadParser,)
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = VideoSerializer(data=request.data)
        videoTitle=request.data.get('videoTitle')
        videofile=request.data.get('videofile')
        thumbnail=request.data.get('thumbnail')
        resource=request.data.get('resource')
        videoOfCourse=request.data.get('videoOfCourse')
        v=Courses.objects.get(sno=int(videoOfCourse))
        c=Videos(videoTitle=videoTitle,videofile=videofile,thumbnail=thumbnail,resource=resource,videoOfCourse=v,creater=request.user)
        c.save()
        return Response({'Response':'Done'},status=200)
class AddTest(APIView):
    parser_class=(FileUploadParser,)
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = AddTestSerializer(data=request.data)
        title=request.data.get('title')
        price=request.data.get('price')
        resource=request.data.get('resource')
        c=InstructorAddedTest(title=title,price=price,testfile=resource,user=request.user)
        c.save()
        return Response({'Response':'Done'},status=200)
@api_view(['POST', ])
@permission_classes(())
@authentication_classes([])
def search(request):
    serializer = TestResultSerializer(data=request.data)
    query=request.data.get('text')
    result=Courses.objects.annotate(search=SearchVector('title') + SearchVector('category')+SearchVector('sub_category')+SearchVector('creater_name')+SearchVector('sub_category2')).filter(search = SearchQuery(query)).filter(verified="True").values()
    result2=Test.objects.annotate(search=SearchVector('title') + SearchVector('category')+SearchVector('creater')).filter(search = SearchQuery(query)).values()
    return Response({'searchResults':result,'test':result2},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def getdemo(request):
    serializer = GDSerializer(data=request.data)
    name=request.data.get('name')
    phone=request.data.get('phone')
    email=request.data.get('email')
    add=request.data.get('address')
    pin=request.data.get('pin')
    tname=request.data.get('tname')
        
    st=HomeTutorDemo(user=request.user,pin=int(pin),fullname=name,phone=phone,email=email,homeTutor=tname,address2=add)
    st.save()
    return Response({'Response':name},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def addwatched(request):
    serializer = WatchedSerializer(data=request.data)
    watch=request.data.get('watched')
    creater=request.data.get('creater')
    v=Videos.objects.get(sno=int(watch))
    c=WatchedVideos(user=request.user,creater=creater,watched=v)
    c.save()
    return Response({'Response':watch},status=200)


class AddToMyCoursesFree(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        #serializer = ADDMYCOURSESFreeSerializer(data=request.data)
        #t=request.data.get('test')
        #m=MyTest(test=Test.objects.get(sno=int(t)),order_id=int(str(request.user.id+int(t))),user=request.user)
        #m.save()
        print('jl')
        return Response({'Response':'ok'},status=200)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def freetest(request):
    serializer = ADDMYCOURSESFreeSerializer(data=request.data)
    name=request.data.get('test')
    serializer = ADDMYCOURSESFreeSerializer(data=request.data)
    t=request.data.get('test')
    m=MyTest(test=Test.objects.get(sno=int(t)),order_id=int(str(request.user.id+int(t))),user=request.user)
    m.save()

    return Response({'Response':'ok'},status=200)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def removeMyTest(request):
    serializer = RemoveMyTestSerializer(data=request.data)
    id=request.data.get('sno')
    
    try:
        c=TestResult.objects.filter(test_id=int(id)).filter(user=request.user)
        c.delete()
        cv=MyTest.objects.filter(test_id=int(id)).filter(user=request.user)
        cv.delete()
        return Response({'Response':id},status=200)

    except:
        return Response({'Response':'failed'},status=200)



@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def newdoubt(request):
    parser_class=(FileUploadParser,)
    serializer = TestAllSerializer(data=request.data)
    query=request.data.get('query')
    queryimg=request.data.get('queryimage')
    c=Doubt(user=request.user,username=request.user.username,doubttext=query,doubtfile=queryimg)
    c.save()
    return Response({'courses':'ok'},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def fetchdoubts(request):
    c=Doubt.objects.all().order_by('-sno').values()
    do=Doubtliked.objects.filter(user=request.user).values()
    return Response({'courses':c,'doubt':do,'time':datetime.now()},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def liked(request):
    serializer = LikeSerializer(data=request.data)
    sno=request.data.get('sno')
    liked=request.data.get('likestatus')
    d=Doubt.objects.get(sno=int(sno))
    if liked == True:
        Do=Doubtliked(user=request.user,doubt=d)
        Do.save()
        d.likecount+=1
    else :
        Do=Doubtliked.objects.filter(doubt=d)
        Do.delete()
        d.likecount-=1
    d.save()
    c=Doubt.objects.all().values()
    return Response({'courses':liked},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def doubtreply(request):
    serializer = DRSerializer(data=request.data)
    sno=request.data.get('sno')
    
    do=DoubtReply.objects.filter(doubt_id=sno).values()
    return Response({'doubtrep':do},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def update(request):
    up=Updates.objects.all().order_by('-timeStamp').values()[:10]
    bk=BookMark.objects.filter(user=request.user).order_by('timeStamp').values()
    return Response({'doubtrep':up,'bm':bk},status=200)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def bookmark(request):
    serializer = BookMarkSerializer(data=request.data)
    sno=request.data.get('sno')
    action=request.data.get('action')
    do=Updates.objects.get(sno=int(sno))
    if action=='add':
        bm=BookMark(update=do,user=request.user)
        bm.save()
    else:
        bk=BookMark.objects.filter(update=do,user=request.user)
        bk.delete()
    return Response({'doubtrep':'ok'},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def replyd(request):
    parser_class=(FileUploadParser,)
    serializer = ReplyDSerializer(data=request.data)
    sno=request.data.get('sno')
    d=Doubt.objects.get(sno=int(sno))
    f=request.data.get('file')
    text=request.data.get('text')
    do=DoubtReply(user=request.user,username=request.user.username,doubt=d,doubtfile=f,reply=text)
    do.save()
    return Response({'doubtrep':'ok'},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def bookmarked(request):
    c=[]
    b=BookMark.objects.filter(user=request.user).values()
    for item in b:
        c.append(Updates.objects.filter(sno=int(item['update_id'])).values())
    return Response({'doubtrep':c},status=200)

@api_view(['POST', ])   
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def getwallet(request):
    serializer = WalletSerializer(data=request.data)
    amt=request.data.get('amount')
    sno=request.data.get('sno')
    cardtype=request.data.get('cardtype')
    w=wallet.objects.filter(user=request.user)
    if cardtype=='purple':
        sc=SratchCard.objects.filter(user=request.user).first()
        sc.status=True
        sc.amount=amt
        sc.save()
    if cardtype=='blue':
       sc=SratchCard.objects.get(sno=int(sno))
       sc.status=True
       sc.amount=amt
       sc.save() 
    if len(w)==0:
        d=wallet(amount=amt,remaining=amt,user=request.user)
        d.save()
    else:
        wl=wallet.objects.get(user=request.user)
        wl.amount=str(int(wl.amount)+int(amt))
        wl.remaining+=amt
        wl.save()
    return Response({'courses':'ok'},status=200)


@api_view(['POST', ])   
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def wlt(request):
    w=wallet.objects.filter(user=request.user).values()
    sc=SratchCard.objects.filter(user=request.user).values()
    return Response({'wallet':w,'sc':sc},status=200)

@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view1(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) != None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)

        username = request.data.get('username', '0')
        if validate_username(username) != None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            return Response(data)

        serializer = RegistrationSerializer(data=request.data)

        did=request.data.get('deviceId')
        share=""
        f=0
        share=did.split('REF')[1]
        if share !="":
            f=share.rfind('#')
            ref=share[0:f]
            try:
                u=User.objects.get(username=ref)
                sq=SratchCard.objects.filter(user=u).filter(deviceId=did.split('REF')[0]).filter(cardtype='blue')
                if len(sq)==0 :
                    data['sharecard']='No'
                    st=SratchCard(user=u,deviceId=did.split('REF')[0],cardtype='blue')
                    st.save()
                else:
                    data['sharecard']='Yes'
            except :
                data1={}
                data1['error_message'] = 'Invalid referral code.'
                data1['response'] = 'Error'
                return Response(data1)

        if serializer.is_valid():
            account = serializer.save() 
            data['response'] = 'successfully registered new user'
            data['email'] = account.email
            data['role'] = account.first_name
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
            s=SratchCard.objects.filter(deviceId=did.split('REF')[0]).filter(cardtype='purple').values()
            if s!=None and len(s)>0:
                data['scard']='Yes'    
            else:
                data['scard']='No'
                sc=SratchCard(user=account,deviceId=str(did).split('REF')[0],cardtype='purple')
                sc.save()
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def report(request):
    serializer = ReportSerializer(data=request.data)
    rs=request.data.get('sno')
    r=Doubt.objects.get(sno=rs)
    r.reports+=1
    r.save()
    return Response({'response':'ok'},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def megaquizIns(request):
    r=MegaQuizInstruction.objects.all().values()[0]
    ad=AccountDetailsForMQ.objects.filter(user=request.user).values()
    now = datetime.now()
    mqr=MegaquizResult.objects.all().values()
    mqmyr=MegaquizResult.objects.filter(user=request.user).values()
    mqe=MegaQuizEnglish.objects.all().values()
    mqh=MegaQuizHindi.objects.all().values()
    return Response({'response':r,'ad':ad,'time':now,'mqr':mqr,'mqe':mqe,'mqh':mqh,'mqmyr':mqmyr},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def adformq(request):
    serializer = ADForMQSerializer(data=request.data)
    mq=AccountDetailsForMQ.objects.filter(user=request.user)
    
    r=request.data.get('ad')
    if len(mq)>0:
        ad=AccountDetailsForMQ.objects.get(user=request.user)
        ad.language=r
        ad.save()
    else:
        mq=AccountDetailsForMQ(user=request.user,language=r)
        mq.save()
    return Response({'response':'ok'},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def editadformq(request):
    serializer =  ADForMQSerializer(data=request.data)
    r=request.data.get('ad')
    mq=AccountDetailsForMQ.objects.get(user=request.user)
    mq.upi=r
    mq.save()
    return Response({'response':'ok'},status=200)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def notifyChange(request):
    d=Doubt.objects.filter(user=request.user).values()
    c=[] 

    for item in d:
        p=DoubtReply.objects.filter(notified=False).filter(doubt_id=item['sno']).values()
        for it in p:
            v=DoubtReply.objects.get(sno=it['sno'])
            c.append(it)
            v.notified=True
            v.save()
    return Response({'response':c},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def winners(request):
    serializer = WINMQSerializer(data=request.data)
    w1=request.data.get('winner1')
    w2=request.data.get('winner2')
    w3=request.data.get('winner3')
    d=Megaquiz.objects.all().order_by('-sno')[0]
    user1=User.objects.get(username=w1)
    user2=User.objects.get(username=w2)
    user3=User.objects.get(username=w3)
    d.winner1=user1
    d.winner1name=user1.username
    d.winner2=user2
    d.winner2name=user2.username
    d.winner3=user3
    d.winner3name=user3.username
    d.save()  
    return Response({'response':'ok'},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def addresults(request):
    serializer = WinnerMQSerializers(data=request.data)
    score=request.data.get('score')
    time=request.data.get('time')
    d=Megaquiz.objects.all().order_by('-sno')[0]
    re=MegaquizResult(mq=d,user=request.user,score=score,time=time,username=request.user.username)
    re.save()
    return Response({'response':'ok'},status=200)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def getresults(request):
    d=Megaquiz.objects.all().order_by('-sno')[0]
    mqr=MegaquizResult.objects.filter(mq=d).values()
    l=[]
    for ob in mqr:
        l.append([int(ob['score'])*1000-int(ob['time']),ob['username'],ob['score'],ob['time']])
    l.sort(reverse=True)
    d.winner1name=l[0][1]
    d.winner2name=l[1][1]
    d.winner3name=l[2][1]
    d.save()
    return Response({'w1':l[0],'w2':l[1],'w3':l[2]},status=200)

class GetCtest(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        serializer = GetPaidVideos(data=request.data)
        id=request.data.get('id')
        t=list(Test.objects.filter(courses_id=id))
        carttItems=[]
        for item in t:
            y=TestResult.objects.filter(test_id=item.sno).filter(user=request.user).values()
            if len(y)>0:
                time=y[0]['timeStamp']
                st='given'
            else:
                time=''
                st='notgiven'
            carttItems.append([Test.objects.filter(sno=item.sno).values(),item.sno,item.timeStamp,st,time])
        return Response({'Response':carttItems},status=200)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def addReview(request):
    serializer = AddReviewSerializers(data=request.data)
    csno=int(request.data['sno'])
    value=int(request.data['rating'])
    action=(request.data['action'])
    course=Courses.objects.get(sno=csno)
    if action=='basereview':
        review =ReviewCourse(reviewOfCourse=course,rating=value,review='',username=request.user.username)
        review.save()
        course.rating+=value
        course.ratedBy+=1
        course.save()
    elif action=='editreview':
        rev=ReviewCourse.objects.get(username=request.user.username)
        rate=rev.rating
        course.rating=course.rating-rate+value
        course.save()
        rev.rating=value
        rev.review=treview
        rev.save()
    return Response({'response':'ok'},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def raisenewquery(request):
    serializer = asknewquerySerializers(data=request.data)
    vid=request.data.get('video')
    query=request.data.get('query')
    creater=request.data.get('creater')
    video=Videos.objects.get(videoTitle=vid)
    wv=WatchedVideos(user=request.user,creater=int(creater),query=query,watched=video)
    wv.save()
    return Response({'response':'ok'},status=200)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def studentaskquery(request):
    courses=list(WatchedVideos.objects.filter(user_id=request.user.id).values().order_by('timeStamp'))
    q=[]
    for item in courses:
        if(len(item['answer'])>-1):
            user=User.objects.get(id=int(item['user_id']))
            q.append([item,user.username])

    
    return Response({'query':q},status=200)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def generalnotify(request):
    serializer = GNSerializers(data=request.data)
    vid=request.data.get('title')
    query=request.data.get('message')
    wv=GeneralNotify(user=request.user,title=vid,message=video)
    wv.save()
    return Response({'response':'ok'},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def getgeneralnotify(request):
    wv=GeneralNotify.objects.all().values()
    return Response({'response':wv},status=200)

@api_view(['POST', ])
@permission_classes(())
@authentication_classes([])
def getnotes(request):
    serializer = CategorySerializer(data=request.data)
    cat=request.data.get('category')
    scat=request.data.get('sub_category')
    scat2=request.data.get('sub_category2')
    s=str(scat)+'/'+str(scat2)
    courses=list(Notes.objects.filter(language=cat).filter(category=s).values().order_by('category'))
    return Response({'courses':courses},status=200)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def getfeeds(request):
    feeds=Feed.objects.filter(isVerified=True).order_by('-timeStamp').values()
    comments=FeedComment.objects.all().order_by('-timeStamp').values()
    likes=FeedLike.objects.filter(user=request.user).order_by('-timeStamp').values()
    saved=SavedFeed.objects.filter(user=request.user).order_by('-timeStamp').values()
    st=Stories.objects.all().values()
    return Response({'feeds':feeds,'comments':comments,'saved':saved,'likes':likes,'st':st},status=200)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def wordoftheday(request):
    feeds=WordoftheDay.objects.all().order_by('-timeStamp').values()[0]
    return Response({'feeds':feeds},status=200)

@api_view(['POST', ])
@permission_classes(())
@authentication_classes([])
def acacom(request):
     c=(Courses.objects.filter(category='Academics').filter(verified="True").order_by('-timeStamp').values())
     t=(Courses.objects.filter(category='Competitive Exams').filter(verified="True").order_by('-timeStamp').values())
     carttItems=[]
     carttItems.append(c)
     carttItems.append(t)
     return Response({'Response':carttItems},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def feedlike(request):
    serializer = BookMarkSerializer(data=request.data)
    sno=request.data.get('sno')
    feed=Feed.objects.get(sno=int(sno))
    feed.likes+=1
    fl=FeedLike(user=request.user,username=request.user.username,feed=feed)
    fl.save()
    feed.save()
    return Response({'response':'ok'},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def feedshare(request):
    serializer = BookMarkSerializer(data=request.data)
    sno=request.data.get('sno')
    feed=Feed.objects.get(sno=int(sno))
    fl=FeedShare(user=request.user,username=request.user.username,feed=feed)
    feed.shares+=1
    feed.save()
    fl.save()
    return Response({'response':'ok'},status=200)
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def removefeedlike(request):
    serializer=BookMarkSerializer(data=request.data)
    sno=request.data.get('sno')
    feed=Feed.objects.get(sno=int(sno))
    lk=FeedLike.objects.filter(user=request.user).filter(feed=feed)
    if len(lk)>0:
        lk.delete()
        feed.likes-=1
        feed.save()
    return Response({'response':'ok'},status=200)
    
@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def removefeedshare(request):
    serializer=BookMarkSerializer(data=request.data)
    sno=request.data.get('sno')
    feed=Feed.objects.get(sno=int(sno))
    lk=FeedShare.objects.filter(user=request.user).filter(feed=feed)
    if len(lk)>0:
        lk.delete()
        feed.shares-=1
        feed.save()
    return Response({'response':'ok'},status=200)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def feedcomment(request):
    serializer=GNSerializers(data=request.data)
    sno=request.data.get('title')
    message=request.data.get('message')
    feed=Feed.objects.get(sno=int(sno))
    f=FeedComment(user=request.user,comment=message,feed=feed,username=request.user.username)
    f.save()
    return Response({'response':'ok'},status=200)



@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def getPractice(request):
    p=Practice.objects.all().values()
    pe=PracticeEnglish.objects.all().values()
    return Response({'practice':p,'practiceeng':pe},status=200)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def newfeed(request):
    parser_class=(FileUploadParser,)
    serializer = TestAllSerializer(data=request.data)
    query=request.data.get('query')
    queryimg=request.data.get('queryimage')
    c=Feed(user=request.user,username=request.user.username,captions=query,post=queryimg)
    c.save()
    return Response({'courses':'ok'},status=200)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def answer(request):
    serializer = asknewquerySerializers(data=request.data)
    day=int(request.data.get('video'))
    sno=request.data.get('query')
    pt=request.data.get('creater')
    dev=request.data.get('device')
    mqr=MegaquizResult.objects.filter(user=request.user)
    if len(mqr)>0:
        mq=MegaquizResult.objects.get(user=request.user)
        if (day) == 1:
            
            mq.day1+=str(sno)+'-'+pt+'#+#'
        if (day) == 2:
            if mq.day2 == None:
                mq.day2=str(sno)+'-'+pt+'#+#'
            else:
                mq.day2+=str(sno)+'-'+pt+'#+#'
        if (day) == 3:
            if mq.day3 == None:
                mq.day3=str(sno)+'-'+pt+'#+#'
            else:
                mq.day3+=str(sno)+'-'+pt+'#+#'
        if (day) == 4:
            if mq.day4 == None:
                mq.day4=str(sno)+'-'+pt+'#+#'
            else:
                mq.day4+=str(sno)+'-'+pt+'#+#'

        if (day) == 5:
            if mq.day5 == None:
                mq.day5=str(sno)+'-'+pt+'#+#'
            else:
                mq.day5+=str(sno)+'-'+pt+'#+#'

        if (day) ==6:
            if mq.day6 == None:
                mq.day6=str(sno)+'-'+pt+'#+#'
            else:
                mq.day6+=str(sno)+'-'+pt+'#+#'

        if (day) == 7:
            if mq.day7 == None:
                mq.day7=str(sno)+'-'+pt+'#+#'
            else:
                mq.day7+=str(sno)+'-'+pt+'#+#'

        mq.score+=int(pt.split('-')[1])
        mq.time+=int(pt.split('-')[0])
        mq.device=dev
        mq.save()
    else:
        if (day) == 1:
            mq=MegaquizResult(user=request.user,username=request.user.username,day1=str(sno)+'-'+pt+'#+#',score=int(pt.split('-')[1]),time=int(pt.split('-')[0]))
        if (day) == 2:
            mq=MegaquizResult(user=request.user,username=request.user.username,day2=str(sno)+'-'+pt+'#+#',score=int(pt.split('-')[1]),time=int(pt.split('-')[0]))
        if (day) == 3:
            mq=MegaquizResult(user=request.user,username=request.user.username,day3=str(sno)+'-'+pt+'#+#',score=int(pt.split('-')[1]),time=int(pt.split('-')[0]))
        if (day) == 4:
            mq=MegaquizResult(user=request.user,username=request.user.username,day4=str(sno)+'-'+pt+'#+#',score=int(pt.split('-')[1]),time=int(pt.split('-')[0]))
        if (day) == 5:
            mq=MegaquizResult(user=request.user,username=request.user.username,day5=str(sno)+'-'+pt+'#+#',score=int(pt.split('-')[1]),time=int(pt.split('-')[0]))
        if (day) == 6:
            mq=MegaquizResult(user=request.user,username=request.user.username,day6=str(sno)+'-'+pt+'#+#',score=int(pt.split('-')[1]),time=int(pt.split('-')[0]))
        if (day) == 7:
            mq=MegaquizResult(user=request.user,username=request.user.username,day7=str(sno)+'-'+pt+'#+#',score=int(pt.split('-')[1]),time=int(pt.split('-')[0]))
        mq.save()
    return Response({'status':'ok'},status=200)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def previousyp(request):
    user=User.objects.all().order_by('id').values()
    papers=PreviousPaper.objects.all().values()
    return Response({'status':papers,'user':user},status=200)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def storyviews(request):
    serializer = BookMarkSerializer(data=request.data)
    sno=request.data.get('sno')
    feed=Stories.objects.get(sno=int(sno))
    feed.views+=1
    feed.save()
    return Response({'response':'ok'},status=200)

@api_view(['POST', ])  
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def alerts(request):
    al=''
    user=request.user.id
    al=alert.objects.all().order_by('-sno')
    if len(alertrecieved.objects.filter(user=request.user,alert=al[0]))==0:
        ar=alertrecieved(user=request.user,alert=al[0])
        ar.save()
        return Response({'response':al.values(),'user':user},status=200)
    else:
        return Response({'response':[],'user':user},status=200)

