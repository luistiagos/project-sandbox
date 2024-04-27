import pandas as pd


def getPurchaseLink(sid):
    id = int(sid)
    df = pd.read_csv('./roms/fileprodutoidmp_out.csv', sep=';')
    return df[df['ID'] == id]['DELIVERLINK'].values[0].strip()
    #return df.loc[[id]]['DELIVERLINK'].values[0].strip()


print(getPurchaseLink('20000'))