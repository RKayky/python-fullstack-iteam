metros = float(input("Distância em metros: "))

km = metros / 1000
cm = metros * 100
mm = metros * 1000
polegadas = metros * 39.3701
pes = metros * 3.28084

print(f"{'Quilômetros':<15}: {km:.4f}")
print(f"{'Centímetros':<15}: {cm:.4f}")
print(f"{'Milímetros':<15}: {mm:.4f}")
print(f"{'Polegadas':<15}: {polegadas:.4f}")
print(f"{'Pés':<15}: {pes:.4f}")