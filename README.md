# Proyecto Urban Grocers

## Estructura del Proyecto

```
- configuration.py             # Rutas base y endpoints de la API
- data.py                      # Datos de entrada utilizados en las solicitudes (cuerpos)
- sender_stand_request.py      # Funciones que envían las solicitudes a la API
- create_kit_name_kit_test.py  # Archivo principal con las pruebas automatizadas
- README.md                    # Este archivo
- .gitignore                   # Archivos que deben ignorarse en Git
```

---

## Escenarios de Prueba Incluidos

Este proyecto valida los siguientes escenarios en la creación de kits:

1. Creación con 1 carácter
2. Creación con 511 caracteres
3. Creación con 0 caracteres (error esperado)
4. Creación con 512 caracteres (error esperado)
5. Nombre con caracteres especiales
6. Nombre con espacios
7. Nombre con números
8. Sin pasar el campo "name" (error esperado)
9. Tipo de dato incorrecto ("name" como número) (error esperado)

---

## Herramientas utilizadas

- Python 
- Pytest
- Requests
- Git

