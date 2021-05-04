import json 
from django.shortcuts import render
from django.http import HttpResponse
from course_app.models import Course
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import QueryDict
import datetime 
@require_http_methods(['POST'])
def post_course(request):
    """Post new course to database

    Args:
        request (HttpRequest): Request to this endpoint

    Returns:
        JsonResponse: Response in json format with status code and details
    """    
    
    try:
        course = Course()
        body_unicode = request.body.decode('utf-8')
         
        body = json.loads(body_unicode)

        course_title = body.get('title').strip()
        course.title = course_title
            
        course_start_date = body.get('start_date').strip()

        course.start_date = course_start_date

        course_end_date = body.get('end_date').strip()
        course.end_date = course_end_date

        course_lecture_number = body.get('lecture_number')
        course.lecture_number = course_lecture_number

        course.save()
        return JsonResponse({
                'status_code' : 200, 
                'details': 'The course was posted succesfully!'
                },status=200)
    except Exception as e:
        return JsonResponse({
                'status_code' : 200, 
                'details': f'The cources was not added! {e.__repr__()}'
                },status=200)
    

@require_http_methods(['PUT','GET', 'DELETE'])
def get_delete_change_course_by_id(request, course_id):
    """Gets, deletes or changes course details by its id in database

    Args:
        request (HttpRequest): Request to django server
        course_id (int): Course id

    Returns:
        JsonResponse: Response with status_code and data or details of error
    """
    if request.method == 'GET':
        try:
            course = Course.objects.get(pk = course_id)
            return JsonResponse({
                    'status_code' : 200,
                    'data' : {
                        'course_title' : course.title, 
                        'course_start_date' : course.start_date, 
                        'course_end_date': course.end_date,
                        'course_lecture_number': course.lecture_number
                    }
                    },status=200)
        except Course.DoesNotExist:
            return JsonResponse({
                'status_code' : 404,
                'details' : "Course does not exist!"
                },status=404)

    elif request.method == 'DELETE':
        try:
            course = Course.objects.get(pk = course_id)
            course.delete()
            return JsonResponse({
                    'status_code' : 200,
                    'details' : 'Course deleted!'
                    },status=200)
        except:
            return JsonResponse({
                    'status_code' : 404,
                    'details' : 'Course does not exist!'
                    },status=404)

    elif request.method == 'PUT':
        try:
  
            
            body_unicode = request.body.decode('utf-8')
         
            body = json.loads(body_unicode)
            
            course = Course.objects.get(pk = course_id)
            
            course_title = body.get('title').strip()
            course.title = course_title
            
            course_start_date = body.get('start_date').strip()

            course.start_date = course_start_date

            course_end_date = body.get('end_date').strip()
            course.end_date = course_end_date

            course_lecture_number = body.get('lecture_number')
            course.lecture_number = course_lecture_number

            course.save()
            return JsonResponse({
                            'status_code' : 200,
                            'details' : 'Course changed!'
                            },status=200)
        except Exception as e:
            return JsonResponse({
                        'status_code' : 404,
                        'details' : f'Course does not exist!{e.__repr__()}'
                        },status=404)

@require_http_methods(['GET'])
def get_all_courses(request):
    """Return all courses from database

    Args:
        request (HttpRequest): Request

    Returns:
        JsonResponse: Response in json format
    """    
    courses = Course.objects.all()
    response_data = []
    for course in courses:
            response_data.append({
                'course_title' : course.title, 
                'course_start_date' : course.start_date, 
                'course_end_date': course.end_date,
                'course_lecture_number': course.lecture_number
                })
    return JsonResponse({
            'status_code' : 200, 
            'data' : response_data
            }, status=200)

@require_http_methods(['GET'])
def get_courses_by_title(request):
    """Get courses by part of title

    Args:
        request (HttpRequest): Request to endpoint

    Returns:
        JsonResponse: Response with jsons 
    """    
    body_unicode = request.body.decode('utf-8')
         
    body = json.loads(body_unicode)
    courses = Course.objects.filter(title__contains = body.get('course_title_contain'))
    response_data = []
    for course in courses:
            response_data.append({
                'course_title' : course.title, 
                'course_start_date' : course.start_date, 
                'course_end_date': course.end_date,
                'course_lecture_number': course.lecture_number
                })
    return JsonResponse({
        'status_code' : 200, 
        'data' : response_data
        }, status=200)


@require_http_methods(['GET'])
def filter_courses_by_date(request):
    """Filter courses by start and end date

    Args:
        request (HttpRequest): Request to endpoint

    Returns:
        JsonResponse: Response with json
    """    
    try:
        body_unicode = request.body.decode('utf-8')
            
        body = json.loads(body_unicode)

        start_date = body.get('start_date')
        end_date = body.get('end_date')
        if not start_date and end_date:
            end_date_parsed = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            courses = Course.objects.filter(end_date__lte = end_date_parsed)
            
        elif start_date and not end_date:
            start_date_parsed = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            courses = Course.objects.filter(end_date__gte = start_date_parsed)

        elif start_date and end_date:
            start_date_parsed = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date_parsed = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            courses = Course.objects.filter(end_date__gte = start_date_parsed, start_date__lte = end_date_parsed)
        else:
            courses = []
        response_data = []
        for course in courses:
            response_data.append({
                    'course_title' : course.title, 
                    'course_start_date' : course.start_date, 
                    'course_end_date': course.end_date,
                    'course_lecture_number': course.lecture_number
                    })
        return JsonResponse({
            'status_code' : 200, 
            'data' : response_data
            }, status=200)
    except Exception as e:
        return JsonResponse({
            'status_code' : 405, 
            'detail' : f'Wrong request format! {e.__repr__()}'
            }, status=405)