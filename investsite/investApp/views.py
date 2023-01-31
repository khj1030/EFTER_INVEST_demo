from django.shortcuts import render, redirect

from .models import userLogin, projectDB

from django.contrib import messages

# Create your views here.
def main(request):
    # data = {"dataList":userLogin.objects.all()}
    dataList = userLogin.objects.all()
    dataResult = {}
    for list in dataList:
        dataTemp = {}
        dataTemp['team'] = list.user_team
        dataTemp['team1'] = list.team1
        dataTemp['team2'] = list.team2
        dataTemp['team3'] = list.team3
        dataTemp['team4'] = list.team4
        dataTemp['team5'] = list.team5
        dataTemp['user_money'] = list.user_money

        dataResult[list.user_id] = dataTemp
    # dataList = [list for list in dataList]
    return render(request, 'main.html', {'dataList':dataResult})

def investPage(request):
    dataList = userLogin.objects.all()
    dataResult = {}
    for list in dataList:
        dataTemp = {}
        dataTemp['team'] = list.user_team
        dataTemp['team1'] = list.team1
        dataTemp['team2'] = list.team2
        dataTemp['team3'] = list.team3
        dataTemp['team4'] = list.team4
        dataTemp['team5'] = list.team5
        dataTemp['user_money'] = list.user_money
        dataResult[list.user_id] = dataTemp
    return render(request, 'invest.html', {'dataList':dataResult})

def investDetailPage(request):
    # JsonResponse("!!!")
    dataList = userLogin.objects.all()
    dataResult = {}
    for list in dataList:
        dataTemp = {}
        dataTemp['team'] = list.user_team
        dataTemp['team1'] = list.team1
        dataTemp['team2'] = list.team2
        dataTemp['team3'] = list.team3
        dataTemp['team4'] = list.team4
        dataTemp['team5'] = list.team5
        dataTemp['user_money'] = list.user_money
        dataResult[list.user_id] = dataTemp
    
    projList = projectDB.objects.all()
    projResult = {}
    for list in projList:
        projResult[list.proj_id] = list.name
    return render(request, 'invest_detail.html', {'dataList':dataResult, 'projList':projResult})

def update_add(request):
    update_money = userLogin.objects.get(user_id= request.POST['user_id'])
    projNum = int(request.POST['proj_num'])

    if projNum==1: 
        update_money.team1 += int(request.POST['invest'])
        if update_money.team1 > 7500000:
            messages.warning(request, "최대 투자 가능 금액은 7,500,000원 입니다.")
            return redirect('/invest_detail')
    elif projNum==2: 
        update_money.team2 += int(request.POST['invest'])
        if update_money.team2 > 7500000:
            messages.warning(request, "최대 투자 가능 금액은 7,500,000원 입니다.")
            return redirect('/invest_detail')
    elif projNum==3: 
        update_money.team3 += int(request.POST['invest'])
        if update_money.team3 > 7500000:
            messages.warning(request, "최대 투자 가능 금액은 7,500,000원 입니다.")
            return redirect('/invest_detail')
    elif projNum==4: 
        update_money.team4 += int(request.POST['invest'])
        if update_money.team4 > 7500000:
            messages.warning(request, "최대 투자 가능 금액은 7,500,000원입니다.")
            return redirect('/invest_detail')
    elif projNum==5: 
        update_money.team5 += int(request.POST['invest'])
        if update_money.team5 > 7500000:
            messages.warning(request, "최대 투자 가능 금액은 7,500,000원 입니다.")
            return redirect('/invest_detail')
    update_money.user_money -= int(request.POST['invest'])
    if update_money.user_money < 0:
        messages.warning(request, "보유금액을 초과하였습니다.")
        return redirect('/invest_detail')
        
    update_money.save()

    dataList = userLogin.objects.all()
    dataResult = {}
    for list in dataList:
        dataTemp = {}
        dataTemp['team'] = list.user_team
        dataTemp['team1'] = list.team1
        dataTemp['team2'] = list.team2
        dataTemp['team3'] = list.team3
        dataTemp['team4'] = list.team4
        dataTemp['team5'] = list.team5
        dataTemp['user_money'] = list.user_money
        dataResult[list.user_id] = dataTemp
    return redirect('/invest', {'dataList':dataResult})

def update_sub(request):
    update_money = userLogin.objects.get(user_id= request.POST['user_id'])
    projNum = int(request.POST['proj_num'])

    if projNum==1: 
        update_money.team1 -= int(request.POST['invest'])
        if update_money.team1 < 0:
            messages.warning(request, "투자금액을 초과하여 뺄 수 없습니다.")
            return redirect('/invest_detail')
    elif projNum==2: 
        update_money.team2 -= int(request.POST['invest'])
        if update_money.team2 < 0:
            messages.warning(request, "투자금액을 초과하여 뺄 수 없습니다.")
            return redirect('/invest_detail')
    elif projNum==3: 
        update_money.team3 -= int(request.POST['invest'])
        if update_money.team3 < 0:
            messages.warning(request, "투자금액을 초과하여 뺄 수 없습니다.")
            return redirect('/invest_detail')
    elif projNum==4: 
        update_money.team4 -= int(request.POST['invest'])
        if update_money.team4 < 0:
            messages.warning(request, "투자금액을 초과하여 뺄 수 없습니다.")
            return redirect('/invest_detail')
    elif projNum==5: 
        update_money.team5 -= int(request.POST['invest'])
        if update_money.team5 < 0:
            messages.warning(request, "투자금액을 초과하여 뺄 수 없습니다.")
            return redirect('/invest_detail')
    update_money.user_money += int(request.POST['invest'])
    update_money.save()

    dataList = userLogin.objects.all()
    dataResult = {}
    for list in dataList:
        dataTemp = {}
        dataTemp['team'] = list.user_team
        dataTemp['team1'] = list.team1
        dataTemp['team2'] = list.team2
        dataTemp['team3'] = list.team3
        dataTemp['team4'] = list.team4
        dataTemp['team5'] = list.team5
        dataTemp['user_money'] = list.user_money
        dataResult[list.user_id] = dataTemp
    return redirect('/invest', {'dataList':dataResult})