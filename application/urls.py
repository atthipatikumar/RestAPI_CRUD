'''from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from application import views

app_name = "user_details"

urlpatterns = [
    url(r'^user_details/', views.details_list),
    url(r'^user/<int:pk>', views.detail_view)


]
urlpatterns = format_suffix_patterns(urlpatterns)
'''
