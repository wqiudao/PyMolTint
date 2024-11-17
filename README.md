# PyMolTint
PyMolTint is a PyMOL plugin designed to enhance the visualization of molecular structures by allowing users to easily highlight specific residues with color and markers. This tool simplifies the process of marking residues with colored spheres, helping to emphasize important areas in a molecular structure for better analysis and presentation.
1. **af2color:** set colors for atoms in the loaded PDB file based on the atom_plddts values from the JSON file.
2. **show_residue_sphere:**  adds a colored sphere at the position of a specified residue in the loaded structure.
## 1. af2color

# AF2Color

Set colors for atoms in the loaded PDB file based on the atom_plddts values from the JSON file.
Parameters:
- `json_file`: Path to the JSON file containing the atom_plddts values

The JSON file is located in PyMOL's current working directory; otherwise, the full path is required.

<pre> af2color json_file  </pre>

### Data Preparation
We need to prepare three files, located in the same directory:

  1. The script `af2color_local.py`, which needs to be downloaded to the local machine.
  2. The Alphafold prediction result files, including `PDB` or `CIF` format structure files, as well as the corresponding `JSON` format files containing pLDDT values (The predicted local distance difference test).
  3. Structural predictions can be obtained through Alphafold3 online (https://golgi.sandbox.google.com/), which is very fast, but currently limited to 20 predictions per day. Alternatively, you can download from the Alphafold database.
  <img src="https://github.com/wqiudao/PyMolTint/blob/main/imgs/AF2Color/af2color_data.png" alt="Alt text" width="800">
-
  <img src="https://github.com/wqiudao/PyMolTint/blob/main/imgs/AF2Color/af2color0.png" alt="Alt text" width="800">
-

### install & run
1. Open the structure file using PyMOL，and in the command line, enter the code to load the `af2color` function.
<pre> run af2color_local.py  </pre>
2. Color structures.
<pre> af2color fold_5xwp_full_data_0.json  </pre>
-
<img src="https://github.com/wqiudao/PyMolTint/blob/main/imgs/AF2Color/af2color1.png" alt="Alt text" width="1200">
-
<img src="https://github.com/wqiudao/PyMolTint/blob/main/imgs/AF2Color/af2color2.png" alt="Alt text" width="1200">
-
<img src="https://github.com/wqiudao/PyMolTint/blob/main/imgs/AF2Color/af2color3.png" alt="Alt text" width="1200">
-
<img src="https://github.com/wqiudao/PyMolTint/blob/main/imgs/AF2Color/af2color4.png" alt="Alt text" width="1200">
-
-
<img src="https://github.com/wqiudao/PyMolTint/blob/main/imgs/AF2Color/af2color_legend.png" alt="Alt text" width="600">

















## 2. show_residue_sphere







