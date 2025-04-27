from channels.generic.websocket import WebsocketConsumer
import json
from .motor_control import MotorController

motor_ctl = MotorController()

class ControlConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        command = data['command']
        motor_ctl.handle_command(command)
        self.send(text_data=json.dumps({'status': 'ok'}))