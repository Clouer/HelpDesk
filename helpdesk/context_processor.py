from helpdesk.models import User


def user_is_support(request):
    if request.user.is_active:
        current_user = User.objects.get(pk=request.user.id)
        permissions = {
            'user_is_support': True if current_user.is_support else False,
            'user_is_super_support': True if current_user.is_super_support else False
        }
        return permissions
    return {'user_is_support': False, 'user_is_super_support': False}
