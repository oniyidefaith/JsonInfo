from django.http import JsonResponse
import datetime


def json_data_info(request):
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track', '')

    current_day = datetime.datetime.utcnow().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/oniyidefaith/JsonInfo/blob/main/jsons/views.py",
        "github_repo_url": "https://github.com/oniyidefaith/JsonInfo",
        "status_code": "200"
    }

    return JsonResponse(response_data)
