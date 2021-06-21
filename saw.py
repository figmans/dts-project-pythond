#Simple additive weighting___
#Autor : Ikhsan Maulana 

def raise_(ex):
    raise ex

# konversi input data (halaman 39 - 40)
def simplifikasi(raw):
    sdata = raw
    for baris in sdata:
        # mapping Masssa Kerja
        if float(baris[1]) <= 5:
            baris[1] = (float(baris[1]) - 1) / 5
        else:
            baris[1] = float(1.0)

        # mapping Penilaian Kinerja
        if round(float(baris[2])) <= 1:
            baris[2] = float(0.2)
        elif round(float(baris[2])) == 2:
            baris[2] = float(0.3)
        elif round(float(baris[2])) == 3:
            baris[2] = float(0.5)
        elif round(float(baris[2])) == 4:
            baris[2] = float(0.7)
        elif round(float(baris[2])) == 5:
            baris[2] = float(0.8)
        else:
            baris[2] = float(1)

        # mapping Prilaku
        if round(float(baris[3])) <= 1:
            baris[3] = float(0.2)
        elif round(float(baris[3])) == 2:
            baris[3] = float(0.3)
        elif round(float(baris[3])) == 3:
            baris[3] = float(0.5)
        elif round(float(baris[3])) == 4:
            baris[3] = float(0.7)
        elif round(float(baris[3])) == 5:
            baris[3] = float(0.8)
        else:
            baris[3] = float(1)

    return sdata

    # normalisasi data (halaman 41)
def normalisasi(data,bc):
    if bc[0]:
        massakerja = [nilai/max([baris[1] for baris in data]) for nilai in [baris[1] for baris in data]]
    else:
        massakerja = [min([baris[1] for baris in data])/nilai for nilai in [baris[1] for baris in data]]

    if bc[1]:
        penilaiankerja = [nilai/max([baris[2] for baris in data]) for nilai in [baris[2] for baris in data]]
    else:
        penilaiankerja = [min([baris[2] for baris in data])/nilai for nilai in [baris[2] for baris in data]]

    if bc[2]:
        perilaku = [nilai/max([baris[3] for baris in data]) for nilai in [baris[3] for baris in data]]
    else:
        perilaku = [min([baris[3] for baris in data])/nilai for nilai in [baris[3] for baris in data]]

    return [[data[i][0],massakerja[i],penilaiankerja[i],perilaku[i]] for i in range(len(data))]

    # menentukan rangking (halaman 42)
def rangking(raw, id_penilaian, benefitcost, weight=[0.25, 0.50, 0.25]):
    raw = list([[data[0], data[5], data[6], data[7]] for data in raw if data[1] == id_penilaian])
    w = weight
    konversi = lambda x: 1 if x == 'benefit' else (0 if x == 'cost' else raise_(Exception("isi input benefitcost dengan \"benefit\" atau \"cost\"")) )
    bc = [konversi(data) for data in benefitcost]
    data = simplifikasi(raw)

    return [[data[0],data[1],data[2],data[3],data[1]*w[0]+data[2]*w[1]+data[3]*w[2]] for data in normalisasi(data,bc)]
