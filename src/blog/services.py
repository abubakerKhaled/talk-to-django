from sentence_transformers import SentenceTransformer
from pgvector.django import CosineDistance
from django.db.models import F
from decouple import config
from django.apps import apps

EMEDDING_MODEL=config("EMEDDING_MODEL", default="multi-qa-distilbert-cos-v1")
EMEDDING_LENGTH=config("EMEDDING_LENGTH", default=768, cast=int)

model = SentenceTransformer(EMEDDING_MODEL)


def get_embedding(text):
    text = text.replace('\n', ' ').strip()
    return model.encode(text, clean_up_tokenization_spaces=False)


def get_query_embedding(text):
    # get_or_create Query Embedding model
    return get_embedding(text)

def search_posts(query, limit=5):
    BlogPost = apps.get_model(app_label='blog', model_name='BlogPost')
    query_embedding = get_query_embedding(query)
    qs = BlogPost.objects.annotate(
        distance = CosineDistance('embedding', query_embedding),
        similarity = 1 - F("distance")
        ).order_by("distance")[:limit]
    
    return qs