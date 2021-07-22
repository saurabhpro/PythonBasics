```bash
(venv) ➜  django-rest-first git:(master) ✗ django-admin startproject demo  
```


```bash
curl --location --request POST 'http://127.0.0.1:8000/api/v1/products/new' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Bislery",
    "description": "this is refreshing",
    "price": 99,
    "sale_start": "2021-06-30T00:00Z",
    "sale_end": "2021-07-31T00:00Z"
}'
```

mock output
```json
{
    "id": 9,
    "name": "Bislery",
    "description": "this is refreshing",
    "price": 99.0,
    "sale_start": "2021-06-30T00:00:00Z",
    "sale_end": "2021-07-31T00:00:00Z",
    "is_on_sale": true,
    "current_price": 89.1
}
```