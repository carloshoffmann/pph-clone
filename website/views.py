from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
#from django.shortcuts import render_to_response

# Create your views here.
def home(request):
   
   return render(request, 'base.html', {
      'title': 'RRHH Manager',


   })


