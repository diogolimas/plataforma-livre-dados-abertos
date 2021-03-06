"""update tables

Revision ID: 8373eb55e977
Revises: fcaf08a84c61
Create Date: 2020-07-15 19:36:04.150658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8373eb55e977'
down_revision = 'fcaf08a84c61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password_hash', sa.String(length=150), nullable=True),
    sa.Column('about_me', sa.String(length=300), nullable=True),
    sa.Column('nickname', sa.String(length=150), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], name=op.f('fk_followers_followed_id_user')),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], name=op.f('fk_followers_follower_id_user'))
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('sphere', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=800), nullable=True),
    sa.Column('officialLink', sa.String(length=300), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_post_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_post'))
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_post_officialLink'), ['officialLink'], unique=False)
        batch_op.create_index(batch_op.f('ix_post_sphere'), ['sphere'], unique=False)
        batch_op.create_index(batch_op.f('ix_post_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_post_title'), ['title'], unique=True)

    op.create_table('software',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=800), nullable=True),
    sa.Column('downloadLink', sa.String(length=300), nullable=True),
    sa.Column('activeDevelopment', sa.String(length=200), nullable=True),
    sa.Column('license', sa.String(length=200), nullable=True),
    sa.Column('owner', sa.String(length=200), nullable=True),
    sa.Column('dateCreation', sa.String(length=300), nullable=True),
    sa.Column('dateRelease', sa.String(length=300), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_software_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_software'))
    )
    with op.batch_alter_table('software', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_software_activeDevelopment'), ['activeDevelopment'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_dateCreation'), ['dateCreation'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_dateRelease'), ['dateRelease'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_downloadLink'), ['downloadLink'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_license'), ['license'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_owner'), ['owner'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_title'), ['title'], unique=True)

    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('postCategory_id', sa.Integer(), nullable=True),
    sa.Column('softwareCategory_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['postCategory_id'], ['post.id'], name=op.f('fk_category_postCategory_id_post')),
    sa.ForeignKeyConstraint(['softwareCategory_id'], ['software.id'], name=op.f('fk_category_softwareCategory_id_software')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_category'))
    )
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_category_category'), ['category'], unique=False)
        batch_op.create_index(batch_op.f('ix_category_timestamp'), ['timestamp'], unique=False)

    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('text', sa.String(length=600), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('postComment_id', sa.Integer(), nullable=True),
    sa.Column('softwareComment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['postComment_id'], ['post.id'], name=op.f('fk_comment_postComment_id_post')),
    sa.ForeignKeyConstraint(['softwareComment_id'], ['software.id'], name=op.f('fk_comment_softwareComment_id_software')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_comment'))
    )
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_comment_email'), ['email'], unique=False)
        batch_op.create_index(batch_op.f('ix_comment_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_comment_text'), ['text'], unique=False)
        batch_op.create_index(batch_op.f('ix_comment_timestamp'), ['timestamp'], unique=False)

    op.create_table('favorites_post',
    sa.Column('favorite_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_id'], ['post.id'], name=op.f('fk_favorites_post_favorite_id_post'))
    )
    op.create_table('favorites_software',
    sa.Column('favorite_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_id'], ['software.id'], name=op.f('fk_favorites_software_favorite_id_software'))
    )
    op.create_table('report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('type', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('postReport_id', sa.Integer(), nullable=True),
    sa.Column('softwareReport_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['postReport_id'], ['post.id'], name=op.f('fk_report_postReport_id_post')),
    sa.ForeignKeyConstraint(['softwareReport_id'], ['software.id'], name=op.f('fk_report_softwareReport_id_software')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_report'))
    )
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_report_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_report_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_report_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_report_type'), ['type'], unique=False)

    op.create_table('similar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('postSimilar_id', sa.Integer(), nullable=True),
    sa.Column('softwareSimilar_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['postSimilar_id'], ['post.id'], name=op.f('fk_similar_postSimilar_id_post')),
    sa.ForeignKeyConstraint(['softwareSimilar_id'], ['software.id'], name=op.f('fk_similar_softwareSimilar_id_software')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_similar'))
    )
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_similar_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_similar_timestamp'), ['timestamp'], unique=False)

    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('postTag_id', sa.Integer(), nullable=True),
    sa.Column('softwareTag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['postTag_id'], ['post.id'], name=op.f('fk_tag_postTag_id_post')),
    sa.ForeignKeyConstraint(['softwareTag_id'], ['software.id'], name=op.f('fk_tag_softwareTag_id_software')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tag'))
    )
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tag_tag'), ['tag'], unique=False)
        batch_op.create_index(batch_op.f('ix_tag_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tag_timestamp'))
        batch_op.drop_index(batch_op.f('ix_tag_tag'))

    op.drop_table('tag')
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_similar_timestamp'))
        batch_op.drop_index(batch_op.f('ix_similar_name'))

    op.drop_table('similar')
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_report_type'))
        batch_op.drop_index(batch_op.f('ix_report_timestamp'))
        batch_op.drop_index(batch_op.f('ix_report_name'))
        batch_op.drop_index(batch_op.f('ix_report_description'))

    op.drop_table('report')
    op.drop_table('favorites_software')
    op.drop_table('favorites_post')
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_comment_timestamp'))
        batch_op.drop_index(batch_op.f('ix_comment_text'))
        batch_op.drop_index(batch_op.f('ix_comment_name'))
        batch_op.drop_index(batch_op.f('ix_comment_email'))

    op.drop_table('comment')
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_category_timestamp'))
        batch_op.drop_index(batch_op.f('ix_category_category'))

    op.drop_table('category')
    with op.batch_alter_table('software', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_software_title'))
        batch_op.drop_index(batch_op.f('ix_software_timestamp'))
        batch_op.drop_index(batch_op.f('ix_software_owner'))
        batch_op.drop_index(batch_op.f('ix_software_license'))
        batch_op.drop_index(batch_op.f('ix_software_downloadLink'))
        batch_op.drop_index(batch_op.f('ix_software_description'))
        batch_op.drop_index(batch_op.f('ix_software_dateRelease'))
        batch_op.drop_index(batch_op.f('ix_software_dateCreation'))
        batch_op.drop_index(batch_op.f('ix_software_activeDevelopment'))

    op.drop_table('software')
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_title'))
        batch_op.drop_index(batch_op.f('ix_post_timestamp'))
        batch_op.drop_index(batch_op.f('ix_post_sphere'))
        batch_op.drop_index(batch_op.f('ix_post_officialLink'))
        batch_op.drop_index(batch_op.f('ix_post_description'))

    op.drop_table('post')
    op.drop_table('followers')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
