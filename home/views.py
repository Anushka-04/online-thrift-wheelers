from django.shortcuts import render

def index(request):
	return render(request,"index.html")

def carform(request):
	return render(request,"form.html")


