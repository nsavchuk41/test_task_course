from django.test import TestCase
from course_app.models import Course
from django.urls import reverse
from django.test import Client
import json

class CourseViewTest(TestCase):
          
    def test_view_post_course(self):
        response = self.client.post('/course/add_course', json.dumps({'auto_increment_id':1,'title':'adsfadsg', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")
        
        self.assertEqual(response.status_code, 200)

    def test_view_get_all_courses(self):
        self.client.post('/course/add_course', json.dumps({'title':'adsfadsg', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")
        self.client.post('/course/add_course', json.dumps({'title':'adsfadsg', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")
          
        response = self.client.get('/course/all_courses')
        
        self.assertEqual(response.status_code, 200)
    
    def test_view_get_course_by_id(self):
        self.client.post('/course/add_course', json.dumps({'title':'adsfadsg', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")

        response = self.client.get('/course/1')
        self.assertEqual(response.status_code, 200)
        
    def test_view_delete_course_by_id(self):
        self.client.post('/course/add_course', json.dumps({'title':'adsfadsg', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")
   
        response = self.client.delete('/course/1')

        self.assertEqual(response.status_code, 200)

    def test_view_put_course_by_id(self):
        self.client.post('/course/add_course', json.dumps({'title':'adsfadsg', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")
 
        response = self.client.put('/course/1', json.dumps({'title':'Project', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")
        
        self.assertEqual(response.status_code, 200)    

    def test_view_filter_courses_by_title(self):
        self.client.post('/course/add_course', json.dumps({'title':'abc', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")
        self.client.post('/course/add_course', json.dumps({'title':'efg', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")
        
        response = self.client.generic('GET', '/course/get_courses_by_title', json.dumps({"course_title_contain":"a"}))
                
        self.assertEqual(response.status_code, 200)

    def test_view_filter_courses_by_date(self):
        self.client.post('/course/add_course', json.dumps({'title':'New title', 'start_date':'2020-01-01', 'end_date':'2020-05-02','lecture_number':20}), content_type="application/json")
        self.client.post('/course/add_course', json.dumps({'title':'abc', 'start_date':'2018-01-01', 'end_date':'2022-05-02','lecture_number':20}), content_type="application/json")

        response = self.client.generic('GET', '/course/filter_courses_by_date', json.dumps({"start_date":"2019-01-01","end_date":"2021-12-12"}))
                
        self.assertEqual(response.status_code, 200)