"""empty message

Revision ID: 6b54ec6e0004
Revises: None
Create Date: 2016-04-19 20:25:58.846017

"""

# revision identifiers, used by Alembic.
revision = '6b54ec6e0004'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('short_description', sa.Text(), nullable=True),
    sa.Column('long_description', sa.Text(), nullable=True),
    sa.Column('goal_amount', sa.Integer(), nullable=True),
    sa.Column('time_start', sa.DateTime(), nullable=True),
    sa.Column('time_end', sa.DateTime(), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pledge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pledge')
    op.drop_table('project')
    op.drop_table('member')
    ### end Alembic commands ###
