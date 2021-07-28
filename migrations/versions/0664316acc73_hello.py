"""Hello

Revision ID: 0664316acc73
Revises: 
Create Date: 2021-07-28 10:25:45.553962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0664316acc73'
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