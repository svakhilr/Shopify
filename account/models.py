from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class AccountManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,phone_number,password=None):
        if not email:
            return ValueError('User must have email')


        user = self.model(
            email       = self.normalize_email(email),
            
            first_name  = first_name,
            last_name   = last_name,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,first_name,last_name,phone_number,password):
        user=self.create_user(email=email,first_name=first_name,last_name=last_name,phone_number=phone_number,password=password)

        user.is_admin   = True
        user.is_active  = True
        user.is_staff   = True
        user.is_superadmin  = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    phone_number=models.CharField(max_length=15)

    date_joined     = models.DateTimeField(auto_now_add=True)  
    last_login      = models.DateTimeField(auto_now_add=True)  
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

     
    USERNAME_FIELD      = 'email'
    REQUIRED_FIELDS     = ['first_name', 'last_name','phone_number']

    objects = AccountManager()




    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    


class Address(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50) 


    def __str__(self):
        return f"{str(self.user_id)} {self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_address(self):
        return f"{self.address1} {self.address2}"