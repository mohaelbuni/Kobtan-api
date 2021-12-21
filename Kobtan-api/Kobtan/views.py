from django.http import HttpResponse
def homePageView(request):
  return HttpResponse('Kobtan Api running successfully, please go to /api/ to see api endpoints,and go to /admin/ if you want got to admin page but you need username and password contact with Abdulmohaimen Elbuni to give you credential')