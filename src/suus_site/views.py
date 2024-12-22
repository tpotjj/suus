from django.shortcuts import render
from django.views import View

HOME_PAGE_NAME = "home-page"

class HomePage(View):
    def get(self, request):
        return render(request, "home-page.html")