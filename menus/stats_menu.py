


def stats_menu(stats):
    print(f"Promedio de gastos de los clientes VIP: ${stats.avgExpenses()}")
    stats.drawTable()
    print("Partido mas asistido: ",stats.mostAssistedMatch())
    print("Partido con mas boletos vendidos: ",stats.mostSoldTicket())
    input("Presione enter para continuar...")

    

