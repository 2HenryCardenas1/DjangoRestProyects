from django.urls import path
from users.API.views import RegisterView,UserView,ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    # Ruta para ver informacion del usuario
    path('auth/me', UserView.as_view()),
    #Actualizar contraseña
    path('auth/change-password/', ChangePasswordView.as_view()),
    # Ruta login con JWT
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view())

]
