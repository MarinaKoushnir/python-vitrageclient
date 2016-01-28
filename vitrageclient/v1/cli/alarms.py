# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from cliff import lister

from vitrageclient.common import utils


class AlarmsList(lister.Lister):
    """List alarms on entity"""

    def get_parser(self, prog_name):
        parser = super(AlarmsList, self).get_parser(prog_name)
        parser.add_argument("id", metavar="<entity id>", help="The entity id")

        return parser

    def take_action(self, parsed_args):
        entity_id = parsed_args.id
        alarms = self.app.client.alarms.list(entity_id=entity_id)
        return utils.list2cols(('id', 'name', 'severity', 'update_timestamp'),
                               alarms)
