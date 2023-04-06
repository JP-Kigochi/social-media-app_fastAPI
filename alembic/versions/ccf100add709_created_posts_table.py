"""Created posts table

Revision ID: ccf100add709
Revises: 
Create Date: 2023-04-03 22:05:03.768674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccf100add709'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
                    sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
                    sa.Column('title', sa.String(), nullable = False)
                    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
