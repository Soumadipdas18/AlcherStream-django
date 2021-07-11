from django.urls import path
from . import views

urlpatterns = [
    path("", views.reviews, name="reviews"),
    path('all/<path:slug>', views.allreview, name="All Reviews"),
    path('postcomment/<path:slug>',views.postcomment,name='Post Comment'),
    path('delete/<path:slug>', views.deletereview, name="Delete Review"),
]