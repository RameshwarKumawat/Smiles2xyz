from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt

coronene_g_smiles = 'c1cc2ccc3ccc4ccc5ccc6ccc1c7c2c3c4c5c67'
coronene_g = Chem.MolFromSmiles(coronene_g_smiles)
Draw.MolToMPL(coronene_g, size=(100, 100))
