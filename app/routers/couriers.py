from fastapi import APIRouter, Query
from typing import Union
from typing_extensions import Annotated

router = APIRouter()


# Регистрация курьера в системе. Поля:

# name: str - имя курьера
# districts: list[str] - массив районов. Заказ и курьер должны иметь общий район

@router.post("/")
async def read_item(id: int):
    return {"item_id": id, "name": "first"}

# получение информации о всех курьеров системе. Ожидаемые поля:

# id: UUID или int - уникальный идентификатор. Можно использовать uuid или обычный автоинкремент
# name: str - имя курьера

@router.get("/")
def items():
    return [{"id": 1, "name": "first"}]

# Получение подробной информации о курьере

# id: UUID | int - уникальный идентификатор. Можно использовать uuid или обычный автоинкремент
# name: str - имя курьера
# active_order: dict - информация об активном заказе. Если такого нет, возвращать None

# {"order_id": ид заказа,
# "order_name": имя заказа
# }
# avg_order_complete_time: datetime - среднее время отработки заказа
# avg_day_orders: int - среднее колво заверешенных заказов в день


@router.get("/{id}")
def read_item(id: int):
    return {"item_id": id, "name": "first"}



