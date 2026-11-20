import copy, os
MES={"Mar":"Mar","Apr":"Abr","May":"May","Jun":"Jun","Jul":"Jul","Aug":"Ago","Sep":"Sep","Oct":"Oct","Nov":"Nov"}
De=copy.deepcopy(D)
for m in De["months"]:
    k,y=m["label"][:3],m["label"][3:]; m["label"]=MES[k]+y
De["visits"]=[dict(month=MES[v["month"]],n=v["n"]) for v in De["visits"]]
De["comm"]=[dict(period="25 de marzo – 30 de junio de 2026",sales=s1,comm=c1,status="Pagado · 3 de julio de 2026"),
 dict(period="1 de julio – 31 de octubre de 2026",sales=s2,comm=c2,status="Pagado · 18 de noviembre de 2026"),
 dict(period="Noviembre 2026 en adelante",sales=0,comm=0,status="Próximo pago después del 31 de enero de 2027")]
De["work"]=[
 dict(k="Visitas de servicio desde la instalación",v=f"≈{nv}",p="Hasta dos veces por semana de marzo a junio, mientras estabilizábamos la máquina y su mezcla de productos; después, más o menos una vez por semana."),
 dict(k="Horas por visita",v=f"{HPV:g} h",p="2 h de manejo (cerca de una hora de ida y otra de vuelta desde nuestra bodega), 1.5 h en el lugar y 4 h comprando producto, planeando el surtido y revisando ventas."),
 dict(k="Nuestro tiempo hasta ahora",v=f"≈{hrs:,.0f} h",p="Todo pagado por Buenavyda, más la gasolina de cada viaje. Nada se descuenta del 10% de la clínica."),
 dict(k="Máquina, entregada e instalada",v="+$10,000",p="Máquina vending combinada, lector de tarjetas Nayax, monedero, aceptador de billetes, $269 en monedas para cambio, entrega en el lugar y 13% de HST. Montos en CAD."),
 dict(k="Peticiones atendidas",v="3",p="Chicles en lugar de jugo, el regreso de Dr Pepper y opciones de Fanta, cada una cambiada en la siguiente visita."),
]
De["inv"]=[dict(item="Una máquina vending moderna en el lugar, con pago con tarjeta, efectivo y monedas, entregada e instalada",amt=9731.00,how="Facturas del proveedor"),
 dict(item="Cambio para quien paga en efectivo, siempre cargado",amt=269.00,how="Facturas del proveedor"),
 dict(item="Una máquina llena de productos desde el primer día",amt=255,how="≈208 artículos a nuestro costo (cerca de la mitad del precio de venta)"),
 dict(item=f"≈{hrs:,.0f} horas de servicio: surtido, limpieza, efectivo, reparaciones y planeación",amt=round(labour),how="$25/h más CPP patronal 5.95%, EI 2.28%, 4% de vacaciones y ≈5% de nómina y contabilidad"),
 dict(item=f"≈{km:,} km de viajes para mantener la máquina llena",amt=round(drive),how=f"{nv} viajes redondos de ≈200 km a la tarifa CRA 2026 (73¢ los primeros 5,000 km, 67¢ después)")]
CATS_ES={"Cans & drinks":"Latas y bebidas","Chocolate":"Chocolates","Bottles":"Botellas","Gummies & gum":"Gomitas y chicles","Chips & Takis":"Papas y Takis"}
De["cats"]=[dict(c,name=CATS_ES[c["name"]]) for c in De["cats"]]
PR_ES={"Large gummies (Maynards)":"Gomitas grandes (Maynards)","Coca-Cola can":"Coca-Cola lata","Coke Zero bottle":"Coca-Cola Zero botella","Coca-Cola bottle":"Coca-Cola botella","Small gummies":"Gomitas chicas","Coke Zero can":"Coca-Cola Zero lata","Pepsi bottle":"Pepsi botella","Pepsi can":"Pepsi lata"}
De["products"]=[dict(p,name=PR_ES.get(p["name"],p["name"])) for p in De["products"]]
repe=dict(rep)
repe.update({"__ASOF__":"18 de noviembre de 2026","__START__":"25 de marzo de 2026",
 "__INVNOTE__":"Los valores del equipo vienen de las facturas del proveedor. Las horas de servicio y los viajes se valúan a lo que le costaría a la clínica contratar a alguien para hacer el mismo trabajo. El surtido después de la primera carga se paga con las ventas, así que no se cuenta dos veces.",
 "__F3__":f"<b>Buenavyda ha aportado cerca de ${invT:,.0f} de valor</b> a la clínica en equipo, productos, servicio y viajes, sin costo para la clínica. Además, la clínica ha ganado ${c1+c2:,.2f}: el 10% de cada venta, sin nada del costo ni del riesgo.",
 "__MONTHNOTE__":"*Marzo cuenta desde la instalación el 25 de marzo. La división tarjeta/efectivo se muestra desde julio. Fuente: Nayax; marzo a junio de los registros mensuales de Buenavyda.",
 "__F1__":f"<b>${total:,.0f} vendidos en poco más de siete meses</b>, con el mejor mes en mayo (${max(full):,.0f}). La mayoría paga en efectivo, por eso la máquina acepta ambos y recogemos y contamos el efectivo en cada visita.",
 "__F2__":"<b>La mayoría de las compras son en la noche, entre las 8 y las 11 pm</b>, con un pico menor a la hora de la comida. Dejamos la máquina llena antes de las noches y los fines de semana.",
 "__HEATNOTE__":"Muestra: 13 al 17 de noviembre de 2026 (43 compras). Horas en hora de Toronto.","__PERIOD__":"11 de octubre al 17 de noviembre: 319 unidades",
 "__WORKNOTE__":f"Estimado con nuestros registros de visitas: dos veces por semana de marzo a junio, más o menos semanal desde julio. Cada visita cuenta {HPV:g} horas de tiempo de Buenavyda.",
 "__DATA__":json.dumps(De)})
os.makedirs("es",exist_ok=True)
render("template_es.html",De,repe,"es/index.html")
h=open("es/index.html").read()
h=h.replace('<button data-v="cnt">Compras</button>','').replace('thousands of compras · 7 meses completos','25 de marzo al 31 de octubre · 7 meses completos')
open("es/index.html","w").write(h)
