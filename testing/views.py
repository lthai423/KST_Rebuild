from django.shortcuts import render

def environmental(request):
	return render(request, 'testing/environmental.html')

def ballistic(request):
	return render(request, 'testing/ballistic.html')

def jet(request):
	return render(request, 'testing/jet.html')