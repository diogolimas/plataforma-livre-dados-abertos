"""resolvi bug

Revision ID: 4caa86c3f7d6
Revises: 9f43e70d7b73
Create Date: 2019-11-19 10:39:18.287336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4caa86c3f7d6'
down_revision = '9f43e70d7b73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_softwares_activeDevelopment'), 'softwares', ['activeDevelopment'], unique=False)
    op.create_index(op.f('ix_softwares_dateCreation'), 'softwares', ['dateCreation'], unique=False)
    op.create_index(op.f('ix_softwares_dateRelease'), 'softwares', ['dateRelease'], unique=False)
    op.create_index(op.f('ix_softwares_downloadLink'), 'softwares', ['downloadLink'], unique=False)
    op.drop_index('ix_softwares_activeDevelopment', table_name='softwares')
    op.drop_index('ix_softwares_dateCreation', table_name='softwares')
    op.drop_index('ix_softwares_dateRelease', table_name='softwares')
    op.drop_index('ix_softwares_downloadLink', table_name='softwares')
    op.create_index(op.f('ix_sources_datasetLink'), 'sources', ['datasetLink'], unique=False)
    op.create_index(op.f('ix_sources_officialLink'), 'sources', ['officialLink'], unique=False)
    op.drop_index('ix_sources_datasetLink', table_name='sources')
    op.drop_index('ix_sources_officialLink', table_name='sources')
    op.create_index(op.f('ix_tag_palavraChave'), 'tag', ['palavraChave'], unique=False)
    op.drop_index('ix_tag_palavraChave', table_name='tag')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_tag_palavraChave', 'tag', ['palavraChave'], unique=False)
    op.drop_index(op.f('ix_tag_palavraChave'), table_name='tag')
    op.create_index('ix_sources_officialLink', 'sources', ['officialLink'], unique=False)
    op.create_index('ix_sources_datasetLink', 'sources', ['datasetLink'], unique=False)
    op.drop_index(op.f('ix_sources_officialLink'), table_name='sources')
    op.drop_index(op.f('ix_sources_datasetLink'), table_name='sources')
    op.create_index('ix_softwares_downloadLink', 'softwares', ['downloadLink'], unique=False)
    op.create_index('ix_softwares_dateRelease', 'softwares', ['dateRelease'], unique=False)
    op.create_index('ix_softwares_dateCreation', 'softwares', ['dateCreation'], unique=False)
    op.create_index('ix_softwares_activeDevelopment', 'softwares', ['activeDevelopment'], unique=False)
    op.drop_index(op.f('ix_softwares_downloadLink'), table_name='softwares')
    op.drop_index(op.f('ix_softwares_dateRelease'), table_name='softwares')
    op.drop_index(op.f('ix_softwares_dateCreation'), table_name='softwares')
    op.drop_index(op.f('ix_softwares_activeDevelopment'), table_name='softwares')
    # ### end Alembic commands ###