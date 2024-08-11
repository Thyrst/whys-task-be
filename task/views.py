import json
from django.http import JsonResponse, HttpResponse
from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB("db.json")


def import_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            for item in data:
                for model, fields in item.items():
                    table = db.table(model)
                    if "id" in fields:
                        doc_id = fields["id"]
                        document = Document(fields, doc_id)
                        table.upsert(document)
                    else:
                        return JsonResponse(
                            {"error": 'Missing "id" in fields'}, status=400
                        )
            return HttpResponse(status=204)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return HttpResponse(status=405)


def get_data(request, model_name, model_id=None):
    if not model_name in db.tables() or model_id == 0:
        return HttpResponse(status=404)
    table = db.table(model_name)
    if model_id:
        result = table.get(doc_id=model_id)
        if result:
            return JsonResponse(result)
        else:
            return HttpResponse(status=404)
    else:
        results = table.all()
        return JsonResponse(results, safe=False)
