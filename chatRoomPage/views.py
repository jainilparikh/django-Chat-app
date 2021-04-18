import datetime
import json
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view  
from rest_framework import viewsets
from .models import Message
from .serializer import LanguageSerializer, MessageSerializer


# Create your views here.
def home(request):
    """
        renders home Screen
        :param:
        :return: 
    """
    return render(request, 'chatRoomPage/home.html')


class LanguageView(viewsets.ModelViewSet): 
    '''
        Legacy Code
        :param: Django prebuilt ViewSet
        :return: 
    '''
    queryset = Message.objects.all()
    serializer_class = LanguageSerializer


def chatView(request):
    """
        Displays Chat Screen and saves the new chat messages that the user enters. 
        :param: Request Object
        :return: 
    """
    sender = request.session['sender']
    receiver = request.session['receiver']

    totalMessages = Message.objects.filter(sender = receiver)
    messageList = []
    messagesList1 = []
    for i in totalMessages:
        data = {
            'message': i.message,
            'time': i.time,
            'sender': '0'
            }
        messageList.append(data)
        
    totalMessages = Message.objects.filter(sender = sender)
    messagesList2 = []
    for i in totalMessages:
        data = {
            'message': i.message,
            'time': i.time,
            'sender': '1'
        }
        messageList.append(data)
    messageList = sorted(messageList, key = lambda k: k['time'])

    context = {
        'messagesList': messageList,
        'sender': sender,
        'receiver': receiver
    }

    if request.method == "POST":
        message = request.POST.get('messageBox') # response['message']
        res = Message(sender=sender, receiver=receiver, message=message, time= datetime.datetime.now())
        res.save()

        totalMessages = Message.objects.filter(sender = receiver)
        messageList = []
        messagesList1 = []
        for i in totalMessages:
            data = {
                'message': i.message,
                'time': i.time,
                'sender': '0'
            }
            messageList.append(data)
        
        totalMessages = Message.objects.filter(sender = sender)
        messagesList2 = []
        for i in totalMessages:
            data = {
                'message': i.message,
                'time': i.time,
                'sender': '1'
            }
            messageList.append(data)
            messageList = sorted(messageList, key = lambda k: k['time'])

        context = {
            'messagesList': messageList,
            'sender': sender,
            'receiver': receiver
        }
        return render(request, 'chatRoomPage/chatRoom.html', context)

    return render(request, 'chatRoomPage/chatRoom.html', context)


def loginView(request):
    """
       Displays Login Screen and moves the user to chat View screen.
       Currently we support only two users.
       :param: Request Object
       :return: 
    """
    if(request.method == "POST"):

        sender = request.POST.get('Username')
        if(sender == 'kate'):
            receiver = 'john'
        else:
            receiver = 'kate'
        
        request.session.set_test_cookie()
        request.session ['sender'] =  sender
        request.session ['receiver'] =  receiver
        
        request.method = 'GET'
        totalMessages = Message.objects.filter(sender = sender)
        messagesList1 = []
        messagesList = []

        for i in totalMessages:
            data = {
                'message': i.message,
                'time': i.time,
                'sender': '1'
            }
            messagesList.append(data)

        totalMessages = Message.objects.filter(sender = receiver)
        messagesList2 = []

        for i in totalMessages:
            data = {
                'message': i.message,
                'time': i.time,
                'sender': '0'
            }
            messagesList.append(data)
            messagesList = sorted(messagesList, key = lambda k: k['time'])

        context = {
            'messagesList': messagesList,
            'sender': sender,
            'receiver': receiver
        }
        return render(request, 'chatRoomPage/chatRoom.html', context)

    return render(request, 'loginScreen/login.html')


"""
@api_view(['GET', 'POST'])
def getMessageView(request): 
    '''
        Get Message API
        Legacy Code
    '''
    response = json.loads(request.body.decode('utf-8'))
    sender = response['sender']
    receiver = response['receiver']
    res = Message.objects.filter(sender=sender, receiver=receiver).values()
    messageList = []
    for i in res:
        print(i)
        print(i['message'])
        messageList.append(i['message'])

    return JsonResponse({'message': messageList})


@api_view(['GET', 'POST'])
def sendMessageView(request): 
    '''
        Get Message API
        Legacy code
    '''
    sender = 'user1'
    receiver = 'user2'
    message = '' # response['message']
    res = Message(sender=sender, receiver=receiver, message=message)
    res.save()
    return render(request, 'blogPage/chatRoom.html')
    # queryset = Message.objects.all()
    # serializer_class = MessageSerializer
"""