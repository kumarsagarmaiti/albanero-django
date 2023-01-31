import utils
from rest_framework.decorators import api_view
from django.http import HttpResponse

connection_handler = utils.create_connection("albanero-demo", "employees")


@api_view(["POST"])
def create_employee(request):
    if request.method == "POST":
        connection_handler.insert_one(request.data)
        return HttpResponse("success")
