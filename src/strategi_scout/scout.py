"""
StrategyScout – genererar nya strategier baserat på mätbar edge och signalmönster.
"""

def föreslå_strategier(marknadsdata):
    """
    Returnerar en lista med potentiella strategier baserat på inkommande data.
    TODO: Integrera analys via t.ex. moving averages, RSI, trendkanaler etc.
    """
    strategier = []

    # Exempelstrategi (dummy)
    if marknadsdata[-1]["pris"] > marknadsdata[-20]["pris"]:
        strategier.append("Trendföljande strategi – positiv momentum")

    return strategier
