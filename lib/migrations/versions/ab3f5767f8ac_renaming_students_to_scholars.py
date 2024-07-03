"""Renaming students to scholars

Revision ID: ab3f5767f8ac
Revises: 791279dd0760
Create Date: 2024-07-03 22:13:49.975055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab3f5767f8ac'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
