# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from pathlib import Path
from types import MethodType

from .._input_field import InputField


class TextInput(InputField):

    dtype = str

    _type = "textinput"

    _default = {
        "width": "s100%",
        "params": {
            "placeholder": "Write your value here...",
        }
    }

from sisl import BaseSile

if not hasattr(BaseSile, "to_json"):
    # Little patch so that Siles can be sent to the GUI
    def sile_to_json(self):
        return str(self.file)

    BaseSile.to_json = sile_to_json


class FilePathInput(TextInput):

    _default = {
        "width": "s100%",
        "params": {
            "placeholder": "Write your path here...",
        }
    }

    def parse(self, val):

        if isinstance(val, BaseSile):
            val = val.file

        if isinstance(val, str):
            val = Path(val)

        return val
