from django.shortcuts import render

def tech(request):
	return render(request, 'community/tech.html')

def education(request):
	return render(request, 'community/education.html')

def econ(request):
	return render(request, 'community/econ.html')