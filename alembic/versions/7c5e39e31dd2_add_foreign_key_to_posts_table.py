"""Add foreign key to posts table

Revision ID: 7c5e39e31dd2
Revises: 1de377daca96
Create Date: 2023-04-03 23:42:35.481767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c5e39e31dd2'
down_revision = '1de377daca96'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('user_id', sa.Integer(), nullable=False)
                  )
    op.create_foreign_key('posts_users_fk', 
                          source_table="posts", 
                          referent_table="users", 
                          local_cols=['user_id'], 
                          remote_cols=['id'], 
                          ondelete='CASCADE'
                          )
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'user_id')
    pass
