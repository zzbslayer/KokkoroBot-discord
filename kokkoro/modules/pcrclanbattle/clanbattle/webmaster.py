from datetime import datetime, timezone, timedelta

from kokkoro import config
from kokkoro.util import rand_string
from .dao.sqlitedao import ClanDao, MemberDao, UserDao, UserLoginDao
from .exception import NotFoundError

class WebMaster():
    def __init__(self):
        super().__init__()
        self.clandao = ClanDao()
        self.memberdao = MemberDao()
        self.userdao = UserDao()
        self.logindao = UserLoginDao()

    def get_or_add_user(self, uid):
        authority_group = 100
        if uid in config.SUPER_USER:
            authority_group = 1
        return self.userdao.get_or_add(uid, authority_group, rand_string())
    def get_user(self, uid):
        return self.userdao.find_one(uid)
    def get_user_with_member(self, uid):
        user = self.get_user(uid)
        member = self.memberdao.find_one(uid)
        user['name'] = member['name']
        user['gid'] = member['gid']
        return user
    def get_user_with_clan(self, uid):
        user = self.get_user_with_member(uid)
        clan = self.clandao.find_one(user['gid'], 1)
        user['clan_name'] = clan['name']
        return user
    def mod_user(self, user:dict):
        return self.userdao.modify(user)

    def add_login(self, uid, auth_cookie, auth_cookie_expire_time):
        return self.logindao.add(uid, auth_cookie, auth_cookie_expire_time)
    def get_login(self, uid, auth_cookie):
        return self.logindao.find_one(uid, auth_cookie)
    def mod_login(self, login:dict):
        return self.logindao.modify(login)
    def del_login(self, uid):
        return self.logindao.delete(uid)
    def del_login_by_time(self, time):
        return self.logindao.delete_by_time(self, time)
