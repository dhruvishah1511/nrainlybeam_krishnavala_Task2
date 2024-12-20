

from django.shortcuts import render
from .models import ErrorLog
from django.db import models  
import matplotlib.pyplot as plt
import io
import base64

def home(request):
    return render(request, 'tasktry/home.html')

def view_logs(request):
   
    logs = ErrorLog.objects.all()


    status_counts = logs.values('status_code').annotate(count=models.Count('status_code')).order_by('status_code')

  
    status_codes = [status['status_code'] for status in status_counts]
    counts = [status['count'] for status in status_counts]

    fig, ax = plt.subplots()
    ax.bar(status_codes, counts, color='skyblue')
    ax.set_xlabel('Status Codes')
    ax.set_ylabel('Count')
    ax.set_title('Error Log Counts by Status Code')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph_url = base64.b64encode(buffer.read()).decode('utf-8')


    return render(request, 'tasktry/view_logs.html', {'logs': logs, 'graph_url': graph_url})
