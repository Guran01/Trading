"""
Komponenter – stödlogik för UI eller framtida grafiska gränssnitt.
"""

def visa_meny(titel, alternativ):
    print(f"📋 {titel}")
    for i, alt in enumerate(alternativ, 1):
        print(f"[{i}] {alt}")

    val = input("Ange val: ")
    return int(val)
