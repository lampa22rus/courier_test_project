from fastapi import APIRouter

router = APIRouter()


# Публикация заказа в системе с полями:

# name: str - имя заказа
# district: str - район заказа.

# В случае, если удалось найти подходящего курьера, запрос должен вернуть order_id (ид заказа) и courier_id( ид курьера). Если подходящего курьера нет, то запрос должен вернуть ошибку.


@router.post("/")
async def read_item(id: int):
    return {"item_id": id, "name": "first"}


# 5) GET /order/{id}

# Получение информации о заказе

# courier_id: UUID | int
# status: int - статус заказа. 1 - в работе, 2 - завершен

@router.get("/{id}")
def read_item(id: int):
    return {"item_id": id, "name": "first"}


# 6) POST /order/{id}

# Завершить заказ. Должен вернуть ошибку если заказ уже завершен или такого заказа нет

@router.put("/{id}")
async def read_item(id: int):
    return {"item_id": id, "name": "first"}