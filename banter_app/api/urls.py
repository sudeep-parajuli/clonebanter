from banterclone import urls
from django.urls import path, include
from banter_app.api.views import *

app_name = "createcontact"

urlpatterns = [
    path("create/", CreateContactView.as_view(), name = "createcontact")
]