import omni.kit.commands
from pxr import Sdf
import omni.usd

omni.kit.commands.execute('CreateReference',
	path_to=Sdf.Path('/World/toy_drummer2'),
	asset_path='C:/Users/mcodesal/Downloads/toy_drummer.usdz',
	usd_context=omni.usd.get_context())


