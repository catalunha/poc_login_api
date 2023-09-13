from django.contrib.auth.base_user import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser deve ter is_staff=True. Pois tem acesso ao admin."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser deve ter is_superuser=True. Pois é super usuário."
            )
        return self.create_user(email, password, **extra_fields)
