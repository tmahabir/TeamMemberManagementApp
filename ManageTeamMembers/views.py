from django.shortcuts import render, redirect
from .models import Member

# Create your views here.
def list(request):
    members = Member.objects.all()
    membersCount = Member.objects.all().count()
    return render(request, 'list.html', {'members': members, 'membersCount': membersCount})

def addMember(request):
    if request.method == 'POST':
        adminTemp = request.POST.get('isAdmin', False)
        if adminTemp == 'admin':
            adminTemp = True
        else:
            adminTemp = False     

        adminViewTemp = ''
        if adminTemp:
            adminViewTemp = '(admin)'
        
        new_member = Member(
            first_name = request.POST['firstName'],
            last_name = request.POST['lastName'],
            email = request.POST['email'],
            phone_number = request.POST['phoneNumber'],
            admin = adminTemp,
            adminView = adminViewTemp
        )
        new_member.save()
        return redirect('/')
    return render(request, 'addMember.html')

def editMember(request, pk):
    member = Member.objects.get(id=pk)
    if request.method == 'POST':
        if 'saveBtn' in request.POST:
            adminTemp = request.POST.get('isAdmin', False)
            if adminTemp == 'admin':
                adminTemp = True
            else:
                adminTemp = False    
            member.first_name = request.POST['firstName']
            member.last_name = request.POST['lastName']
            member.email = request.POST['email']
            member.phone_number = request.POST['phoneNumber']
            member.admin = adminTemp
            
            if member.admin:
                member.adminView = '(admin)'
            else:
                member.adminView = ''
            
            member.save()
            return redirect('/')
        elif 'deleteBtn' in request.POST:
            member.delete()
            return redirect('/')
    if member.admin:
        return render(request, 'editAdmin.html', {'member': member})
    else:
        return render(request, 'editMember.html', {'member': member})
