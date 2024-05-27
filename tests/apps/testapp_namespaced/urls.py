from django.urls import re_path as url
from django.http import HttpResponse


def testview(request):
    return HttpResponse()


app_name = "testapp_namespaced"

urlpatterns = [url(r"^$", testview, name="test_url_namespaced")]
