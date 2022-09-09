import omni.kit.commands
import omni.kit.primitive.mesh as mesh_cmds

# Creates history
omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
	prim_type='Cube')

# Doesn't create history
mesh_cmds.CreateMeshPrimWithDefaultXformCommand("Cube").do()
