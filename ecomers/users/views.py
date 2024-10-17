from django.shortcuts import render

# Create your views here.

# Vista para la página de administración de usuarios
def user_admin(request):
    return render(request, 'usuarios/admin_users.html', {})