from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .motor_control import MotorController
import json
motor_ctl = MotorController()  # Ваш класс управления моторами

@csrf_exempt
def control_command(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            command = data.get('command', 'stop')
            motor_ctl.handle_command(command)
            return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error'}, status=405)