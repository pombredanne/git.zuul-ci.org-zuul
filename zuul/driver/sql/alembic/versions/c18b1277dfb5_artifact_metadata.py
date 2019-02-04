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

"""artifact_metadata

Revision ID: c18b1277dfb5
Revises: 39d302d34d38
Create Date: 2019-02-04 14:02:44.291890

"""

# revision identifiers, used by Alembic.
revision = 'c18b1277dfb5'
down_revision = '39d302d34d38'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(table_prefix=''):
    op.add_column(
        table_prefix + 'zuul_artifact', sa.Column('metadata', sa.TEXT()))


def downgrade():
    raise Exception("Downgrades not supported")
