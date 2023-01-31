import utils
from rest_framework.decorators import api_view
from django.http import HttpResponse
from bson.objectid import ObjectId

connection_handler = utils.create_connection("albanero-demo", "employees")


@api_view(["POST"])
def create_employee(request):
    connection_handler.insert_one(request.data)
    return HttpResponse("success")


@api_view(["GET"])
def get_employee(request):
    employee_docs = connection_handler.find()
    return HttpResponse(employee_docs)


@api_view(["GET", "PUT", "DELETE"])
def employee(request, employee_id):
    converted_id = ObjectId(employee_id)
    if request.method == "GET":
        employee_docs = HttpResponse(
            list(connection_handler.find({"_id": converted_id}, {"_id": 0}))
        )
        employee_docs["Content-Type"] = "application/json"
        return employee_docs
