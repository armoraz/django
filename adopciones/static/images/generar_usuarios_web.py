# populate_dummy_data.py

import os
import django
import random

# Setear entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_adopcion_web.settings")
django.setup()

# Importar modelos
from adopciones.models import Perro, UsuarioAdoptante

# Opciones de datos
RAZAS = [
    'labrador',
    'beagle',
    'pastor_aleman',
    'poodle',
    'callejero',
]

SALUD = ['sano', 'tratamiento', 'recuperacion']

TAMAÑOS = ['pequeño', 'mediano', 'grande']

TEMPERAMENTOS = ['tranquilo', 'jugueton', 'protector', 'sociable']

ESTADOS = ['disponible', 'reservado', 'adoptado']

IMAGENES = [
    "https://images.dog.ceo/breeds/terrier-australian/n02096294_2118.jpg",
    "https://images.dog.ceo/breeds/terrier-westhighland/n02098286_5080.jpg",
    "https://images.dog.ceo/breeds/eskimo/n02109961_4670.jpg",
    "https://images.dog.ceo/breeds/pitbull/dog-5437227_640.jpg",
    "https://images.dog.ceo/breeds/african/n02116738_233.jpg",
    "https://images.dog.ceo/breeds/terrier-kerryblue/n02093859_3140.jpg",
    "https://images.dog.ceo/breeds/malinois/n02105162_6492.jpg",
    "https://images.dog.ceo/breeds/hound-plott/hhh-23456.jpg",
    "https://images.dog.ceo/breeds/spaniel-sussex/n02102480_276.jpg",
    "https://images.dog.ceo/breeds/pariah-indian/The_Indian_Pariah_Dog.jpg",
    "https://images.dog.ceo/breeds/pinscher-miniature/n02107312_4929.jpg",
    "https://images.dog.ceo/breeds/clumber/n02101556_7987.jpg",
    "https://images.dog.ceo/breeds/dingo/n02115641_12981.jpg",
    "https://images.dog.ceo/breeds/mastiff-tibetan/n02108551_4421.jpg",
    "https://images.dog.ceo/breeds/australian-kelpie/IMG_7387.jpg",
    "https://images.dog.ceo/breeds/komondor/n02105505_4070.jpg",
    "https://images.dog.ceo/breeds/borzoi/n02090622_8338.jpg",
    "https://images.dog.ceo/breeds/groenendael/n02105056_5668.jpg",
    "https://images.dog.ceo/breeds/rajapalayam-indian/Rajapalayam-dog.jpg",
    "https://images.dog.ceo/breeds/terrier-welsh/lucy.jpg"
]

# Limpiar la base de datos (opcional, para no duplicar cada vez que corrés el script)
Perro.objects.all().delete()
UsuarioAdoptante.objects.all().delete()

print("Base de datos limpia.")

# Crear usuarios
usuarios = []
for i in range(10):
    usuario = UsuarioAdoptante.objects.create(
        nombre=f"Usuario{i+1}",
        dni=f"{random.randint(20000000, 50000000)}",
        email=f"usuario{i+1}@correo.com",
        preferencias_raza=random.choice(RAZAS),
        preferencias_edad=random.randint(1, 12),
        preferencias_tamaño=random.choice(TAMAÑOS)
    )
    usuarios.append(usuario)
    print(f"[+] Usuario creado: {usuario.nombre}")

# Crear perros
for i in range(20):
    estado = random.choice(ESTADOS)
    reservado_por = None
    
    # Si el perro está reservado o adoptado, lo vinculamos a un usuario al azar
    if estado in ['reservado', 'adoptado'] and usuarios:
        reservado_por = random.choice(usuarios)

    perro = Perro.objects.create(
        nombre=f"Perro{i+1}",
        raza=random.choice(RAZAS),
        edad=random.randint(1, 15),
        tamaño=random.choice(TAMAÑOS),
        peso=round(random.uniform(5.0, 40.0), 1),
        estado_salud=random.choice(SALUD),
        vacunado=random.choice([True, False]),
        estado=estado,
        temperamento=random.choice(TEMPERAMENTOS),
        url_imagen=random.choice(IMAGENES),
        reservado_por=reservado_por
    )
    
    print(f"[+] Perro creado: {perro.nombre} ({perro.estado}) → {perro.reservado_por.nombre if perro.reservado_por else 'No reservado'}")

print("\nDummy data generada exitosamente.")
