"""empty message

Revision ID: 4328807b495
Revises: 55af87ac514
Create Date: 2015-09-02 16:56:50.597467

"""

# revision identifiers, used by Alembic.
revision = '4328807b495'
down_revision = '55af87ac514'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('answer', sa.String(length=100), nullable=True),
    sa.Column('guesses', sa.Text(), nullable=True),
    sa.Column('misses', sa.Text(), nullable=True),
    sa.Column('board', sa.Text(), nullable=True),
    sa.Column('host_id', sa.Integer(), nullable=True),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('winner_id', sa.Integer(), nullable=True),
    sa.Column('loser_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['host_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['loser_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['winner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    op.drop_table('users')
    ### end Alembic commands ###
