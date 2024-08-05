import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View

from ..model.Book import Book
from ..model.Author import Author
from ..dry.Book import dry_book


class BookView(View):
    def get(self, request):
        books = Book.objects.all()
        response = {[dry_book(book) for book in books]}
        return JsonResponse(response, status=200)

    def post(self, request):
        data = json.loads(request.body)
        try:
            author = Author.objects.get(id=data["author_id"])
        except ObjectDoesNotExist:
            return JsonResponse({"status": "Error", "error": "author object doesn't exist"}, status=400)
        if isinstance(data["book_name"], str):
            book_name = data["book_name"]
        else:
            return JsonResponse({"status": "Error", "error": "book_name must be string"}, status=400)
        if isinstance(data["pagination"], int):
            pagination = data["pagination"]
        else:
            return JsonResponse({"status": "Error", "error": "pagination must be integer"}, status=400)
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
        if "book_name" in data and isinstance(data["book_name"], str):
            book.name = data["book_name"]
        else:
            return JsonResponse({"status": "Error", "error": "book_name must be string"}, status=400)
        if "pagination" in data and isinstance(data["pagination"], int):
            book.pagination = data["pagination"]
        else:
            JsonResponse({"status": "Error", "error": "pagination must be integer"}, status=400)
        book.save()
        return JsonResponse({"status": "ok", "id": book.id}, status=200)

    def delete(self, request):
        book_id = request.GET.get("id")
        try:
            book = Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "Error", "error": "book object doesn't exist"}, status=400)
        book.delete()
        return JsonResponse({"status": "ok"}, status=200)
