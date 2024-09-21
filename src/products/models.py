from django.db import models
from pgvector.django import VectorField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

EMBEDDING_LENGTH = 768

class Embedding(models.Model):
    embedding = VectorField(dimensions=EMBEDDING_LENGTH, blank=True, null=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')


class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    embedding = GenericRelation(Embedding)
    timestamp = models.DateTimeField(auto_now_add=True)
    can_delete = models.BooleanField(default=False, help_text='Use in jupyter notebooks')

        
    def get_embedding_text_raw(self):
        return self.content