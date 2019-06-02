from django.contrib import admin
from django.urls import path, include
import api
from api.views import tip_payment, web


handler404 = 'api.views.web.error'
handler500 = 'api.views.web.error'


urlpatterns = [
    path('', web.mainpage),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('<int:id>/', tip_payment.payment_page),
    path('<int:id>/pay/', tip_payment.TipPaymentView.as_view()),
    path('testpay/', tip_payment.test_payment_page),
    path('testpay/pay/', tip_payment.TestTipPaymentView.as_view()),
    path('thanks/', web.thanks),
    path('terms/', web.terms),
    path('privacy/', web.privacy),
]
