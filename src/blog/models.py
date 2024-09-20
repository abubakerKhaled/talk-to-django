from django.db import models
from pgvector.django import VectorField
from sentence_transformers import SentenceTransformer


EMBEDDING_MODEL = 'all-mpnet-base-v2'
EMBEDDING_LENGTH = 768

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMBEDDING_LENGTH, blank=True, null=True)