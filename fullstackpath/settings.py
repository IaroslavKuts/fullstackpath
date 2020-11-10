import os
import dynaconf


if os.environ['DJANGO_ENV'] == 'development':
    settings = dynaconf.DjangoDynaconf(__name__,
                                   SETTINGS_FILE_FOR_DYNACONF=["../settings_development.yaml", "../.secrets.yaml"])

else:
    settings = dynaconf.DjangoDynaconf(__name__,
                                   SETTINGS_FILE_FOR_DYNACONF=["../settings_production.yaml", "../.secrets.yaml"])