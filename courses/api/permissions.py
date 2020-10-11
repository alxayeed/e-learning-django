from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    """
    Custom Instance-level permission to ensure that
    students can access the contents of the the courses they enrolled
    """

    def has_object_permission(self, request, view, obj):
        """
        checking if the current user are in the stidents list of the obj(course)
        """
        return obj.students.filter(id=request.user.id).exists()
