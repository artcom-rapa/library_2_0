#!C:\Users\artcom\kodilla\library_2_0\library_2_0\libr_env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'coverage==4.0.1','console_scripts','coverage-3.8'
__requires__ = 'coverage==4.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('coverage==4.0.1', 'console_scripts', 'coverage-3.8')()
    )
