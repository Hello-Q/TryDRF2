from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from app01 import models, serializers
from rest_framework import generics
#
# @api_view(['GET', 'POST'])
# def publisher_list(request, format=None):
#     """
#     列出所有出版社，或者创建一个出版社
#     """
#     if request.method == 'GET':
#         queryset = models.Publisher.objects.all()
#         s = serializers.PublisherSerializer(queryset, many=True)
#         return Response(s.data)
#     if request.method == 'POST':
#         s = serializers.PublisherSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def publisher_detail(request, pk):
#     try:
#         publisher = serializers.Publisher.objects.get(pk=pk)
#     except serializers.Publisher.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         s = serializers.PublisherSerializer(publisher)
#         return Response(s.data)
#     elif request.method == 'PUT':
#         s = serializers.PublisherSerializer(publisher, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class PublisherList(APIView):
#     """
#     列出所有的出版社,或新建一个出版社
#     """
#
#     def get(self, request, format=None):
#         publisher = models.Publisher.objects.all()
#         s = serializers.PublisherSerializer(publisher, many=True)
#         return Response(s.data)
#
#     def post(self, request, format=None):
#         s = serializers.PublisherSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PublisherDetail(APIView):
#     """
#     获取一个查看、修改、删除视图
#     """
#     def get_object(self, pk):
#         try:
#             return models.Publisher.objects.get(pk=pk)
#         except models.Publisher.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = serializers.PublisherSerializer(publisher)
#         return Response(s.data)
#
#     def put(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = serializers.PublisherSerializer(publisher, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#
#     def delete(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#
# class PublisherList(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PublisherDetail(mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class PublisherList(generics.ListCreateAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)  # 权限控制

    # def post(self, request, *args, **kwargs):
    #     print(request.data)
    #     return self.post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(operator=self.request.user)


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)  # 权限控制

#
# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     书籍详情
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#

#
# class PublisherViewSet(viewsets.ModelViewSet):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (permissions.IsAuthenticated,)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'publisher': reverse('publisher-list', request=request, format=format),
#         'book': reverse('book-list', request=request, format=format)
#     })
