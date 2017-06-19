"""empty message

Revision ID: 4a0768c7d7ff
Revises: 
Create Date: 2017-06-18 22:13:10.484418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a0768c7d7ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('datos',
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('favorite_color', sa.String(length=120), nullable=True),
    sa.Column('cats_dog', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('datos')
    # ### end Alembic commands ###