"""Tabelas Usuario

Revision ID: 14dded2ed444
Revises: 51d33d300fde
Create Date: 2019-11-06 20:24:30.669016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14dded2ed444'
down_revision = '51d33d300fde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=200), nullable=True))
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.VARCHAR(length=200), nullable=True))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###