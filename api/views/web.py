# -*- coding: utf-8 -*-
import os
from django.shortcuts import render


def mainpage(request):
	return render(request, 'i/Index.html', {})

def thanks(request):
	return render(request, 'thanks/Index.html', {})

def payment_page(request, id):
    return render(request, 'tip_payment.html', {})

def terms(request):
	return render(request, 'terms/Index.html', {})

def privacy(request):
	return render(request, 'privacy/Index.html', {})

def error_404_view(request, exception):
	return render(request, 'Error/Index.html', {})

def error_500_view(request):
	return render(request, 'Error/Index.html', {})
