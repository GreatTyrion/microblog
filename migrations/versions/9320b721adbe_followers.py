"""followers

Revision ID: 9320b721adbe
Revises: f1bd04bfa823
Create Date: 2021-04-20 15:11:23.364101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9320b721adbe'
down_revision = 'f1bd04bfa823'
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
