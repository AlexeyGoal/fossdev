
Три микросервиса в отдельных Docker-контейнерах:


## Product Service

Хранит данные о товарах и предоставляет информацию по запросу.

{
    "id": "pencil",
    "name": "Pencil",
    "price": 1.50,
    "available": true
}

## Oreder Service 

Принимает запрос на создание заказа

Получает данные о товаре из Product Service

Запрашивает расчёт скидки из Discount Service

Подсчитывает итоговую стоимость

Возвращает клиенту результат

Запрос:

POST /orders
{
    "product_id": "notebook",
    "quantity": 15,
    "promo_code": "STUDENT10"
}

Ответ:

{
    "product_id": "notebook",
    "quantity": 15,
    "unit_price": 4.20,
    "subtotal": 63.00,
    "discount_percent": 15.0,
    "discount_reason": "Wholesale discount for ordering 10+ items",
    "discount_amount": 9.45,
    "total": 53.55
}


## Discount Service 

Применяет правила для скидок. 

Количество ≥ 10 -> скидка 15%

Количество ≥ 5 -> скидка 5% 

Цена товара > 100 -> скидка 3% 
