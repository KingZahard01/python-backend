## 🐍 Plan de Estudios Backend Developer con Python

### 🧩 **ETAPA 1: Fundamentos de Programación y Python**

**Duración sugerida:** 4–6 semanas

#### 🔑 Temas clave:

- Sintaxis básica, variables, tipos de datos
- Operadores y estructuras de control (`if`, `for`, `while`)
- Funciones, módulos y paquetes
- Estructuras de datos: listas, diccionarios, sets, tuplas

#### 📘 Recursos:

- [Python Básico – MoureDev](https://www.youtube.com/watch?v=Kp4Mvapo5kc) (gratuito)
- [Hello-Python – MoureDev](https://github.com/mouredev/Hello-Python) (github)

#### 💡 Proyecto sugerido:

- **Gestor de tareas CLI**: Agregar, editar, eliminar y listar tareas con prioridad y estado.

#### ✅ GitHub:

- Repo: `python-backend/basics` con ejercicios y tu proyecto.

---

### ⚙️ **ETAPA 2: Python Intermedio + POO**

**Duración sugerida:** 3–5 semanas

#### 🔑 Temas clave:

- Programación Orientada a Objetos
- Manejo de errores y excepciones
- Lectura/escritura de archivos (`open()`, JSON, CSV)
- List comprehensions y funciones lambda
- Entornos virtuales (`venv`, `pip`, `requirements.txt`)

#### 📘 Recursos:

- [POO desde cero – Soy Dalto](https://www.youtube.com/watch?v=HtKqSJX7VoM) (gratuito)

#### 💡 Proyecto sugerido:

- **Sistema de gestión de biblioteca**: usuarios, libros, préstamos.

#### ✅ GitHub:

- Repo: `python-backend/poo` y documentación del diseño del programa.

---

### 🌐 **ETAPA 3: Backend con Python + FastAPI (o Flask)**

**Duración sugerida:** 6–8 semanas

#### 🔑 Temas clave:

- Fundamentos de APIs REST
- FastAPI o Flask (elige uno para empezar, recomiendo **FastAPI**)
- Rutas, controladores, serialización con Pydantic
- CRUD completo con SQLite/MySQL/PostgreSQL
- Conexión con ORM: **SQLAlchemy** o **Tortoise ORM**

#### 📘 Recursos:

- [FastAPI Docs (oficial)](https://fastapi.tiangolo.com/)
- [Curso FastAPI – FreeCodeCamp](https://www.youtube.com/watch?v=0sOvCWFmrtA)

#### 💡 Proyecto sugerido:

- **API de productos** con endpoints REST y base de datos

#### ✅ GitHub:

- Repo: `python-backend/api` con documentación de rutas, base de datos y pruebas con curl o Postman.

---

### 🔐 **ETAPA 4: Autenticación, Testing y Buenas Prácticas**

**Duración sugerida:** 5–7 semanas

#### 🔑 Temas clave:

- JWT y autenticación con FastAPI (OAuth2PasswordBearer)
- Validaciones con Pydantic
- Testing con `pytest`
- Logs y manejo de errores
- Arquitectura limpia (routers, servicios, repositorios)
- Pruebas unitarias y mocks

#### 💡 Proyecto sugerido:

- **Sistema de login y registro** con JWT y protección de rutas

#### ✅ GitHub:

- Repo: `python-backend/auth` con tests, tokens y protección por roles.

---

### ☁️ **ETAPA 5: DevOps Básico + Despliegue**

**Duración sugerida:** 3–4 semanas

#### 🔑 Temas clave:

- Dockerizar tu API (Dockerfile, docker-compose)
- Uso de `.env`, variables de entorno
- CI/CD con GitHub Actions
- Despliegue en plataformas como Render, Railway o Fly.io

#### 💡 Proyecto sugerido:

- Elige uno anterior y **llévalo a producción**

#### ✅ GitHub:

- Agrega badges, documentación de despliegue y test de salud (`/ping` o `/status`).

---

## 📁 Organización de tu GitHub

1. Un repo por cada etapa/proyecto:

   - `basics`
   - `oop`
   - `api`
   - `auth`
   - `deploy`

2. README.md con:

   - Descripción del proyecto
   - Cómo ejecutarlo localmente
   - Ejemplos de uso (curl, Postman)

3. Diario de aprendizaje:

   - Repo: `python-backend`
   - Cada semana, un archivo o entrada en el README tipo:

```markdown
## Semana 3: POO y manejo de errores

✅ Aprendido:

- `try/except`, clases e instancias
- Métodos mágicos como `__str__`

🚧 Pendiente:

- Pruebas con `unittest`

📁 Proyecto:

- Sistema de biblioteca con persistencia en JSON
```

---

## 💼 Proyectos Finales para Portafolio

- **API de tareas con usuarios, login y permisos**
- **Blog con comentarios, búsqueda y tags**
- **Sistema de finanzas personales**
- **API tipo Trello (tableros, tareas, usuarios)**
