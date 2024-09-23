from django.db import models
from pgvector.django import VectorField

from . import services
EMBEDDING_LENGTH=services.EMEDDING_LENGTH

# https://platform.openai.com/docs/guides/embeddings/embedding-models
EMBEDDING_LENGTH = 768

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    _content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMBEDDING_LENGTH, blank=True, null=True)
    can_delete = models.BooleanField(default=False, help_text='Use in jupyter notebooks')


    def get_embedding_text_raw(self):
        return self.content
    

    def save(self, *args, **kwargs):
        has_changed = False
        if self._content != self.content:
            has_changed = True
            self._changed = self.content
        if (self.embedding is None) or has_changed == True:
            raw_embedding_text = self.get_embedding_text_raw()
            if raw_embedding_text is not None:
                self.embedding = services.get_embedding(raw_embedding_text)
        super().save(*args, **kwargs)
    