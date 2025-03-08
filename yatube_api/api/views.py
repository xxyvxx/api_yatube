from rest_framework import viewsets, permissions, status
from posts.models import Post, Group, Comment
from rest_framework.response import Response
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        # Проверяем, является ли текущий пользователь автором поста
        if post.author != request.user:
            return Response({'detail': 'У вас нет прав'},
                            status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        post = self.get_object()
        # Проверяем, является ли текущий пользователь автором поста
        if post.author != request.user:
            return Response({'detail': 'У вас нет прав '},
                            status=status.HTTP_403_FORBIDDEN)

        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        # Проверяем, является ли текущий пользователь автором поста
        if post.author != request.user:
            return Response({'detail': 'У вас нет прав'},
                            status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=post_id)

    def get_serializer_context(self):
        return {'request': self.request, 'post_id': self.kwargs['post_id']}

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response({'detail': 'У вас нет прав'},
                            status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response({'detail': 'У вас нет прав '},
                            status=status.HTTP_403_FORBIDDEN)

        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response({'detail': 'У вас нет прав '},
                            status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)
