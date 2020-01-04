from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_fun(request):
	'''
	print("home fun get hit")
	resp = """
	<html>
	<body>
	<h1>HELLO WORLD</h1>
	</body>
	</html>
	"""
	'''
	#return HttpResponse("this is home")
	#return HttpResponse(resp)
	return render(request, "home.html")