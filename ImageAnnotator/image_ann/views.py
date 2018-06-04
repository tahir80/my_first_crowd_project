from django.shortcuts import render
from image_ann.models import Hit


def hit(request, id):
    h = get_object_or_404(Hit, pk=id)
    # see if there's a turkSubmitTo parameter in the request GET:
    # action = 'http://www.mturk.com/mturk/externalSubmit'
    action = 'http://workersandbox.mturk.com/mturk/externalSubmit'
    #turkSubmitTo: the Mechanical Turk submission server (either production or sandbox).
    # if request.GET.has_key('turkSubmitTo'):
    #     action = request.GET['turkSubmitTo'] + '/mturk/externalSubmit'

    assignment_id = None
    if request.GET.has_key('assignmentId'):
        assignment_id = request.GET['assignmentId']

    return render_to_response('hit.html',
        {'title': h.title, 'body': h.body, 'assignment_id': assignment_id, 'action': action})
