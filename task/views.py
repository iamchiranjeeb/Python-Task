from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import EmployeeForm
from .models import EmployeesTable
from .passwords import Special
# Create your views here.

def signupuser(request):
    if request.method == 'GET':
        return render(request,'task/signup2.html',{'form':UserCreationForm()})
    else:
        sp = Special(request.POST['password1'])
        #errors
        err1 = "Password too short"
        err2 = "Password can not be Entirely Numeric"
        err3 = "Password must contain a small letter"
        err4 = "Password must have at least one numeric"
        err5 = "Password must have at least one special character from these [_@$/|?#]"
        err6 = "Password must have at least one Capital Letter"
        
        if len(request.POST['password1']) <= 7:
            return render(request,'task/signup2.html',{'form':UserCreationForm(),"error":err1})
        elif request.POST['password1'].isdigit():
            return render(request,'task/signup2.html',{'form':UserCreationForm(),"error":err2})
        elif sp.capitalCheck() == False:
            return render(request,'task/signup2.html',{'form':UserCreationForm(),"error":err6})
        elif sp.smallCheck()==False:
            return render(request,'task/signup2.html',{'form':UserCreationForm(),"error":err3})
        elif sp.numCheck() == False:
            return render(request,'task/signup2.html',{'form':UserCreationForm(),"error":err4})
        elif sp.checkSpecial() == False:
            return render(request,'task/signup2.html',{'form':UserCreationForm(),"error":err5})
        elif request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('userprofile')
            except IntegrityError:
                return render(request,'task/signup2.html',{'form':UserCreationForm(),"error":"User Name Taken Already."})
            except Exception as e:
                return render(request,'task/signup2.html',{'form':UserCreationForm(),"error":e})

def loginuser(request):
    if request.method == 'GET':
        return render(request,'task/login2.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            errmsg = "Username & password does not match."
            return render(request,'task/login2.html',{'form':AuthenticationForm(),'error':errmsg})
        else:
            try:
                login(request,user)
                return redirect('userprofile')
            except Exception as e:
                return render(request,'task/login2.html',{'form':AuthenticationForm(),'error':e})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')

def userprofile(request):
    emp_det = EmployeesTable.objects.filter(user=request.user)
    # profile = User.objects.get(id=request.user.id)
    # emp_pk = profile
    # obj = get_object_or_404(EmployeesTable,user=profile)
    return render(request,'task/profile.html',{'obj':emp_det})

def createprofile(request):
    if request.method == 'GET':
        return render(request,'task/createprofile2.html',{'form':EmployeeForm()})
    else:
        try:
            form = EmployeeForm(request.POST,request.FILES)
            newEmployee = form.save(commit=False)
            newEmployee.user = request.user
            newEmployee.save()
            return redirect('userprofile')
        except ValueError:
            return render(request,'task/createprofile2.html',{'form':EmployeeForm(),'error':"Bad Data"})

        except Exception as e:
            return render(request,'task/createprofile2.html',{'form':EmployeeForm(),'error':e})

def viewuserprofile(request,emp_pk):
    emp = get_object_or_404(EmployeesTable,pk=emp_pk,user=request.user)
    if request.method == 'GET':
        return render(request,'task/viewuserprofile.html',{'emp':emp})
    else:
        emp.delete()
        return redirect('userprofile')


def edituserprofile(request,emp_pk):
    emp = get_object_or_404(EmployeesTable,pk=emp_pk,user=request.user)
    if request.method == 'GET':
        return render(request,'task/editprofile2.html',{'form':EmployeeForm(instance=emp),'emp':emp})
    else:
        try:
            form = EmployeeForm(request.POST,request.FILES,instance=emp)
            form.save()
            return redirect('userprofile')
        except ValueError:
            return render(request,'task/editprofile2.html',{'form':EmployeeForm(instance=emp),'emp':emp,'error':'Bad Data'})
        except Exception as e:
            return render(request,'task/editprofile2.html',{'form':EmployeeForm(instance=emp),'emp':emp,'error':e})


