#To install all required modules automatically
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('PyQt5')
install('Image')
install('PyPDF4')
install('wand')
install('PyPDF2')
install('tqdm')
install('natsort')