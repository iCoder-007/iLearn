 
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url,include
urlpatterns = [
    path("",views.home,name="home"),
    path("teach1",views.Teach1,name="Teach1"),
    path('login', views.handleLogin,name="handleLogin"),
    path('logout', views.handleLogout,name="handleLogout"),
    path('signup', views.handleSignUp,name="handleSignUp"),
   
    path('contact', views.contact,name="contact"),
    path('about', views.about,name="about"),
    path('search', views.search,name="search"),
    path('addCourse', views.addCourse,name="addCourse"),
    path('homeTutor', views.homeTutor,name="homeTutor"),
    path('getStarted', views.getStarted,name="getStrated"),
    path('createCourse', views.createCourse,name="createCourse"),
    path('addVideos', views.addVideos,name="addVideos"),
    path('teachersignup', views.handleTeacherSignUp,name="handleTeacherSignUp"),
    path('saveCourse', views.saveCourse,name="saveCourse"),
    path('viewCourses', views.viewCourses,name="viewCourses"),
    path('get_viewCourses', views.get_viewCourses,name="get_viewCourses"),
    path('video', views.video,name="video"),
    path('get_cartItems', views.get_cartItems,name="get_cartItems"),
    path('addCart', views.addCart,name="addCart"),
    path('cart', views.CartItem,name="CartItem"),
    path('teacherProfile', views.teacherProfile,name="teacherProfile"),
    path('get_teacherProfile', views.get_teacherProfile,name="get_teacherProfile"),
    path('teacherPerformance', views.teacherPerformance,name="teacherPerformance"),
    path('previewCourse/<int:id>', views.previewCourse,name="previewCourse"),
    # path('editCourse/<int:id>', views.editCourse,name="editCourse"),
    path('deleteCourse/<int:id>', views.deleteCourse,name="deleteCourse"),
    path('buynow', views.buynow,name="buynow"),
    path('handleRequest/', views.handleRequest,name="handleRequest"),
    path('courseAdded', views.courseAdded,name="courseAdded"),
    path('myCourses', views.myCourses,name="myCourses"),
    path('watched', views.watched,name="watched"),
    path('courses/<str:slug>/<int:id>', views.previewmyCourses,name="previewmyCourses"),

]