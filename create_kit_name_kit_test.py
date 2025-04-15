import data
import sender_stand_request

#Cambiar parametro de "name"

def get_user_body(name_kit):
    current_body = data.kit_body.copy()
    current_body['name'] = name_kit
    return current_body

#Función para generar el "authToken"

def get_new_user_token():
    resp_user = sender_stand_request.post_new_user(data.user_body.copy())
    token = resp_user.json()["authToken"]
    new_token = data.headers.copy()
    new_token["Authorization"] = f"Bearer {token}"
    return new_token

#Pruebas positivas

def positive_assert(name_kit):
    kit_body = get_user_body(name_kit)

    positive_kit_response = sender_stand_request.post_new_kit(kit_body, get_new_user_token())
    assert positive_kit_response.status_code == 201
    assert positive_kit_response.json()['name'] == name_kit


#Pruebas negativas

def negative_assert(name_kit):
    kit_body = get_user_body(name_kit)
    negative_kit_response = sender_stand_request.post_new_kit(kit_body, get_new_user_token())
    assert negative_kit_response.status_code == 400
    assert negative_kit_response.json()['code'] == 400


#PRUEBAS

# 1. El número permitido de caracteres (1)

def test_caracteres_1():
    positive_assert(data.caract_1)


# 2. El número permitido de caracteres (511)

def test_caracteres_511():
    positive_assert(data.caract_511)

# 3. Número de caracteres (0)

def test_caracteres_0():
    negative_assert(data.caract_0)

# 4. El número de caracteres es (512)

def test_caracteres_512():
    negative_assert(data.caract_512)

# 5. Se permiten caracteres especiales

def test_caracteres_especiales():
    positive_assert(data.caract_especiales)

# 6. Se permiten espacios

def test_permiten_espacios():
    positive_assert(data.espacios)

# 7. Se permiten números

def test_permiten_numeros():
    positive_assert(data.numeros)

# 8. Parámetro no se pasa en la solicitud

def test_parametro_no_se_pasa_en_la_solicitud():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)

# 9 Parámetro diferente (número)

def test_tipo_parametro_diferente():
    negative_assert(data.param_diferente)
