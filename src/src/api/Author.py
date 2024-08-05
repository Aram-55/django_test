import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from ..model.Author import Author
from ..dry.Author import dry_author


class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        response = {"data": [dry_author(author) for author in authors]}
        return JsonResponse(response, status=200)

    def post(self, request):
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=data["user_id"])  # how I know user_id and where can I find it out on admin page?
        except ObjectDoesNotExist:
            return JsonResponse({"status": "Error", "Error": "user object doesn't exist"}, status=400)
        if isinstance(data["age"], int):
            age = data["age"]
        else:
            return JsonResponse({"status": "Error", "Error": "age must be integer"}, status=400)
        if data["gender"] in (1, 2):
            gender = data["gender"]
        else:
            return JsonResponse({"status": "Error", "Error": "gender must be 1 or 2"}, status=400)

        author = Author.objects.create(
            user=user,
            age=age,
            gender=gender
        )
        return JsonResponse({"status": "ok", "id": author.id}, status=200)

    def patch(self, request):
        author_id = request.GET.get("id")  # GET-what is it?
        try:
            author = Author.objects.get(id=author_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "Error", "Error": "author object doesn't exist"}, status=400)
        data = json.loads(request.body)
        if "age" in data and isinstance(data["age"], int):
            author.age = data["age"]
        else:
            return JsonResponse({"status": "Error", "Error": "age must be integer"}, status=400)
        if "gender" in data and data["gender"] in (1, 2):
            author.gender = data["gender"]
        else:
            return JsonResponse({"status": "Error", "Error": "gender must be 1 or 2"}, status=400)
        author.save()
        return JsonResponse({"status": "ok", "id": author.id}, status=200)

    def delete(self, request):
        author_id = request.GET.get("id")
        try:
            author = Author.objects.get(id=author_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "Error", "Error": "author object doesn't exist"}, status=400)
        author.delete()
        return JsonResponse({"status": "ok", }, status=200)
