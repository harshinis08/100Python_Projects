"""new commit

Revision ID: 727876771086
Revises: 
Create Date: 2024-06-15 21:46:47.259904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '727876771086'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###
