"""update table1

Revision ID: 097bb8f279fb
Revises: 0de082680838
Create Date: 2020-07-15 00:27:29.630729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '097bb8f279fb'
down_revision = '0de082680838'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('softwareSimilare_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_similar_softwareSimilare_id_software'), 'software', ['softwareSimilare_id'], ['id'])
        batch_op.drop_column('softwarSimilare_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('softwarSimilare_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_similar_softwareSimilare_id_software'), type_='foreignkey')
        batch_op.create_foreign_key(None, 'software', ['softwarSimilare_id'], ['id'])
        batch_op.drop_column('softwareSimilare_id')

    # ### end Alembic commands ###
