from django.conf.urls import url
from basic import views


#this line is compulsory for template tagging
app_name='basic'

urlpatterns=[
     url('relative/',views.relativework,name='relativework'),
     url('other/',views.other,name='other'),
]
