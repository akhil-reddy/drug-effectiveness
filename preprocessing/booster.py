from tdc.multi_pred import Catalyst
from tdc.multi_pred import DrugSyn
from tdc.utils import get_label_map
from indigo import *
import pandas as pd

indigo = Indigo()

'''catalyst = Catalyst(name = 'USPTO_Catalyst')
label_map = get_label_map(name = 'USPTO_Catalyst', task = 'Catalyst')
drug_smiles = []
catalyst_smiles = []

for reactant, cat in zip(catalyst.entity1, catalyst.y):
    drug = indigo.loadMolecule(reactant)
    drug.aromatize()
    drug_smiles.append(drug.canonicalSmiles())

    catSmile = indigo.loadMolecule(label_map[cat])
    catSmile.aromatize()
    catalyst_smiles.append(catSmile.canonicalSmiles())

catalyst_data = pd.DataFrame(zip(drug_smiles, catalyst_smiles), columns=["Drug1", "catalyst"])

catalyst_data.to_csv("catalyst.csv", sep='\t', encoding='utf-8')
catalyst_data = pd.read_csv('catalyst.csv', '\t')'''

def get_canon_smile(smile):
    canon_smile = indigo.loadMolecule(smile)
    canon_smile.aromatize()
    return canon_smile.canonicalSmiles()

drug_comb = DrugSyn(name = 'DrugComb').df
drug_comb["Drug1"] = drug_comb["Drug1"].apply(get_canon_smile)
drug_comb["Drug2"] = drug_comb["Drug2"].apply(get_canon_smile)

'''drug_comb.to_csv("drug_comb.csv", sep='\t', encoding='utf-8')
drug_comb = pd.read_csv('drug_comb.csv')'''

'''onco_poly = DrugSyn(name = 'OncoPolyPharmacology').df
onco_poly["Drug1"] = onco_poly["Drug1"].apply(get_canon_smile)
onco_poly["Drug2"] = onco_poly["Drug2"].apply(get_canon_smile)

onco_poly.to_csv("onco_poly.csv", sep='\t', encoding='utf-8')'''
onco_poly = pd.read_csv('onco_poly.csv', sep='\t')

joined = pd.merge(drug_comb, onco_poly, how='inner')

# joined = pd.merge(joined, catalyst_data, how='inner')
joined.drop(['Cell_Line', 'CellLine', "Cell_Line_ID", "Unnamed: 0"], axis=1, inplace=True)
joined.to_csv("catalyst_joined.csv", index=False)

