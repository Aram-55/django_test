import json

from django.http import JsonResponse
from django.views.generic import View

from ..model.Author import Author


class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        data = []
        for author in authors:
            data.append({
                "id": author.id,
                "user": author.user,
                "age": author.age,
                "gender": author.gender
            })
        return JsonResponse({"status": "ok", "id": author.id}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        author = Author.objects.create(
            user=data.user,
            age=data.age,
            gender=data.gender,
        )
        return JsonResponse({"status": "ok", "id": author.id}, status=200)

    def patch(self, request):
        author_id = request.Get.get("id")
        author = Author.objects.get(id=author_id)
        data = json.loads(request.body)
        if "age" in data:
            author.age = data["age"]
        if "gender" in data:
            author.gender = data["gender"]

        author.save()
        return JsonResponse({"status": "ok", "id": author.id}, status=200)

    def delete(self, request):
        author_id = request.Get.get("id")
        author = Author.objects.get(id=author_id)
        author.delete()
        return JsonResponse({"status": "ok", "id": author.id}, status=200)
