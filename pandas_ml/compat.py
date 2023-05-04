#!/usr/bin/env python

from distutils.version import LooseVersion

import pandas as pd
from pandas.api.types import is_list_like, is_integer_dtype         # noqa

PANDAS_VERSION = LooseVersion(pd.__version__)

_PANDAS_ge_023 = PANDAS_VERSION >= LooseVersion('0.23')
_PANDAS_ge_022 = PANDAS_VERSION >= LooseVersion('0.22')
if PANDAS_VERSION >= LooseVersion('0.21'):
    from pandas.util import Appender, cache_readonly              # noqa
    import pandas.plotting as plotting                            # noqa
    _PANDAS_ge_021 = True
else:
    from pandas.util.decorators import Appender, cache_readonly   # noqa
    import pandas.tools.plotting as plotting                      # noqa
    _PANDAS_ge_021 = False

try:
    import sklearn
    _SKLEARN_INSTALLED = True
    _SKLEARN_ge_019 = sklearn.__version__ >= LooseVersion('0.19')

except ImportError:
    _SKLEARN_INSTALLED = False
    _SKLEARN_ge_019 = False


try:
    import imblearn                 # noqa
    _IMBLEARN_INSTALLED = True
except ImportError:
    _IMBLEARN_INSTALLED = False
