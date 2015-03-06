import UserController

@user.get()
def get_info(request):
    return {'User'}