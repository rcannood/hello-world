#/usr/bin/env python

import os
import tempfile
from singularity.package import build_from_spec

tmpdir = tempfile.mkdtemp()
singularityFile = "Singularity"
sudopw = ''
name = 'test'
build_dir = os.getcwd()
size=None

if os.path.exists(singularityFile):

    # Build an image package from the specfile
    image_package = build_from_spec(spec=singularityFile,
                                    name=name,
                                    build_dir=tmpdir,
                                    output_folder=build_dir,
                                    size=size,
                                    sudopw=sudopw)

print(image_package)
#TODO: need to be able to return an error/build failed to user
