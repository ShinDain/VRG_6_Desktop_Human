# Python 3.9
# Made by: Fortbonnitar
# This works as a bridge between Unreal Engine and Python by allowing the exchanging of data through a local TCP socket connection.


print("""
========================
Unreal_Python_TCP_Bridge
========================
""")

import socket
import weather
import news
import AI
import GetWindowURL_pywinauto
import searchAPI_Serper

debug = False

##########################################################################################
# Set this script as a TCP-Server and create the socket and listen for Unreal connection 
###########################################################################################

class TCP:
    def __init__(self, ip_address: str='127.0.0.1', port: int=8000):
        self.running = True
        self.ip_address = ip_address
        self.port = port
        self.debug = True

        # Create a TCP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the server socket to a specific IP address and port
        self.server_address = (self.ip_address, self.port)
        self.server_socket.bind(self.server_address)

    def listen(self):
        # Listen for incoming connections
        self.server_socket.listen(1)
        print("Server started. Waiting for connections...")

        # Accept a client connection
        self.client_socket, self.client_address = self.server_socket.accept()
        print(f"Client connected: {self.client_address}")


        ##############################################################################
        # After Connection established successfully, if data recieved set as variable
        ###############################################################################


    def get_incoming(self):
        # Main Loop
        while self.running:
            try:
                data = self.client_socket.recv(4096)
                
                # Data is firstly decoded from bytes to a string
                self.in_data = data.decode()

                if self.in_data == '':
                    exit()

                if self.debug == True:
                    print(f'data as string = {self.in_data}')

                order = self.in_data.split(':')

                answer = ""

                if order[0] == '날씨':
                    try:
                        answer = weather.scrape_weather_and_dust()
                    except Exception as e:
                        answer = '날씨 정보를 획득할 수 없습니다.'
                elif order[0] == '요약':
                    try:
                        find_url = GetWindowURL_pywinauto.GetCurrentURL()
                        if find_url.startswith('http'):
                            answer = AI.chat(find_url)
                        else:
                            answer = 'Chrome 브라우저가 아닙니다.'
                    except Exception as e:
                        answer = '사이트 본문이 너무 깁니다. 토큰을 늘려주세요.'
                elif order[0] == '질문':
                    print(self.in_data.__len__())
                    answer = searchAPI_Serper.chat_respons(order[2])
                elif order[0] == '뉴스':
                    if order[1] == '정치':
                        answer = news.scrape_politics_headline_news()
                    elif order[1] == '경제':
                        answer = news.scrape_economy_headline_news()
                    elif order[1] == '문화':
                        answer = news.scrape_culture_headline_news()
                    elif order[1] == '세계':
                        answer = news.scrape_world_headline_news()
                    elif order[1] == '사회':
                        answer = news.scrape_society_headline_news()
                    elif order[1] == 'IT':
                        answer = news.scrape_it_headline_news()
                else:
                    answer = (f'잘못된 입력입니다.')

                self.out_data = answer
                self.send_data(f'{self.out_data}')
            
            except Exception as e:
                print(e)
                exit()


            
    def send_data(self, data_string, encoding='utf-8'):
            # Converting the sending data from string to bytes 
            reply_data = bytes(data_string, encoding)


            # Sending back to Unreal Engine
            send = self.client_socket.send(reply_data)

server = TCP()
server.listen()
server.get_incoming()

#print(news.scrape_politics_headline_news())
# print(GetWindowURL_pywinauto.GetCurrentURL())