#Protein Property Analyzer: Hydrophobicity, Charge, Solubility, Molecular Weight, and Location Prediction Using Python

hydrophobic = "GAVLIPMWYF"
positive = "HRK"
negative = "DE"

#molecular weight of aa 
mw = {
    'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1, 'C': 121.2,
    'E': 147.1, 'Q': 146.2, 'G': 75.1,  'H': 155.2, 'I': 131.2,
    'L': 131.2, 'K': 146.2, 'M': 149.2, 'F': 165.2, 'P': 115.1,
    'S': 105.1, 'T': 119.1, 'W': 204.2, 'Y': 181.2, 'V': 117.1
}
seq = input("Enter protein sequence :").upper()

hphob = 0
pos = 0
neg = 0


for aa in seq:
    if aa in hydrophobic:
        hphob += 1
    if aa in positive:
        pos += 1
    if aa in negative:
        neg += 1
    
weight = 0
for aa in seq:
    weight += mw.get(aa, 0)
if len(seq) > 1:
    weight = weight - (len(seq) - 1) * 18.02


# charge model
charge_pH3 = pos
charge_pH7 = pos*0.3 - neg*0.3
charge_pH11 = -neg
# Solubility predication
ratio = hphob / len(seq)
if ratio > 0.5:
    sol = "Low"
if ratio > 0.3:
    sol = "Medium"
else:
    sol = "High"

# Location prediction
if ratio > 0.45:
    location = "Membrane bound protein"
else:
    location = "Cytosolic protein"

print("\n---- Protein Report ----")
print("Length:", len(seq))
print("Hydrophobic:", hphob, "aa")
print("Positive:", pos, "aa")
print("Negative:", neg, "aa")
print("Molecular Weight:", weight, "Da")
print("Charge at pH3: ~", charge_pH3)
print("Charge at pH7: ~", charge_pH7)
print("Charge at pH11: ~", charge_pH11)
print("Solubility:", sol)
print("Predicted Location:", location)                               
