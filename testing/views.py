from django.shortcuts import render

def testing(request):
	return render(request, 'testing/index.html')

def launch(request):
	return render(request, 'testing/launch.html')

def environment(request):
	return render(request, 'testing/environment.html')

def ballistic(request):
	return render(request, 'testing/ballistic.html')

def jet(request):
	return render(request, 'testing/jet.html')

def protection(request):
	return render(request, 'testing/protection.html')

def impact(request):
	return render(request, 'testing/impact.html')

def seismic(request):
	return render(request, 'testing/seismic.html')

def fluids(request):
	return render(request, 'testing/fluids.html')

def electromagnetic(request):
	return render(request, 'testing/electromagnetic.html')

def reliability(request):
	return render(request, 'testing/reliability.html')

def acoustics(request):
	return render(request, 'testing/acoustics.html')

def structural(request):
	return render(request, 'testing/structural.html')

def engine(request):
	return render(request, 'testing/engine.html')

def explosives(request):
	return render(request, 'testing/explosives.html')

def technologies(request):
	return render(request, 'testing/technologies.html')