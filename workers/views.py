from django.shortcuts import render

from workers.forms import WorkerForm


def worker_create(request):
    if request.method == 'POST':
        worker_form = WorkerForm(request.POST or None)
        if worker_form.is_valid():
            worker_form.save()
    else:
        worker_form = WorkerForm()
    return render(request, 'workers/worker_form.html', {'worker_form': worker_form})
