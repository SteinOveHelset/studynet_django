from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Activity

from course.serializers import CourseListSerializer

@api_view(['GET'])
def get_active_courses(request):
    courses = []

    for activity in request.user.activities.all():
        if activity.status == activity.STARTED and activity.course not in courses:
            courses.append(activity.course)
    
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)