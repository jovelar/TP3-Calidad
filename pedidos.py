DESCUENTOS_SOCIO = {"electronica": 0.10, "ropa": 0.20, "alimento": 0.05}


def subtotal_item(item, es_socio):
    descuento = DESCUENTOS_SOCIO.get(item["tipo"])
    if descuento is None:
        return 0
    subtotal = item["precio"] * item["cantidad"]
    return subtotal * (1 - descuento) if es_socio else subtotal


def calcular_subtotal(pedido, cliente):
    if not pedido or not pedido["items"]:
        return 0
    return sum(subtotal_item(item, cliente["socio"]) for item in pedido["items"])


def aplicar_bonificacion(total):
    return total - 500 if total > 10000 else total


def procesar_pedido(pedido, cliente):
    return aplicar_bonificacion(calcular_subtotal(pedido, cliente))


def procesar_presupuesto(pedido, cliente):
    return calcular_subtotal(pedido, cliente)
