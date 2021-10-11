import random
import uuid

todo_list = [{"id": 54,
              "description": "Hello World",
              "status": 0}]


def insert_data(Description: str) -> None:

    todo_list.append({
        "id": uuid.uuid4(),
        "description": Description,
        "status": 0
    })


def update_data(Data_ID: int, Description: str, status: int) -> dict:
    for Data in todo_list:
        if Data["id"] == Data_ID:
            Data["description"] = Description
            Data["status"] = status
            return
    raise Exception("ID was not found please retry again")


def Get_Data() -> dict:
    if len(todo_list) == 0:
        raise Exception("No data inside the list")
    return todo_list
