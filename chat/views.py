from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def course_chat_room(request, course_id):
    try:
        # retrieve course with given id
        course = request.user.courses_joined.get(id=course_id)
        print(course)
    except:
        # user is not in the course or course does not exist
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})