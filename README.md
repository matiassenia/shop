# PASIÓN POR LA CAMISETA
# Tienda Online de Camisetas de Fútbol

Este es un proyecto de tienda en línea desarrollado con Django. Permite a los usuarios navegar por una colección de remeras, agregar artículos a un carrito de compras, y realizar acciones como registrarse, iniciar sesión y gestionar su carrito de compras.

## Características

- **Registro y Autenticación de Usuarios**: Los usuarios pueden registrarse, iniciar sesión y cerrar sesión.
- **Gestión de Remeras**: Los usuarios pueden ver todas las remeras disponibles.
- **Carrito de Compras**: Funcionalidades para agregar, actualizar y eliminar artículos en el carrito de compras.
- **Página de Contacto**: Los usuarios pueden acceder a una página de contacto.

## Requisitos Previos

- Python 3.12.1 o superior
- Django 5.0.3
- Base de datos (por defecto SQLite, pero puede configurarse otra)

## Instalación


1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

2. **Instala las dependencias del proyecto utilizando pip:**

   ```bash
   pip install -r requirements.txt

3. **Realiza las migraciones de la base de datos:**

    ```bash
    python manage.py migrate

4. **Inicia el servidor de desarrollo:**

    ```bash
    python manage.py runserver

5. **Visita http://127.0.0.1:8000/shop en tu navegador web para ver la aplicación.**

## Uso
**Registro de Usuario**

Navega a /shop/registro/ para crear una nueva cuenta de usuario.
**Inicio de Sesión**

Navega a /shop/login/ para iniciar sesión en tu cuenta.
**Ver Productos**

La página principal /shop/home/ mostrará una lista de todas las camisetas disponibles.
**Agregar al Carrito**

En la vista de detalles de una remera, puedes agregarla al carrito.
**Ver Carrito**

Navega a /shop/carrito/ para ver los artículos en tu carrito, actualizar cantidades o **eliminar artículos.**

**Contacto**
Navega a /shop/contacto/ para ver la página de contacto.

# Estructura del Proyecto
**shop: Aplicación principal con vistas, modelos, formularios y templates.**
**templates: Carpeta de plantillas HTML para renderizar vistas.**
**static: Archivos estáticos (CSS, JS, imágenes).**


