import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View

from ..model.Book import Book
from ..model.Author import Author


class BookView(View):
    def get(self, request):
        books = Book.objects.all()
        print(books)
        data = []
        for book in books:
            data.append({
                "id": book.id,
                "author": {
                    "user": {
                        "username": book.author.user.username
                    },
                    "age": book.author.age,
                    "gender": book.author.gender
                },
                "name": book.name,
                "pagination": book.pagination
            })
        response = {
            "data": data
        }
        return JsonResponse(response, status=200)

    def post(self, request):
        data = json.loads(request.body)
        try:
            author = Author.objects.get(id=data["author_id"])
        except ObjectDoesNotExist:
            return JsonResponse({"status": "Error", "error": "author object doesn't exist"}, status=400)
        try:
            book_name = data["book_name"]
        except ValueError:
            return JsonResponse({"status": "Error", "error": "book name must be string"}, status=400)
        try:
            pagination = data["pagination"]
        except ValueError:
            JsonResponse({"status": "Error", "error": "pagination must be integer"}, status=400)
        book = Book.objects.create(
            author=author,
            name=book_name,
            pagination=pagination
        )
        return JsonResponse({"status": "ok", "id": book.id}, status=200)

    def patch(self, request):
        book_id = request.GET.get("id")
        try:
            book = Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "Error", "error": "book object doesn't exist"}, status=400)
        data = json.loads(request.body)
        if "book_name" in data:
            book.name = data["book_name"]
        if "pagination" in data:
            book.pagination = data["pagination"]
        book.save()
        return JsonResponse({"status": "ok", "id": book.id}, status=200)

    def delete(self,request):
        book_id = request.GET.get("id")
        try:
            book = Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "Error", "error": "book object doesn't exist"}, status=400)
        book.delete()
        return JsonResponse({"status": "ok"}, status=200)
