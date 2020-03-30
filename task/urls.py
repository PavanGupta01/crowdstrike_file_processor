from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^(?P<task_id>[\w\-]+)/$',
        views.TaskView.as_view(),
        name='task',
        ),
    url(r'^$',
        views.TaskView.as_view(),
        name='task',
        )
]