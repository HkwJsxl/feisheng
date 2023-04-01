from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from rest_framework.filters import OrderingFilter
from django_filters import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_haystack.filters import HaystackFilter
from drf_haystack.generics import HaystackGenericAPIView

from .models import CourseDirection, CourseCategory, Course
from .serializers import (
    CourseDirectionModelSerializer, CourseCategoryModelSerializer, CourseInfoModelSerializer,
    CourseIndexHaystackSerializer
)

from mixins import ReListModelMixin, ReRetrieveModelMixin
from paginations import RePageNumberPagination


class CourseDirectionGenericAPIView(GenericViewSet, ReListModelMixin):
    """学习方向"""
    queryset = CourseDirection.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseDirectionModelSerializer
    pagination_class = None


class CourseCategoryFilterSet(FilterSet):
    """
    获取方向下的全部分类
    http://127.0.0.1:8000/course/category/?direction=10
    """
    direction = filters.CharFilter(field_name='direction', label='课程分类名称')

    class Meta:
        model = CourseCategory
        fields = ('direction',)


class CourseCategoryGenericAPIView(GenericViewSet, ReListModelMixin):
    """课程分类"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CourseCategoryFilterSet
    pagination_class = None

    queryset = CourseCategory.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseCategoryModelSerializer


class CourseInfoFilterSet(FilterSet):
    """
    课程列表筛选
    http://127.0.0.1:8000/course/
    http://127.0.0.1:8000/course/?direction=1&category=2
    """
    direction = filters.CharFilter(field_name='direction', label='课程方向')
    category = filters.CharFilter(field_name='category', label='课程分类')

    class Meta:
        model = Course
        fields = ("direction", "category",)


class CourseInfoGenericAPIView(GenericViewSet, ReListModelMixin):
    """
    课程列表接口
    排序：http://127.0.0.1:8000/course/?ordering=-students
    分页：http://127.0.0.1:8000/course/?page=2&size=2
    """
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CourseInfoFilterSet
    ordering_fields = ('id', 'students', 'orders')
    pagination_class = RePageNumberPagination

    queryset = Course.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseInfoModelSerializer


class CourseSearchViewSet(ReRetrieveModelMixin, ReListModelMixin, ViewSetMixin, HaystackGenericAPIView):
    """课程信息全文搜索视图类"""
    # 指定本次搜索的最终真实数据的保存模型
    index_models = [Course]
    serializer_class = CourseIndexHaystackSerializer
    filter_backends = [OrderingFilter, HaystackFilter]
    ordering_fields = ('id', 'students', 'orders')
    pagination_class = RePageNumberPagination
