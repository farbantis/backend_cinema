# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
# from rest_framework.decorators import api_view
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
# from rest_framework import generics
# from account.models import User
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from .models import Movie
# from .serializers import MovieSerializer
#
#
# class MovieSetPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100
#     page_query_param = 'page'
#
#
# class MoviesAPIView(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     pagination_class = MovieSetPagination
#
#     # @method_decorator(ensure_csrf_cookie, name='dispatch')
#     # def dispatch(self, *args, **kwargs):
#     #     return super(MoviesAPIView, self).dispatch(*args, **kwargs)
#
#
# # @api_view(['POST'])
# # def check_username_existence(request, check_user):
# #     try:
# #         #
# #         return Response(User.objects.filter(username=check_user).exists())
# #     except:
# #         return Response(False)
#
#
# # # Создаём класс RegistrUserView
# # class RegistrUserView(CreateAPIView):
# #     # Добавляем в queryset
# #     queryset = User.objects.all()
# #     # Добавляем serializer UserRegistrSerializer
# #     serializer_class = UserRegistrSerializer
# #     # Добавляем права доступа
# #     permission_classes = [AllowAny]
# #
# #     def post(self, request, *args, **kwargs):
# #         # Добавляем UserRegistrSerializer
# #         serializer = UserRegistrSerializer(data=request.data)
# #         # Создаём список data
# #         data = {}
# #         if serializer.is_valid():
# #             # Сохраняем нового пользователя
# #             serializer.save()
# #             # Добавляем в список значение ответа True
# #             data['response'] = True
# #             # Возвращаем что всё в порядке
# #             return Response(data, status=status.HTTP_200_OK)
# #         else:
# #             # Иначе Присваиваем data ошибку
# #             data = serializer.errors
# #         # Возвращаем ошибку
# #         return Response(data)
#
#
#
#
#
