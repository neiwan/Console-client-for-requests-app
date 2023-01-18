import requests

HOST = "localhost"
PORT = 8080


def req_create_note(token):
    return requests.post(f"http://{HOST}:{PORT}/create_note", params={"token": token})


def req_read_note_by_id(id, token):
    return requests.get(f"http://{HOST}:{PORT}/read_note_by_id", params={"id": id, "token": token})


def req_get_note_time_info_by_id(id, token):
    return requests.get(f"http://{HOST}:{PORT}/get_note_time_info_by_id", params={"id": id, "token": token})


def req_update_note_text(id, text, token):
    return requests.put(f"http://{HOST}:{PORT}/update_note_text",
                        params={"id": id, "text": text, "token": token})


def req_delete_note_by_id(id, token):
    return requests.delete(f"http://{HOST}:{PORT}/delete_note_by_id", params={"id": id, "token": token})


def req_print_note_id(token):
    return requests.get(f"http://{HOST}:{PORT}/print_note_id", params={"token": token})


def input_id():
    return input("\nВведите id:")


def input_txt():
    return input("\nВведите текст:")


def server_response(response):
    print()
    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.text}")
    pass


def do_req():
    command_list = ["create note", "read note by id", "get note time info", "update note text",
                    "delete note by id", "print note id"]

    token = input("\ninput token:")
    command_number = input("input number of command\n"
                           "0 - create note\n"
                           "1 - read note by id\n"
                           "2 - get note time info\n"
                           "3 - update note text\n"
                           "4 - delete note by id\n"
                           "5 - print note id\n"
                           "6 - exit\n")

    is_valid_number = False
    if command_number.isdigit():
        command_number = int(command_number)
        try:
            print("you chose: ", command_list[command_number])
        except:
            print("invalid input")

        is_valid_number = True
    else:
        is_valid_number = False

    if is_valid_number:
        if command_number <= 6:
            response = ""
            if command_number == 0:
                response = req_create_note(token)
            if command_number == 1:
                id = input_id()
                response = req_read_note_by_id(id, token)
            if command_number == 2:
                id = input_id()
                response = req_get_note_time_info_by_id(id, token)
            if command_number == 3:
                id = int(input_id())
                text = input_txt()
                response = req_update_note_text(id, text, token)
            if command_number == 4:
                id = input_id()
                response = req_delete_note_by_id(id, token)
            if command_number == 5:
                response = req_print_note_id(token)
            if command_number == 6:
                exit(0)
            server_response(response)
        else:
            print("invalid input")
    pass


# Перед запуском этой программы запустить main.py!
if __name__ == '__main__':
    while True:
        do_req()
