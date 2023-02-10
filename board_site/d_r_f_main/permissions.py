from rest_framework import permissions
# мы можем испльзовать тоько has_permission
# и has_object_permission


# # можно указать дефолтные ограничения в settings.py
# REST_FRAMEWORK = {
#     "(. . .):[]",
#
#
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.IsAuthenticated"
#
# }


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        # проверка является ли пользователь Админом
        # эта строка взята из IsAdminUser
        # поясение:
        # вернуть булевое значение(это пользователь и
        # это пользователь из персонала(.is_staff))
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


