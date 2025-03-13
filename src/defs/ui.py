import os
import sys

main_module = str(sys.modules["__main__"].__file__)
ROOT_DIR = os.path.dirname(main_module)
ASSETS_PATH = f"{ROOT_DIR}/assets"
STYLESHEET_PATH = f"{ASSETS_PATH}/style.tcss"
