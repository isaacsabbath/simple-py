# to make the project a package one must have an init file
from . import module1
from . import module2

# the typical steps to create a package
# 1. project folder with its package name
# 2. create an __init__.py file
# 3. create the required modules
# 4. in the __init__.py file add code to reference the modules needed in the package.
# 5. after creating the package, you need to verify the package
#
#