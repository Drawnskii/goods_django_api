# 📌 Django Goods Management API

Este proyecto es una API de gestión de bienes (goods) desarrollada con Django y PostgreSQL.

## 🚀 Requisitos previos

Antes de empezar, asegúrate de tener instalado:

- **Python** (>=3.7)
- **PostgreSQL** (>=12)
- **Git**
- **Virtualenv** (opcional, pero recomendado)

---

## 🔹 1. Clonar el repositorio
```bash
git clone https://github.com/Drawnskii/goods_django_api.git
cd goods_django_api
```

---

## 🔹 2. Crear y activar un entorno virtual

### 🔹 En Windows (cmd / PowerShell):
```powershell
python -m venv venv
venv\Scripts\activate
```

### 🔹 En macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

> **Nota**: Siempre activa el entorno virtual antes de ejecutar comandos de Django.

---

## 🔹 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## 🔹 4. Configurar variables de entorno
Crea un archivo **`.env`** en la raíz del proyecto y agrega:

```env
DB_NAME=goods_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

---

## 🔹 5. Aplicar migraciones y crear superusuario
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Sigue las instrucciones para establecer el usuario y contraseña del administrador.

---

## 🔹 6. Correr el servidor
```bash
python manage.py runserver
```
Abre en tu navegador: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🔹 7. Acceder al Panel de Administración de Django
Dirígete a **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)** e ingresa con el superusuario que creaste.

---

## 📌 Extras

- **Para salir del entorno virtual**:
  - Windows: `deactivate`
  - macOS/Linux: `deactivate`

- **Si cambias dependencias**, actualiza `requirements.txt`:
```bash
pip freeze > requirements.txt
```

¡Listo! 🎉 Ahora puedes empezar a desarrollar 🚀
