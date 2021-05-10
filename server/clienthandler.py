
import json
import threading
import sys
import calcData


class ClientHandler(threading.Thread):

    numbers_clienthandlers = 0

    def __init__(self, socketclient, messages_queue):
        threading.Thread.__init__(self)
        # connectie with client
        self.socket_to_client = socketclient
        # message queue -> link to gui server
        self.messages_queue = messages_queue
        # id clienthandler
        self.id = ClientHandler.numbers_clienthandlers
        ClientHandler.numbers_clienthandlers += 1

        self.datahandler = calcData.dataHandler()

    def run(self):
        io_stream_client = self.socket_to_client.makefile(mode='rw')

        self.print_bericht_gui_server("Started & waiting...")
        commando = io_stream_client.readline().rstrip('\n')
        while (commando != "CLOSE"):
            msg = io_stream_client.readline().rstrip('\n')
            self.print_bericht_gui_server(f"Message: {msg}")

            if msg == "Verify":
                getal1 = io_stream_client.readline().rstrip('\n')
                self.print_bericht_gui_server(f"Username: {getal1}")
                getal2 = io_stream_client.readline().rstrip('\n')
                self.print_bericht_gui_server(f"Mail: {getal2}")
                database = "data\data.json"
                data = json.loads(open(database).read())
                user_data = data['user_info']

                user_info = []
                for i in user_data:

                    if getal1 == i['username']:

                        user_info.append(i['name'])
                        user_info.append(i['username'])
                        user_info.append(i['mail'])
                        user_info.append(i['status'])

                    else:
                        pass

                if getal1 in user_info:
                    if getal2 == user_info[2]:
                        antw = '1'
                        with open('data\data.json', 'r') as f:
                            change = json.load(f)

                        change["user_info"]['username' ==
                                            getal1]['status'] = 1  # hier plaats je status van login naar 1 dus iedereen dat op 1 staat is ingelogd en er moet op de loguit hetzelfe maar terug naar 0 en dan zijn ze pas uitgelogd

                        with open('data\data.json', 'w') as f:
                            json.dump(change, f)

                    else:
                        antw = '2'

                else:
                    antw = '3'

                user_info.clear()
                io_stream_client.write(f"{antw}\n")
                io_stream_client.flush()
                self.print_bericht_gui_server(
                    f"Sending verification {antw} back")

            elif msg == "Register":
                name = io_stream_client.readline().rstrip('\n')
                self.print_bericht_gui_server(f"Name: {name}")
                username = io_stream_client.readline().rstrip('\n')
                self.print_bericht_gui_server(f"Username: {username}")
                mail = io_stream_client.readline().rstrip('\n')
                self.print_bericht_gui_server(f"Mail: {mail}")
                status = io_stream_client.readline().rstrip('\n')
                self.print_bericht_gui_server(f"Status: {status}")

                def write_json(data, filename='data\data.json'):
                    with open(filename, 'w') as f:
                        json.dump(data, f, indent=4)

                with open('data\data.json') as json_file:
                    data = json.load(json_file)

                    temp = data['user_info']

                    # python object to be appended
                    y = {"name": name,
                         "username": username,
                         "mail": mail,
                         "status": int(status)
                         }

                    # appending data to emp_details
                    temp.append(y)

                write_json(data)
                # io_stream_client.write(f"{antw}\n")
                io_stream_client.flush()
                self.print_bericht_gui_server(f"Registration Compleet")

            elif msg == "Get parameters":

                # data = data.data.dataHandler
                age1 = io_stream_client.readline().rstrip('\n')
                self.print_bericht_gui_server(f"Age: {age1}")
                result = self.datahandler.getParameters(age1)
                self.print_bericht_gui_server(f"Age result: {result}")
                io_stream_client.write(f"{result}\n")
                io_stream_client.flush()

            elif msg == "Get Gender Graph":
                result = self.datahandler.getGraph("gender")
                self.print_bericht_gui_server(result)
                io_stream_client.write(f"{result}\n")
                io_stream_client.flush()

                # data = data.data.dataHandler
                # age1 = io_stream_client.readline().rstrip('\n')
                # self.print_bericht_gui_server(f"Age: {age1}")
                # result = self.datahandler.getParameters(age1)
                # self.print_bericht_gui_server(f"Age result: {result}")
                # io_stream_client.write(f"{result}\n")
                # io_stream_client.flush()

            elif msg == "Get Heart Disease Graph":
                result = self.datahandler.getGraph("heart_disease")
                self.print_bericht_gui_server(result)
                io_stream_client.write(f"{result}\n")
                io_stream_client.flush()

            elif msg == "Get Statistic Data":
                result = self.datahandler.getStatistics()
                self.print_bericht_gui_server(result)
                io_stream_client.write(f"{result}\n")
                io_stream_client.flush()

            commando = io_stream_client.readline().rstrip('\n')

        self.print_bericht_gui_server("Connection with client closed...")
        self.socket_to_client.close()

    def print_bericht_gui_server(self, message):
        self.messages_queue.put(f"CLH {self.id}:> {message}")
