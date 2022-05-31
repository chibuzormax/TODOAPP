"""empty message

Revision ID: d5b781d484e8
Revises: cde72634dc92
Create Date: 2022-05-30 11:20:29.519763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5b781d484e8'
down_revision = 'cde72634dc92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    
    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
    
    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
