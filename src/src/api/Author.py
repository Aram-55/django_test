import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from ..model.Author import Author


class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        data = []
        for author in authors:
            data.append({
                "id": author.id,
                "user": {
                    "username": author.user.username,
                    "full_name": " ".join([author.user.first_name, author.user.last_name])
                },
                "age": author.age,
                "gender": author.gender
            })

        response = {
            "data": data
        }
        return JsonResponse(response, status=200)

    def post(self, request):
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=data["user_id"])  # how I know user_id and where can I find it out on admin page?
        except ObjectDoesNotExist:
            return JsonResponse({"status": "Error", "Error": "user object doesn't exist"}, status=400)
        try:
            age = data["age"]
        except ValueError:
            return JsonResponse({"status": "Error", "Error": "age must be integer"},status=400)
        if data["gender"] == "Male" or "Female":
            gender = data["gender"]
        else:
            try:
                gender = data["gender"]
            except ValueError:
                return JsonResponse({"status": "Error", "Error": "gender must be 'Male' or 'Female"},status=400)

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
        if "age" in data:
            try:
                author.age = data["age"]
            except ValueError:
                return JsonResponse({"status": "Error", "Error": "age must be integer"},status=400)
        if "gender" in data:
            if data["gender"] == "Male" or "Female":
                author.gender = data["gender"]
            else:
                try:
                    author.gender = data["gender"]
                except ValueError:
                    return JsonResponse({"status": "Error", "Error": "gender must be 'Male' or 'Female"},status=400)
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
