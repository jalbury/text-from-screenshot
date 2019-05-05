import os
import PIL
import tempfile

# create temp file to store screenshot
f = tempfile.NamedTemporaryFile(delete=False)
f.close()

# call internal Mac screenshot tool
os.system('screencapture -i ' + f.name)

# clean-up: delete temp file
os.unlink(f.name)
