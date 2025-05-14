class Sala:
    def __init__(self, nom: str, capacitat: int):
        self.nom = nom
        self.capacitat = capacitat

class Usuari:
    def __init__(self, nom: str, correu: str):
        self.nom = nom
        self.correu = correu
        self.reserves = []

    def afegir_reserva(self, reserva):
        self.reserves.append(reserva)

class Reserva:
    def __init__(self, data: str, hora_inici: str, hora_fi: str, sala: Sala, usuari: Usuari):
        self.data = data
        self.hora_inici = hora_inici
        self.hora_fi = hora_fi
        self.sala = sala
        self.usuari = usuari

# Exemple d'ús:
if __name__ == "__main__":
    sala1 = Sala("Aula 1", 30)
    usuari1 = Usuari("Joan", "joan@example.com")

    reserva1 = Reserva("2025-05-15", "10:00", "12:00", sala1, usuari1)
    usuari1.afegir_reserva(reserva1)

    print(f"Usuari: {usuari1.nom}, Correu: {usuari1.correu}")
    print(f"Ha fet {len(usuari1.reserves)} reserva:")
    for r in usuari1.reserves:
        print(f"- Data: {r.data}, Inici: {r.hora_inici}, Fi: {r.hora_fi}, Sala: {r.sala.nom}")