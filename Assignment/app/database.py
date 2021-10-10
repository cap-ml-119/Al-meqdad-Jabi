import random
import uuid

todo_list = []


def insert_data(Description: str):

    todo_list.append({
        "id": uuid.uuid4(),
        "description": Description
    })
