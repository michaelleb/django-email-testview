from django.apps import AppConfig

class EmailTestViewConfig(AppConfig):
    """Simple AppConfig which does automatic discovery of emails in other apps."""

    name = 'email_testview'

    def ready(self):
        self.module.autodiscover_emails()

