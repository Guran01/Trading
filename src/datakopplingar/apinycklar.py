"""
Datakopplingar – hanterar laddning och validering av API-nycklar från .env-fil.
"""

import os
from dotenv import load_dotenv

def ladda_api_nycklar():
    load_dotenv()

    nycklar = {
        "TWELVEDATA": os.getenv("TWELVEDATA_API_KEY"),
        "POLYGON": os.getenv("POLYGON_API_KEY"),
    }

    if not all(nycklar.values()):
        raise ValueError("En eller flera API-nycklar saknas. Kontrollera .env-filen.")
    
    return nycklar
