from django.contrib import admin
from django.urls import path, include
from api.views import tip_payment, web


handler404 = 'api.views.web.error_404_view'
handler500 = 'api.views.web.error_500_view'


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
