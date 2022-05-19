"""empty message

Revision ID: f54878c76572
Revises: 
Create Date: 2022-05-19 16:58:39.128875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f54878c76572'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('secure_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('tel', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('hoods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('about', sa.String(), nullable=False),
    sa.Column('members', sa.Integer(), nullable=True),
    sa.Column('hood_pic', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('amenities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('police_contact', sa.String(), nullable=True),
    sa.Column('hospital_contact', sa.String(), nullable=True),
    sa.Column('hood_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hood_id'], ['hoods.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('amenities')
    op.drop_table('post')
    op.drop_table('hoods')
    op.drop_table('business')
    op.drop_table('users')
    # ### end Alembic commands ###
