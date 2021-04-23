import random
import threading
import pickle
import math
import os


class ClientHandler(threading.Thread):
    numbers_clienthandlers = 0

    def __init__(self, socketclient, messages_queue):
        threading.Thread.__init__(self)
        # connectie with client
        self.socketclient = socketclient
        # message queue -> link to gui server
        self.messages_queue = messages_queue
        # id clienthandler
        self.id = ClientHandler.numbers_clienthandlers
        ClientHandler.numbers_clienthandlers += 1
        self.in_out_clh = self.socketclient.makefile(mode='rwb')

    def run(self):

        command = pickle.load(self.in_out_clh)

        while (command != "CLOSE"):
            print(command)

            if (command == "get_random_image"):
                # filename = 'images/kleuren.jpg'
                filename = self.getRandomFile()  # hulpmethode
                f = open(filename, 'rb')

                # bepaal de bestandsgrootte
                size_in_bytes = os.path.getsize(filename)
                # bereken hoeveel keer 1024 bytes verstuurd zullen worden
                number = math.ceil(size_in_bytes / 1024)

                # voorbereiding: ik geef dit aantal door aan de cliënt zodat hij weet hoeveel keer
                # hij het readcommando zal moeten doen (om zo de afbeelding volledig binnen te halen)
                pickle.dump("%d" % number, self.in_out_clh)
                self.in_out_clh.flush()

                # volgende stap: het effectief versturen van de afbeelding
                l = f.read(1024)
                while (l):
                    self.socketclient.send(l)
                    # volgende 1024 bytes inlezen
                    l = f.read(1024)

            # waiting for next commando
            command = pickle.load(self.in_out_clh)

        self.print_bericht_gui_server("Connection with client closed...")
        self.socketclient.close()

    def print_bericht_gui_server(self, message):
        self.messages_queue.put("CLH %d:> %s" % (self.id, message))

    def getRandomFile(self):
        """
        Returns a random filename, chosen among the files of the given path.
        """
        files = os.listdir("images")
        index = random.randrange(0, len(files))
        return "images/%s" % files[index]
