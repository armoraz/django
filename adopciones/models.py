from django.db import models

RAZAS = [
    ('labrador', 'Labrador'),
    ('beagle', 'Beagle'),
    ('pastor_aleman', 'Pastor Alemán'),
    ('poodle', 'Poodle'),
    ('callejero', 'Callejero'),
]

SALUD = [
    ('sano', 'Sano'),
    ('tratamiento', 'En tratamiento'),
    ('recuperacion', 'En recuperación'),
]

TAMAÑOS = [
    ('pequeño', 'Pequeño'),
    ('mediano', 'Mediano'),
    ('grande', 'Grande'),
]

TEMPERAMENTOS = [
    ('tranquilo','Tranquilo'),
    ('jugueton','Juguetón'),
    ('protector','Protector'),
    ('sociable','Sociable'),
]

ESTADOS = [
    ('disponible', 'Disponible'),
    ('reservado', 'Reservado'),
    ('adoptado', 'Adoptado')
]


class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50, choices=RAZAS)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=20, choices=TAMAÑOS)
    peso = models.FloatField()
    estado_salud = models.CharField(max_length=100, choices=SALUD)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    temperamento = models.CharField(max_length=50, choices=TEMPERAMENTOS)
    url_imagen = models.URLField(max_length=300, null=True, blank=True)
    reservado_por = models.ForeignKey('UsuarioAdoptante', null=True, blank=True, on_delete=models.SET_NULL)


class UsuarioAdoptante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    preferencias_raza = models.CharField(max_length=50, choices=RAZAS, null=True, blank=True)
    preferencias_edad = models.IntegerField(null=True, blank=True)
    preferencias_tamaño = models.CharField(max_length=20, choices=TAMAÑOS)
