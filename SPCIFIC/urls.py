from django.urls import path
from SPCIFIC.views import *
app_name="specific"

urlpatterns=[
  path('spc_html3/',spc_html3,name='spc_html3'),
  path('spc_html4/',spc_html4,name='spc_html4')
]
