from django.core.management.base import BaseCommand
from adopciones.models import Perro, UsuarioAdoptante
import random

class Command(BaseCommand):
    help = 'Genera data dummy de perros y usuarios'

    def handle(self, *args, **kwargs):
        imagenes = [
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

        # Opciones
        razas = ['labrador', 'beagle', 'pastor_aleman', 'poodle', 'callejero']
        tamaños = ['pequeño', 'mediano', 'grande']
        estados = ['disponible', 'reservado', 'adoptado']
        temperamentos = ['tranquilo','jugueton','protector','sociable']
        salud = ['sano', 'tratamiento', 'recuperacion']

        # Borrar datos previos
        Perro.objects.all().delete()
        UsuarioAdoptante.objects.all().delete()

        # Crear perros
        for i, url in enumerate(imagenes):
            Perro.objects.create(
                nombre=f'Perro {i+1}',
                raza=random.choice(razas),
                edad=random.randint(1, 10),
                tamaño=random.choice(tamaños),
                peso=round(random.uniform(5, 30), 1),
                estado_salud=random.choice(salud),
                vacunado=random.choice([True, False]),
                estado=random.choice(estados),
                temperamento=random.choice(temperamentos),
                url_imagen=url
            )

        # Crear usuarios
        for i in range(5):
            UsuarioAdoptante.objects.create(
                nombre=f'Usuario {i+1}',
                dni=f'1234567{i}',
                email=f'usuario{i+1}@test.com',
                preferencias_raza=random.choice(razas),
                preferencias_edad=random.randint(1, 10),
                preferencias_tamaño=random.choice(tamaños)
            )

        self.stdout.write(self.style.SUCCESS('✅ Se generaron perros y usuarios dummy con éxito.'))
