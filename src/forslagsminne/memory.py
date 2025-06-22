"""
Förslagsminne – lagrar strategiförslag som användaren pausat eller avböjt.
"""

lagrat_förslag = []

def spara_förslag(förslag):
    lagrat_förslag.append(förslag)

def hämta_arkiv():
    return lagrat_förslag
