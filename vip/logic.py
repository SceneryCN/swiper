import logging

from common.errors import NotHasPerm

err_logger = logging.getLogger('err')


def need_perm(perm_name):
    '''权限检查装饰器'''
    def check(view_func):
        def wrapper(request):
            user = request.user
            if user.vip.has_perm(perm_name):
                return view_func(request)
            else:
                err_logger.error(f'user({user.id}) not has perm {perm_name}')
                raise NotHasPerm
        return wrapper
    return check
