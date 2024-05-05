from typing import Union, Optional, Annotated

from fastapi import FastAPI, Query, Path
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class Currency(str, Enum):
    rupee = "R"
    baht = "B"
    yen = "Y"

class Item(BaseModel):
    name: str
    price: float
    tax : Optional[float] = None
    description: Optional[str] = None # or str | None = None
    is_offer : Optional[bool] = None


@app.get("/")
async def read_root():
    return {"hello": "world"}

@app.get("/items/{item_id}")
async def read_item(item_id: Annotated[int, Path(title="The ID of the item to get")], 
                    q: Annotated[Optional[str], Query(max_length=50)] = None):
    """
    Example: localhost:8000/items/19?q=nineteen
    Note: we could declare q type as Optional[str]=None or Union[str, None] = None
    """
    return { "item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, **item.dict()}


@app.put("/item/copy/{item_id}")
async def copy_item(item_id: int, item: Item):
    item_data = {
        "name" : item.name,
        "price": item.price,
        "is_offer": item.is_offer

    }

    new_item : Item = Item(**item_data)

    return {"item_name": new_item.name, "item_id": item_id}

# api call example with predefined type
@app.put('/item/{currency}')
async def set_currency(currency: Currency, item: Item):
    return {"name": item.name, "currency": currency}


# declaering query param with multiple values
@app.get("/item/search")
def apply_filter(filters: Annotated[Union[list[str], None], Query()] = None):
    filter_obj = {"filters": filters}
    return filter_obj
