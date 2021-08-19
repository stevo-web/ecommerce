from ariadne import MutationType, upload_scalar
from .models import User

mutation = MutationType()


@mutation.field('register')
def resolve_register(_, info, firstname, lastname, email, phone, location, password):
    try:
        user = User.objects.create_user(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone=phone,
            location=location,
            password=password,
        )
        user.save()
        return {
            "success": True
        }
    except ValueError as err:
        return {
            "success": False
        }

resolvers = [mutation, upload_scalar]