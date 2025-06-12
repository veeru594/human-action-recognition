from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel, UserActionsModel
from django.core.files.storage import FileSystemStorage
from datetime import datetime


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHomePage.html', {})


def UserUploadPic(request):
    return render(request, "users/UploadPicForm.html", {})


def UploadImageAction(request):
    image_file = request.FILES['file']
    # let's check if it is a csv file
    if not image_file.name.endswith('.png'):
        messages.error(request, 'THIS IS NOT A PNG  FILE')

    fs = FileSystemStorage(location="media/actions/")
    filename = fs.save(image_file.name, image_file)
    # detect_filename = fs.save(image_file.name, image_file)
    uploaded_file_url = "/media/actions/" + filename  # fs.url(filename)
    print("Image path ", uploaded_file_url)

    from .utility.ClassifyIMages import ClassifyUserPics
    obj = ClassifyUserPics()
    result = obj.startProcess(filename)
    print("Result=", result)
    return render(request, "users/UploadPicForm.html", {'result': result})


def UserStreamAction(request):
    from .utility.UserLiveStream import LiveStream
    obj = LiveStream()
    actions = obj.startProcess()
    print('Result is:', actions)
    name = request.session['loggeduser']
    login_user = request.session['loginid']
    email = request.session['email']
    c_date = datetime.now()
    UserActionsModel.objects.create(name=name, login_user=login_user, email=email, actions=str(actions), c_date=c_date)
    return render(request, 'users/UserActions.html', {'actions': actions})


def UserActionsViews(request):
    login_user = request.session['loginid']
    data = UserActionsModel.objects.filter(login_user=login_user)
    return render(request, 'users/UserActionViews.html', {'data': data})


def UserVideoProcess(request):
    if request.method == 'POST':
        image_file = request.FILES['file']
        fs = FileSystemStorage(location="media/videos/")
        filename = fs.save(image_file.name, image_file)
        # detect_filename = fs.save(image_file.name, image_file)
        uploaded_file_url = "media/videos/" + filename  # fs.url(filename)
        print("Image path ", uploaded_file_url)
        import subprocess
        import os
        path = os.path.join(uploaded_file_url)
        harActivity = "human_activity_reco.py --model resnet-34_kinetics.onnx --classes action_recognition_kinetics.txt --input "+path
        print(harActivity)
        subprocess.call("python " + harActivity)
        return render(request, 'users/UserVideoProcess.html', {})
    else:
        return render(request, 'users/UserVideoProcess.html', {})
