# Smiles2xyz
Smiles to xyz converter python script
Below, I am going to show you how to use openbabel to convert the smiles .smi file into .xyz cartesian co-ordinates.
Steps:
1. Install the openbabel on any linux or ubuntu platform using the following command line on terminal: sudo apt install openbabel

Once the installation done...

2. Type the following command line on your terminal: obabel -ismi filename.smi -oxyz filename.xyz --gen3d

This will generate .xyz file for example coronene molecule. You can save it on your current directory or somewhere else.

3. You can also visualize the 3D structure of coronene either with openbabel or ase, avogadro, chemcraft, vesta, molden, jmol, etc.
