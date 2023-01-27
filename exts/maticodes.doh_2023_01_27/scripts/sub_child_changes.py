# SPDX-License-Identifier: Apache-2.0

# UsdWatcher

from pxr import Sdf, Tf, Usd
import omni.usd

stage = omni.usd.get_context().get_stage()


def changed_paths(notice, stage):
    print("Change fired")
    for p in notice.GetChangedInfoOnlyPaths():
        if str(p).startswith("/World/Parent" + "/"):
            print("Something happened to a descendent of /World/Parent")
            print(p)
    for p in notice.GetResyncedPaths():
        if str(p).startswith("/World/Parent" + "/"):
            print("A descendent of /World/Parent was added or removed")
            print(p)

objects_changed = Tf.Notice.Register(Usd.Notice.ObjectsChanged, changed_paths, None)

objects_changed.Revoke()
