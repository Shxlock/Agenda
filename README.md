Este proyecto es una agenda de contactos y tareas.

En este proyecto se uso como base de datos PostgreSQL, por lo cual se debe configurar este apartado:

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "agenda",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

según tu configuración de pgAdmin. 
