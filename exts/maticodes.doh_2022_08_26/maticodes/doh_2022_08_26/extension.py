import carb
import omni.ext


class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        carb.log_info("[maticodes.doh_2022_08_26] Dev Office Hours Extension (2022-08-26) startup")

    def on_shutdown(self):
        carb.log_info("[maticodes.doh_2022_08_26] Dev Office Hours Extension (2022-08-26) shutdown")
