from pprint import pprint


def beolvas():
    with open('sneakers.csv') as forras:
        forras.readline()
        cipok = []
        for sor in forras:
            cipo = sor.strip().split(',')
            cipo_adatai = {'title': cipo[0],
                           'color': cipo[1],
                           'full price': cipo[2],
                           'current price': cipo[3],
                           'publish date': cipo[4]
                           }
            cipok.append(cipo_adatai)
    return cipok


def valaszt():
    print('Válassz, melyik szempont alapján rendezzem a cipőket? ')
    lehetosegek = ['title', 'color', 'full price', 'current price', 'publish date']
    for index, lehetoseg in enumerate(lehetosegek):
        print(f'{index + 1} - {lehetoseg}')
    valasztas = int(input('Add meg a lehetőség számát! '))
    print()
    return lehetosegek[valasztas - 1]


def main():
    valasztas = valaszt()
    cipok = beolvas()
    pprint(sorted(cipok, key=lambda cipo: cipo[valasztas]))


main()
