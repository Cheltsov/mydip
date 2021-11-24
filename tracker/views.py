from django.shortcuts import render, redirect


# Create your views here.
def dashboard(request):
    if 'user' in request.session:
        return render(request, 'base/dashboard.html', {})
    else:
        return redirect('auth:auth')



