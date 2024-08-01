import os
import django
from django.forms import model_to_dict

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoDjango.settings')
django.setup()


from fonluz.models import Article


data = []
for article in Article.objects.all():

    data.append(article.toJSON())

print(data)






