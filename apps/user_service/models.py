from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self,telephone,username,password,**kwargs):
        if not telephone:
            raise ValueError('请传入手机号码！')
        if not username:
            raise ValueError('请传入用户名！')
        if not password:
            raise ValueError('请传入密码！')

        user = self.model(telephone=telephone,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone,username,password,**kwargs)

    def create_superuser(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone,username,password,**kwargs)

class User(AbstractBaseUser,PermissionsMixin):
    """重写django自带的user表"""

    # 自增id
    # id = models.AutoField()
    # username
    username = models.CharField(unique=False,max_length=16,verbose_name="用户名")
    # 手机号
    telephone = models.CharField(unique=True,max_length=11,verbose_name="手机号")
    # email
    email = models.EmailField(unique=True,max_length=32,verbose_name="邮箱",null=True)
    # 昵称
    nick_name = models.CharField(unique=False,max_length=16,verbose_name="昵称")
    # 头像
    avatar = models.CharField(max_length=200,verbose_name="头像")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    # 更新时间
    update_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    # 是否可用
    is_active = models.BooleanField(default=True,verbose_name="是否可用")

    # 用户名用到的字段
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['username']

    EMAIL_FIELD = 'email'

    object = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username