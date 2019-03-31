from django.contrib.auth.password_validation import validate_password

def passVerify(req):

    if(req.POST['new_password1'] == req.POST['new_password2'] and validate_password(req.POST['new_password1'], user=req.user) == None):
        return True
    else:
        return False
