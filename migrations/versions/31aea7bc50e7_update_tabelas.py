"""update tabelas

Revision ID: 31aea7bc50e7
Revises: 2fbcccd86f86
Create Date: 2020-03-24 20:24:31.276469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31aea7bc50e7'
down_revision = '2fbcccd86f86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('post',
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('tag', sa.String(length=200), nullable=True),
    sa.Column('categorie', sa.String(length=200), nullable=True),
    sa.Column('sphere', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=800), nullable=True),
    sa.Column('officialLink', sa.String(length=300), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_categorie'), 'post', ['categorie'], unique=False)
    op.create_index(op.f('ix_post_description'), 'post', ['description'], unique=False)
    op.create_index(op.f('ix_post_officialLink'), 'post', ['officialLink'], unique=False)
    op.create_index(op.f('ix_post_sphere'), 'post', ['sphere'], unique=False)
    op.create_index(op.f('ix_post_tag'), 'post', ['tag'], unique=False)
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_index(op.f('ix_post_title'), 'post', ['title'], unique=True)
    op.create_table('software',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('tag', sa.String(length=800), nullable=True),
    sa.Column('categorie', sa.String(length=800), nullable=True),
    sa.Column('description', sa.String(length=800), nullable=True),
    sa.Column('downloadLink', sa.String(length=300), nullable=True),
    sa.Column('activeDevelopment', sa.String(length=200), nullable=True),
    sa.Column('license', sa.String(length=200), nullable=True),
    sa.Column('owner', sa.String(length=200), nullable=True),
    sa.Column('dateCreation', sa.String(length=300), nullable=True),
    sa.Column('dateRelease', sa.String(length=300), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_software_activeDevelopment'), 'software', ['activeDevelopment'], unique=False)
    op.create_index(op.f('ix_software_categorie'), 'software', ['categorie'], unique=False)
    op.create_index(op.f('ix_software_dateCreation'), 'software', ['dateCreation'], unique=False)
    op.create_index(op.f('ix_software_dateRelease'), 'software', ['dateRelease'], unique=False)
    op.create_index(op.f('ix_software_description'), 'software', ['description'], unique=False)
    op.create_index(op.f('ix_software_downloadLink'), 'software', ['downloadLink'], unique=False)
    op.create_index(op.f('ix_software_license'), 'software', ['license'], unique=False)
    op.create_index(op.f('ix_software_owner'), 'software', ['owner'], unique=False)
    op.create_index(op.f('ix_software_tag'), 'software', ['tag'], unique=False)
    op.create_index(op.f('ix_software_timestamp'), 'software', ['timestamp'], unique=False)
    op.create_index(op.f('ix_software_title'), 'software', ['title'], unique=True)
    op.drop_index('ix_software_dados_dataCriacao', table_name='software_dados')
    op.drop_index('ix_software_dados_dataLancamento', table_name='software_dados')
    op.drop_index('ix_software_dados_descricao', table_name='software_dados')
    op.drop_index('ix_software_dados_desenvolvimentoAtivo', table_name='software_dados')
    op.drop_index('ix_software_dados_licenca', table_name='software_dados')
    op.drop_index('ix_software_dados_linkDownload', table_name='software_dados')
    op.drop_index('ix_software_dados_proprietario', table_name='software_dados')
    op.drop_index('ix_software_dados_titulo', table_name='software_dados')
    op.drop_table('software_dados')
    op.drop_index('ix_tipo_usuario_nome', table_name='tipo_usuario')
    op.drop_table('tipo_usuario')
    op.drop_index('ix_fonte_dados_descricao', table_name='fonte_dados')
    op.drop_index('ix_fonte_dados_esfera', table_name='fonte_dados')
    op.drop_index('ix_fonte_dados_linkDataset', table_name='fonte_dados')
    op.drop_index('ix_fonte_dados_linkOficial', table_name='fonte_dados')
    op.drop_index('ix_fonte_dados_titulo', table_name='fonte_dados')
    op.drop_table('fonte_dados')
    op.add_column('user', sa.Column('about_me', sa.String(length=300), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.drop_index('ix_user_description', table_name='user')
    op.drop_index('ix_user_nickname', table_name='user')
    op.drop_column('user', 'password')
    op.drop_column('user', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('description', sa.VARCHAR(length=500), nullable=True))
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=200), nullable=True))
    op.create_index('ix_user_nickname', 'user', ['nickname'], unique=False)
    op.create_index('ix_user_description', 'user', ['description'], unique=False)
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    op.create_table('fonte_dados',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('titulo', sa.VARCHAR(length=70), nullable=True),
    sa.Column('esfera', sa.VARCHAR(length=110), nullable=True),
    sa.Column('descricao', sa.VARCHAR(length=200), nullable=True),
    sa.Column('linkOficial', sa.VARCHAR(length=200), nullable=True),
    sa.Column('linkDataset', sa.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_fonte_dados_titulo', 'fonte_dados', ['titulo'], unique=False)
    op.create_index('ix_fonte_dados_linkOficial', 'fonte_dados', ['linkOficial'], unique=False)
    op.create_index('ix_fonte_dados_linkDataset', 'fonte_dados', ['linkDataset'], unique=False)
    op.create_index('ix_fonte_dados_esfera', 'fonte_dados', ['esfera'], unique=False)
    op.create_index('ix_fonte_dados_descricao', 'fonte_dados', ['descricao'], unique=False)
    op.create_table('tipo_usuario',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tipo_usuario_nome', 'tipo_usuario', ['nome'], unique=False)
    op.create_table('software_dados',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('titulo', sa.VARCHAR(length=70), nullable=True),
    sa.Column('descricao', sa.VARCHAR(length=200), nullable=True),
    sa.Column('dataCriacao', sa.VARCHAR(length=10), nullable=True),
    sa.Column('dataLancamento', sa.VARCHAR(length=10), nullable=True),
    sa.Column('linkDownload', sa.VARCHAR(length=200), nullable=True),
    sa.Column('desenvolvimentoAtivo', sa.VARCHAR(length=200), nullable=True),
    sa.Column('licenca', sa.VARCHAR(length=10), nullable=True),
    sa.Column('proprietario', sa.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_software_dados_titulo', 'software_dados', ['titulo'], unique=False)
    op.create_index('ix_software_dados_proprietario', 'software_dados', ['proprietario'], unique=False)
    op.create_index('ix_software_dados_linkDownload', 'software_dados', ['linkDownload'], unique=False)
    op.create_index('ix_software_dados_licenca', 'software_dados', ['licenca'], unique=False)
    op.create_index('ix_software_dados_desenvolvimentoAtivo', 'software_dados', ['desenvolvimentoAtivo'], unique=False)
    op.create_index('ix_software_dados_descricao', 'software_dados', ['descricao'], unique=False)
    op.create_index('ix_software_dados_dataLancamento', 'software_dados', ['dataLancamento'], unique=False)
    op.create_index('ix_software_dados_dataCriacao', 'software_dados', ['dataCriacao'], unique=False)
    op.drop_index(op.f('ix_software_title'), table_name='software')
    op.drop_index(op.f('ix_software_timestamp'), table_name='software')
    op.drop_index(op.f('ix_software_tag'), table_name='software')
    op.drop_index(op.f('ix_software_owner'), table_name='software')
    op.drop_index(op.f('ix_software_license'), table_name='software')
    op.drop_index(op.f('ix_software_downloadLink'), table_name='software')
    op.drop_index(op.f('ix_software_description'), table_name='software')
    op.drop_index(op.f('ix_software_dateRelease'), table_name='software')
    op.drop_index(op.f('ix_software_dateCreation'), table_name='software')
    op.drop_index(op.f('ix_software_categorie'), table_name='software')
    op.drop_index(op.f('ix_software_activeDevelopment'), table_name='software')
    op.drop_table('software')
    op.drop_index(op.f('ix_post_title'), table_name='post')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_index(op.f('ix_post_tag'), table_name='post')
    op.drop_index(op.f('ix_post_sphere'), table_name='post')
    op.drop_index(op.f('ix_post_officialLink'), table_name='post')
    op.drop_index(op.f('ix_post_description'), table_name='post')
    op.drop_index(op.f('ix_post_categorie'), table_name='post')
    op.drop_table('post')
    op.drop_table('followers')
    # ### end Alembic commands ###
