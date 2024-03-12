from tdc.multi_pred import Catalyst
from tdc.multi_pred import DrugSyn
from tdc.utils import get_label_map
from indigo import *
import pandas as pd

indigo = Indigo()

catalyst = Catalyst(name = 'USPTO_Catalyst')
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

def get_canon_smile(smile):
    canon_smile = indigo.loadMolecule(smile)
    canon_smile.aromatize()
    return canon_smile.canonicalSmiles()

drug_comb = DrugSyn(name = 'DrugComb').df
drug_comb["Drug1"] = drug_comb["Drug1"].apply(get_canon_smile)
drug_comb["Drug2"] = drug_comb["Drug2"].apply(get_canon_smile)

onco_poly = DrugSyn(name = 'OncoPolyPharmacology').df
onco_poly["Drug1"] = onco_poly["Drug1"].apply(get_canon_smile)
onco_poly["Drug2"] = onco_poly["Drug2"].apply(get_canon_smile)

joined = pd.concat([drug_comb,onco_poly], axis=1, join='inner')

joined = pd.concat([joined, catalyst_data], axis=1, join='inner')

