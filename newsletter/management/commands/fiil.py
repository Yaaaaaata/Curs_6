from django.core.management import BaseCommand
import json

from blog.views import BlogPost


class Command(BaseCommand):
    def handle(self, *args, **options):
        BlogPost.objects.all().delete()

        with open('data.json') as file:
            data = json.load(file)

        for item in data:
            category = BlogPost(name=item['name'])
            category.save()
