from django.shortcuts import render

def testing(request):
	return render(request, 'testing/index.html')

def launch(request):
	return render(request, 'testing/launch.html')

def environment(request):
	return render(request, 'testing/test.html')

def ballistic(request):
	return render(request, 'testing/test.html')

def jet(request):
	return render(request, 'testing/jet.html')

def protection(request):
	return render(request, 'testing/test.html')

def impact(request):
	return render(request, 'testing/test.html')

def seismic(request):
	return render(request, 'testing/test.html')

def fluids(request):
	return render(request, 'testing/test.html')

def electromagnetic(request):
	return render(request, 'testing/test.html')

def reliability(request):
	return render(request, 'testing/test.html')

def acoustics(request):
	return render(request, 'testing/test.html')

def structural(request):
	return render(request, 'testing/test.html')

def engine(request):
	return render(request, 'testing/test.html')

def explosives(request):
	return render(request, 'testing/test.html')