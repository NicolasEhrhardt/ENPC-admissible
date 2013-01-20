"""
Views which allow users to create and activate accounts.

"""

from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def test(**kwargs):
    """
    Test display template
    """
    
    return render_to_response('test.html', kwargs)


