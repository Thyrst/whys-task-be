# whys-task-be

### Setup

0. You need `rye` installed (https://rye.astral.sh/guide/installation/)
1. `rye sync`
2. `source .venv/bin/activate`
3. `python manage.py migrate`

### Run

`python manage.py runserver`

### Usage

Import data:

```bash
curl -X POST http://localhost:8000/api/import/ \
     -H "Content-Type: application/json" \
     -d '[
      {
        "Attribute": {
          "id": 1,
          "nazev_atributu_id": 1,
          "hodnota_atributu_id": 1
        }
      },
      {
        "AttributeName": {
          "id": 1,
          "nazev": "Barva"
        }
      },
      {
        "AttributeValue": {
          "id": 1,
          "hodnota": "modrá"
        }
      }
    ]'
```

Query data:
```bash
curl http://localhost:8000/api/attributes/
```

or

```bash
curl http://localhost:8000/api/attributes/1/
```

Browsable API:

You can also browse the API to check imported resources here: http://localhost:8000/api/