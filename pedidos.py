def procesar_pedido(pedido, cliente):
    total = 0
    if pedido is not None:
        if pedido["items"]:
            for item in pedido["items"]:
                if item["tipo"] == "electronica":
                    if cliente["socio"]:
                        total += item["precio"] * item["cantidad"] * 0.9
                    else:
                        total += item["precio"] * item["cantidad"]
                elif item["tipo"] == "ropa":
                    if cliente["socio"]:
                        total += item["precio"] * item["cantidad"] * 0.8
                    else:
                        total += item["precio"] * item["cantidad"]
                elif item["tipo"] == "alimento":
                    if cliente["socio"]:
                        total += item["precio"] * item["cantidad"] * 0.95
                    else:
                        total += item["precio"] * item["cantidad"]
            if total > 10000:
                total = total - 500
    return total


def procesar_presupuesto(pedido, cliente):
    total = 0
    if pedido is not None:
        if pedido["items"]:
            for item in pedido["items"]:
                if item["tipo"] == "electronica":
                    if cliente["socio"]:
                        total += item["precio"] * item["cantidad"] * 0.9
                    else:
                        total += item["precio"] * item["cantidad"]
                elif item["tipo"] == "ropa":
                    if cliente["socio"]:
                        total += item["precio"] * item["cantidad"] * 0.8
                    else:
                        total += item["precio"] * item["cantidad"]
                elif item["tipo"] == "alimento":
                    if cliente["socio"]:
                        total += item["precio"] * item["cantidad"] * 0.95
                    else:
                        total += item["precio"] * item["cantidad"]
    return total
