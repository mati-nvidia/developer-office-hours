import omni.kit.commands
import omni.kit.undo

# Requires Ctrl+Z twice to undo
omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
	prim_type='Cube')
omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
	prim_type='Cube')


# Grouped into one undo
with omni.kit.undo.group():
    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
	    prim_type='Cube')
    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
        prim_type='Cube')