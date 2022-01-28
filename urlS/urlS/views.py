from django.shortcuts import render
import pyshorteners
from django.views import View

class url_shortener(View):
   def post(self, request):
      long_url = 'url' in request.POST and request.POST['url']
      pys = pyshorteners.Shortener()
      short_url = pys.tinyurl.short(long_url)
      return render(request,'index.html', context={'short_url':short_url,'long_url':long_url})

   def get(self, request):
      return render(request,'index.html')
