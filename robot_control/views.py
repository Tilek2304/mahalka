from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .motor_control import MotorController

motor_ctl = MotorController(
            pca,
            left_ch_a=pca.channels[1],  # IN1
            left_ch_b=pca.channels[0],  # IN2
            right_ch_a=pca.channels[3], # IN3
            right_ch_b=pca.channels[2] # IN4
        )

@csrf_exempt
def control_command(request):
    if request.method == 'POST':
        command = request.POST.get('command', 'stop')
        motor_ctl.handle_command(command)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})