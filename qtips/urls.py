from django.contrib import admin
from django.urls import path, include
from api.views import tip_payment, web


handler404 = 'api.views.web.error_404_view'
handler500 = 'api.views.web.error_500_view'


urlpatterns = [
    path('', web.mainpage),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('testpayment/', tip_payment.TestTipPaymentView.as_view(),
         name="test_tip_payment"),
    path('thanks/', web.thanks, name="thanks"),
    path('terms/', web.terms, name="terms"),
    path('privacy/', web.privacy, name="privacy"),
    path('<int:id>/', tip_payment.TipPaymentView.as_view(), name="tip_payment"),
]
