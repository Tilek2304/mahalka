from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .motor_control import MotorController

motor_ctl = MotorController()  # Ваш класс управления моторами

@csrf_exempt
def control_command(request):
    if request.method == 'POST':
        command = request.POST.get('command', 'stop')
        motor_ctl.handle_command(command)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})