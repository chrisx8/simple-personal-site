from mozilla_django_oidc.auth import OIDCAuthenticationBackend


# custom OIDCAuthenticationBackend. writes username and first and last name
class SPSOIDCAuthBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        # create user normally
        user = super(SPSOIDCAuthBackend, self).create_user(claims)

        # change username, first name, and lastname
        user.username = claims.get('preferred_username', '')
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        return user

    def update_user(self, user, claims):
        # update username, first name, and lastname when IdP info changes
        user.username = claims.get('preferred_username', '')
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        return user
