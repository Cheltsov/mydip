from core.models import User


# Create your models here.
class UserRepository(User):
    def check_client(self):
        tmp = User.objects.filter(email=self.email, password=self.password).values_list('id', flat=True)
        return tmp[0] if tmp else False

    @staticmethod
    def getUserByEmail(email):
        return User.objects.filter(email=email).all()

    class Meta:
        proxy = True
