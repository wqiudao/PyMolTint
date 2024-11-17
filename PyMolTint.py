import json
from pymol import cmd
from pymol.cgo import * 

"""
af2color json_file

Set colors for atoms in the loaded PDB file based on the atom_plddts values from the JSON file.
Parameters:
- `json_file`: Path to the JSON file containing the atom_plddts values

The JSON file is located in PyMOL's current working directory; otherwise, the full path is required.

--------------------------------------

show_residue_sphere residue_number,sph_radius,sph_color

show_residue_sphere, which adds a colored sphere at the position of a specified residue in the loaded structure. 

Input Parameters:
	residue_number: The residue number to mark with a sphere. Defaults to 1.
	sph_radius: The radius of the sphere. Defaults to 2.
	sph_color: The color of the sphere, provided as a space-separated RGB string (e.g., '1.0 0.0 0.0' for red).

"""


def af2color(json_file):

	with open(json_file, 'r') as f:
		data = json.load(f)
	plddts = data["atom_plddts"]
	atoms = cmd.get_model("all").atom
	if len(atoms) != len(plddts):
		print("Warning: The number of atoms does not match the number of plddts data!")
		return
	for i, atom in enumerate(atoms):
		plddt = plddts[i]
		if plddt >= 90:
			color_name = "neptunium"
		elif 70 <= plddt < 90:
			color_name = "cyan"
		elif 50 <= plddt < 70:
			color_name = "gold"
		else:
			color_name = "phosphorus"
		atom_selection = f"id {atom.index}"
		cmd.color(color_name, atom_selection)
cmd.extend("af2color", af2color)




def show_residue_sphere(residue_number=1,sph_radius=2,sph_color='1.0 0.0 0.0'):
	print(sph_color)
	residue_number=int(residue_number)
	sph_radius=int(sph_radius)
	residue_number = max(residue_number,1)

	sph_colors = [float(color) for color in re.split(r'\s+',sph_color)]
	if max(sph_colors)>1:
		sph_colors=[1,0,0]	
	print(f'residue_number: {residue_number}\nsph_colors:{sph_colors}')	
	objects = cmd.get_object_list()
	if objects:
		chains = cmd.get_chains(objects[0])
		selection = f'chain {chains[0]} and resi {residue_number}'
		if cmd.count_atoms(selection) == 0:
			print(f"Error: The selected residue '{selection}' does not exist!")
		else:
			residue_xyzs = cmd.get_coords(selection, 1)
			x, y, z = residue_xyzs[0]
			sphere_name=f'residue_{chains[0]}_{residue_number}'
			if sphere_name in cmd.get_names():
				cmd.delete(sphere_name) 
				print(f"Existing object '{sphere_name}' has been deleted.")
			cmd.load_cgo([COLOR, sph_colors[0], sph_colors[1], sph_colors[2], SPHERE, x, y, z, sph_radius], sphere_name)
	else: 
		print("Error: No available structure objects found. Please load a structure first.")
		
cmd.extend("show_residue_sphere", show_residue_sphere)








