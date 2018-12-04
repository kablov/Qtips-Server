from django.contrib import admin
from django.urls import path, include
import api
from api.views import tip_payment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('<int:id>/pay/', tip_payment.TipPaymentView.as_view()),
]
