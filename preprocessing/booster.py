from tdc.multi_pred import Catalyst
from tdc.multi_pred import DrugSyn
from tdc.utils import get_label_map
from indigo import *

indigo = Indigo()
mol1 = indigo.loadMolecule("CN2C(=O)N(C)C(=O)C1=C2N=CN1C")
mol2 = indigo.loadMolecule("CN1C=NC2=C1C(=O)N(C)C(=O)N2C")
mol1.aromatize()
mol2.aromatize()
print(mol1.canonicalSmiles())
print(mol2.canonicalSmiles())
assert mol1.canonicalSmiles() == mol2.canonicalSmiles()

data = Catalyst(name = 'USPTO_Catalyst')
data2 = DrugSyn(name = 'DrugComb')
data3 = DrugSyn(name = 'OncoPolyPharmacology')

label_map = get_label_map(name = 'USPTO_Catalyst', task = 'Catalyst')
print(label_map)