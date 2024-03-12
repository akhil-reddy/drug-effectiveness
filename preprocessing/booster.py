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

catalyst_data = pd.DataFrame([drug_smiles, catalyst_smiles], columns=["smile", "catalyst"])
drug_comb = DrugSyn(name = 'DrugComb')
onco_poly = DrugSyn(name = 'OncoPolyPharmacology')

