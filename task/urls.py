from django.urls import path
from task.views import import_data, get_data

urlpatterns = [
    path("api/import/", import_data, name="import_data"),
    path("api/<str:model_name>/", get_data, name="get_model_data"),
    path(
        "api/<str:model_name>/<int:model_id>/", get_data, name="get_specific_model_data"
    ),
]
