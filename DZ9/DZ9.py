class OilError(Exception):
    def __str__(self):
        return f"Залишилось мало масла в машині!"
def check_material(amount_of_oil, limit_value):
    if amount_of_oil>limit_value:
        return " матеріалу достатньо"
    else:
        raise OilError(amount_of_oil)
materials=123
check_material(materials,300)

class PetrolError(Exception):
    def __str__(self):
        return f"Мало бензину!"
def check_material(amount_of_petrol, limit_value):
    if amount_of_petrol>limit_value:
        return "Бензину вдосталь!"
    else:
        raise OilError(amount_of_petrol)
materials=123
check_material(materials,300)


class WindowCleaner(Exception):
    def __str__(self):
        return f"Мало омивача!"
def check_material(amount_of_WindowCleaner, limit_value):
    if amount_of_WindowCleaner>limit_value:
        return "Бензину вдосталь!"
    else:
        raise OilError(amount_of_WindowCleaner)
materials=123
check_material(materials,300)
