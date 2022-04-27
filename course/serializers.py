from rest_framework import serializers

from .models import Course, Lesson, Comment, Category, Quiz

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description', 'get_image')

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description', 'long_description')

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'slug', 'lesson_type', 'short_description', 'long_description', 'youtube_id')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'created_at')

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'lesson_id', 'question', 'answer', 'op1', 'op2', 'op3')