from django.urls import path,re_path
from . import views
urlpatterns = [
    path("",views.index),
    path("login/",views.loginUser,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path("about/",views.about),
    path("create/",views.create),
    path("display/",views.display,name="display"),
    re_path(r'^delete_product/(?P<pk>[0-9]+)/$',views.delete,name="delete"),
    path("add-user/",views.addUser),
    path("edit/<int:id>",views.edit,name="edit"),
    path("update/<int:id>",views.update),
]
