# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contact,Courses,Videos,TeacherProfile,MyCourses,WatchedVideos
# Register your models here.
admin.site.register(Contact),
admin.site.register(Courses),
admin.site.register(Videos),
admin.site.register(TeacherProfile),
admin.site.register(MyCourses),
admin.site.register(WatchedVideos),

