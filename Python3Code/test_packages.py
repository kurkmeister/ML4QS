#!/usr/bin/env python3
"""
Test script to verify all packages are working correctly
"""

try:
    import numpy as np
    print(f'✅ NumPy: {np.__version__}')
except ImportError as e:
    print(f'❌ NumPy failed: {e}')

try:
    import pandas as pd
    print(f'✅ Pandas: {pd.__version__}')
except ImportError as e:
    print(f'❌ Pandas failed: {e}')

try:
    import matplotlib.pyplot as plt
    import matplotlib
    print(f'✅ Matplotlib: {matplotlib.__version__}')
except ImportError as e:
    print(f'❌ Matplotlib failed: {e}')

try:
    import sklearn
    print(f'✅ Scikit-learn: {sklearn.__version__}')
except ImportError as e:
    print(f'❌ Scikit-learn failed: {e}')

try:
    import scipy
    print(f'✅ SciPy: {scipy.__version__}')
except ImportError as e:
    print(f'❌ SciPy failed: {e}')

try:
    import nltk
    print(f'✅ NLTK: {nltk.__version__}')
except ImportError as e:
    print(f'❌ NLTK failed: {e}')

try:
    import statsmodels
    print(f'✅ Statsmodels: {statsmodels.__version__}')
except ImportError as e:
    print(f'❌ Statsmodels failed: {e}')

try:
    import gensim
    print(f'✅ Gensim: {gensim.__version__}')
except ImportError as e:
    print(f'❌ Gensim failed: {e}')

try:
    import pykalman
    print(f'✅ PyKalman: Available')
except ImportError as e:
    print(f'❌ PyKalman failed: {e}')

try:
    import pyclust
    print(f'✅ Pyclust: Available')
except ImportError as e:
    print(f'❌ Pyclust failed: {e}')

try:
    import treelib
    version = getattr(treelib, '__version__', 'Available')
    print(f'✅ Treelib: {version}')
except ImportError as e:
    print(f'❌ Treelib failed: {e}')

try:
    import inspyred
    print(f'✅ Inspyred: Available')
except ImportError as e:
    print(f'❌ Inspyred failed: {e}')

try:
    from unidecode import unidecode
    print(f'✅ Unidecode: Available')
except ImportError as e:
    print(f'❌ Unidecode failed: {e}')

print("\n🎉 Package installation test completed!")
