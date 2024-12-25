import math

freqHz = input("Frequencia utilizada(em Hz): ")
freqHz = float(freqHz)

lB = (3 * math.pow(10,8))/(freqHz * math.pow(10,9))
print("Lambda: ", lB)

n = 1
dist1 = input("distancia do ponto até a primeira antena: ")
dist1 = float(dist1)
dist2 = input("distancia do ponto até a segunda antena: ")
dist2 = float(dist2)

R = math.sqrt((n*lB*dist1*dist2)/(dist1+dist2))
print("\nO raio de Fresnel no ponto informado é de", R, "metros...")
