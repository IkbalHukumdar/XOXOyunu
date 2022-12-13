import random


tahta = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
mevcutOyuncu = "X"
kazanan = None
gameRunning = True


def printtahta(tahta):
    print(tahta[0] + " | " + tahta[1] + " | " + tahta[2])
    print("---------")
    print(tahta[3] + " | " + tahta[4] + " | " + tahta[5])
    print("---------")
    print(tahta[6] + " | " + tahta[7] + " | " + tahta[8])


# oyuncu girişi
def playerInput(tahta):
    inp = int(input("1-9 arasında sayı seçin: "))
    if tahta[inp-1] == "-":
        tahta[inp-1] = mevcutOyuncu
    else:
        print("Bu oyuncu vardı.")


# galibiyeti veya beraberliği kontrol et
def kontrolHorizontle(tahta):
    global kazanan
    if tahta[0] == tahta[1] == tahta[2] and tahta[0] != "-":
        kazanan = tahta[0]
        return True
    elif tahta[3] == tahta[4] == tahta[5] and tahta[3] != "-":
        kazanan = tahta[3]
        return True
    elif tahta[6] == tahta[7] == tahta[8] and tahta[6] != "-":
        kazanan = tahta[6]
        return True

def kontrolRow(tahta):
    global kazanan
    if tahta[0] == tahta[3] == tahta[6] and tahta[0] != "-":
        kazanan = tahta[0]
        return True
    elif tahta[1] == tahta[4] == tahta[7] and tahta[1] != "-":
        kazanan = tahta[1]
        return True
    elif tahta[2] == tahta[5] == tahta[8] and tahta[2] != "-":
        kazanan = tahta[3]
        return True


def kontrolDiag(tahta):
    global kazanan
    if tahta[0] == tahta[4] == tahta[8] and tahta[0] != "-":
        kazanan = tahta[0]
        return True
    elif tahta[2] == tahta[4] == tahta[6] and tahta[4] != "-":
        kazanan = tahta[2]
        return True


def kontrolIfWin(tahta):
    global gameRunning
    if kontrolHorizontle(tahta):
        printtahta(tahta)
        print(f"kazanan {kazanan}!")
        gameRunning = False

    elif kontrolRow(tahta):
        printtahta(tahta)
        print(f"kazanan  {kazanan}!")
        gameRunning = False

    elif kontrolDiag(tahta):
        printtahta(tahta)
        print(f" kazanan  {kazanan}!")
        gameRunning = False


def kontrolIfTie(tahta):
    global gameRunning
    if "-" not in tahta:
        printtahta(tahta)
        print("Kaybettin!")
        gameRunning = False


# oyuncu değisikligi
def oyuncuDegisikligi():
    global mevcutOyuncu
    if mevcutOyuncu == "X":
        mevcutOyuncu = "O"
    else:
        mevcutOyuncu = "X"


def computer(tahta):
    while mevcutOyuncu == "O":
        position = random.randint(0, 8)
        if tahta[position] == "-":
            tahta[position] = "O"
            oyuncuDegisikligi()


while gameRunning:
    printtahta(tahta)
    playerInput(tahta)
    kontrolIfWin(tahta)
    kontrolIfTie(tahta)
    oyuncuDegisikligi()
    computer(tahta)
    kontrolIfWin(tahta)
    kontrolIfTie(tahta)

