from . import views
from django.urls import include, path

urlpatterns = [
    path('add_course', views.post_course, name='add_course'),
    path('<int:course_id>', views.get_delete_change_course_by_id, name='get_delete_change_course_by_id'),
    path('all_courses', views.get_all_courses, name='get_all_courses'),
    path('get_courses_by_title', views.get_courses_by_title, name='get_courses_by_title'),
    path('filter_courses_by_date', views.filter_courses_by_date, name='filter_courses_by_date'),
]