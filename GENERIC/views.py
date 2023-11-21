from django.shortcuts import render

# Create your views here.
def gen_html1(request):
   return render(request,'gen_html1.html')
def gen_html2(request):
  return render(request,'gen_html2.html')