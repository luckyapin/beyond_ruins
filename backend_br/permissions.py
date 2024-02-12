from rest_framework import permissions


# Ограничение к большинству запросов
class MyPermission(permissions.BasePermission):
    def has_permission(self, request, view):  # К нескольким экземплярам
        if request.method in permissions.SAFE_METHODS:  # Разрешаем все безопасные
            return True
        elif request.method == 'POST':  # Авторизованные могут добавлять
            return bool(request.user.is_authenticated)
        return False

    def has_object_permission(self, request, view, obj):  # К единичному
        if request.method in permissions.SAFE_METHODS:  # Разрешаем все безопасные
            return True
        return obj.user == request.user  # Создатель может делать со своим творением что-угодно

# Ограничение для таблицы User. Можно только смотреть, добавление - это регистрация
class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
