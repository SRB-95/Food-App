from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # User Signal
    def ready(self):
        import users.signals
