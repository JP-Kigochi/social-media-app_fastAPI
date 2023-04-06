"""Add last few columns to posts table

Revision ID: adbcf38815f7
Revises: 7c5e39e31dd2
Create Date: 2023-04-04 00:34:19.195210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adbcf38815f7'
down_revision = '7c5e39e31dd2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', 
                  sa.Column('published', 
                            sa.Boolean(), 
                            nullable=False, 
                            server_default = 'True'
                            )
                  )
    op.add_column('posts',
                   sa.Column('created_at', 
                             sa.TIMESTAMP(timezone=True), 
                             nullable=False, 
                             server_default = sa.text('now()')
                             )
                   )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
