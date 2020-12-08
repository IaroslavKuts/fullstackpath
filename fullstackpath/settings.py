import os
import dynaconf
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

if os.environ['DJANGO_ENV'] == 'development':
    settings = dynaconf.DjangoDynaconf(__name__,
                                   SETTINGS_FILE_FOR_DYNACONF=["../settings_development.yaml", "../.secrets.yaml"],
                                   INCLUDES_FOR_DYNACONF="../env_vars.yaml")
    sentry_sdk.init(integrations=[DjangoIntegration()],**SENTRY_SDK)


else:
    settings = dynaconf.DjangoDynaconf(__name__,
                                   SETTINGS_FILE_FOR_DYNACONF=["../settings_production.yaml", "../.secrets.yaml"])