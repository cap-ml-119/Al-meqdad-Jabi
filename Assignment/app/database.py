import uuid

todo_list = []


def insert_data(Description: str) -> None:
    """[A function that is responsible for inserting data into our list by
    adding a new descrption and generating a unieq
    id for each item in that list using the library uuid]

    Args:
    takes the paremeter desciption as an
    str and inserted to the list
    with the uniqe id and fixed value of status which is 0
    """
    todo_list.append({
        "id": str(uuid.uuid4()),
        "description": Description,
        "status": 0
    })


def update_data(Data_ID, Description: str) -> None:
    """[A function that is responsible for Updating The data By ID
    it takes the ID from the api as an argument beisde the Description
    and search the list for that id and if found it will update
    the data with no problems
    if ID was not found it will thros an Exception]

    Exception:
    The Id entered was not found please try again

    Args:
    Data_ID: which is the id the function will
    use to update the data by searching
    for the data that matches the id

    Description: Which is the new data that
    will be entered by the user and replace the old description
    """
    for Data in todo_list:
        if Data['id'] == Data_ID:
            Data["description"] = Description
            return
    raise Exception("ID was not found please retry again")


def Get_Data() -> dict:
    """[A function that will get all the data from our list
    if the list was empty it will raise an Exception]

    Exception:
    No data was found. *List is empty*

    Returns:
    todo_list: all the data stored in our list
    """
    if len(todo_list) == 0:
        raise Exception("No data was found. *List is empty*")
    return todo_list


def DeleteDataByID(Data_ID) -> None:
    """[A function that deletes a specific row
    from the data by the id and raise an exception if that id was not found]

    Exception:
    ID was not found please retry again

    Args:
    Data_ID: the id we use to search the list for the row we want to delete
    """
    for index, Data in enumerate(todo_list):
        if Data['id'] == Data_ID:
            print(index)
            todo_list.pop(index)
            return
    raise Exception("ID was not found please retry again")


def update_data_status(Data_ID, status: int) -> None:
    """[A function that updates the status of specific row
    in our data using the id of that row
    raise an expetion if the id was not found]

    Exception:
    ID was not found please retry again

    Args:
    Data_ID: which is the id the function will
    use to update the status by searching
    for the data that matches the id

    status: which is the new status that will be updated
    once the id is found inside the list
    """
    for Data in todo_list:
        if Data['id'] == Data_ID:
            Data["status"] = status
            return
    raise Exception("ID was not found please retry again")


def GetDataByID(Data_ID) -> dict:
    """[A function that is used to get a specifi row from our list of
    data by using the id raises an Exception if the id was not found]

    Exception:
    ID was not found please retry again

    Args:
    Data_ID: the id we use to search the list for the row we want to retreive aka Get
    """
    if len(todo_list) == 0:
        raise Exception("No data inside the list")
    else:
        for Data in todo_list:
            if Data['id'] == Data_ID:
                return Data
        raise Exception("ID was not found please retry again")
