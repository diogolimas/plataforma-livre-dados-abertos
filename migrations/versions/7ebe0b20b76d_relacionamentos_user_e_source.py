"""relacionamentos user e source

Revision ID: 7ebe0b20b76d
Revises: 5f6478ccc7a4
Create Date: 2019-11-11 00:32:47.922964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ebe0b20b76d'
down_revision = '5f6478ccc7a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'source', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'source', type_='foreignkey')
    # ### end Alembic commands ###