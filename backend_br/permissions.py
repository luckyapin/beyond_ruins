from rest_framework import permissions


# Ограничение к большинству запросов
class MyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):  # К единичному
        if request.user.is_superuser:  # Проверяем, является ли пользователь суперпользователем
            return True
        if request.method in permissions.SAFE_METHODS:  # Разрешаем все безопасные
            return True
        return obj.userId == request.user  # Создатель может делать со своим творением что-угодно

    def has_permission(self, request, view):  # К нескольким экземплярам
        if request.user.is_superuser:  # Проверяем, является ли пользователь суперпользователем
            return True
        if request.method in permissions.SAFE_METHODS:  # Разрешаем все безопасные
            return True
        return bool(request.user.is_authenticated)




# Ограничение для таблицы User. Можно только смотреть, добавление - это регистрация
class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:  # Проверяем, является ли пользователь суперпользователем
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:  # Проверяем, является ли пользователь суперпользователем
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
