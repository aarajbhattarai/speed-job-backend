from accounts.api.serializers import UserSerializer
import graphene
import graphql_jwt
from . import sub_mutations as user_mutations
from graphql_jwt import ObtainJSONWebToken
# class LoginObtainJSONWebToken(graphql_jwt.ObtainJSONWebToken):
#     user = "hello"

#     @classmethod
#     def resolve(cls, root, info, **kwargs):
#         return cls(user=info.context.user)

# class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
#     user = graphene.Field(UserType)

#     @classmethod
#     def resolve(cls, root, info, **kwargs):
#         return cls(user=info.context.user)
class AuthMutation(graphene.ObjectType):
    login = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_role=graphql_jwt.role.Field()
    # login=ObtainJSONWebToken 
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    employee_register = user_mutations.EmployeeRegister.Field()
    employer_register = user_mutations.EmployerRegister.Field()
