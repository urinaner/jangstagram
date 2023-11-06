from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
  def get(self, request):
    print("겟임")
    return render(request, "jangstagramtemp/main.html")
  
  def post(self, request):
    print("포스트임")
    return render(request, "jangstagramtemp/main.html")


 