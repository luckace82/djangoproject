from  django.urls  import path
from .views import operation,result

urlpatterns=[
    path('',operation,name='home'),
    path('result',result,name='result')
]