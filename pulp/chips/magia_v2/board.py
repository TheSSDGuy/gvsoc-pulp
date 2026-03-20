# Copyright (C) 2025 Fondazione Chips-IT

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



# Authors: Lorenzo Zuolo, Chips-IT (lorenzo.zuolo@chips.it)
import gvsoc.systree
import gvsoc.runner
import os
from pulp.chips.magia_v2.arch import MagiaTree

from pulp.chips.magia_v2.soc import MagiaV2Soc
from gvrun.parameter import TargetParameter

class MagiaV2Board(gvsoc.systree.Component):
    def __init__(self, parent, name:str, parser, options):
        super().__init__(parent, name, options=options)

        # Soc model
        tree = MagiaTree(self, 'magia_v2')
        self.soc = MagiaV2Soc(self, 'magia-v2-soc', tree, parser)


class Target(gvsoc.runner.Target):
    def __init__(self, parser, options):
        super(Target, self).__init__(parser, options,
              model=MagiaV2Board, description="Magia v2 (memory mapped) board")