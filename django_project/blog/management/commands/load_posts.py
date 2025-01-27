import json
from django.core.management.base import BaseCommand
from blog.models import Post
class Command(BaseCommand):
    help = 'Load posts from posts.json'

    def handle(self, *args, **kwargs):

        try:
            with open('posts.json', 'r') as file:
                posts_data = json.load(file)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR("The file 'posts.json' was not found."))
            return
        except json.JSONDecodeError:
            self.stderr.write(self.style.ERROR("Error decoding JSON. Please check the file format."))
            return

        # Iterate through the JSON data and create posts
        for post in posts_data:
            try:
                Post.objects.create(
                    title=post['title'],
                    content=post['content'],
                    author_id=post['user_id'],
                )
                self.stdout.write(self.style.SUCCESS(f"Post '{post['title']}' added successfully."))
            except KeyError as e:
                self.stderr.write(self.style.ERROR(f"Missing key in JSON: {e}"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error creating post: {e}"))

        self.stdout.write(self.style.SUCCESS('All posts loaded successfully!'))
