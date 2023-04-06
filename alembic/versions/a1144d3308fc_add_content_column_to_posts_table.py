"""Add content column to posts table

Revision ID: a1144d3308fc
Revises: ccf100add709
Create Date: 2023-04-03 22:32:14.051998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1144d3308fc'
down_revision = 'ccf100add709'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', 
                  sa.Column('content', sa.String(), nullable=False)
                  )
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
