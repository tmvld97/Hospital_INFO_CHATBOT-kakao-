import socket

class BotServer:
    def __init__(self, srv_port, listen_num):   # srv_port = 소켓서버의 포트 번호, listen_num : 연결을 수락할 클라이언트 수
        self.port = srv_port
        self.listen = listen_num
        self.mySock = None

    # sock 생성
    def create_sock(self):  # BotServer의 소켓을 생성하는 메서드
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock.bind(("0.0.0.0", int(self.port)))
        self.mySock.listen(int(self.listen))
        return self.mySock

    # client 대기
    def ready_for_client(self): # 챗봇 클라이언트 연결을 대기하고 있다가 연결을 수락하는 메서드
        return self.mySock.accept()

    # sock 반환
    def get_sock(self): # 생성된 서버 소켓 반환
        return self.mySock