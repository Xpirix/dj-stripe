"""
Represents protected content
"""

from django.urls import re_path as url
from django.http import HttpResponse


def testview(request):
    return HttpResponse()


urlpatterns = [url(r"^$", testview, name="test_url_content")]
