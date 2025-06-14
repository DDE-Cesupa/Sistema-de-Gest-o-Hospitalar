"""initial_02

Revision ID: b0fc6c3aa815
Revises: 
Create Date: 2025-05-24 19:59:06.904661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0fc6c3aa815'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('usuarios', 'senha_hash',
                existing_type=sa.String(length=128),
                type_=sa.String(length=512))
    # ### end Alembic commands ###


def downgrade() -> None:
        op.alter_column('usuarios', 'senha_hash',
                    existing_type=sa.String(length=512),
                    type_=sa.String(length=128))
