"""Schema Repair

Revision ID: eb3e29735758
Revises: d58613990eed
Create Date: 2023-11-03 16:25:59.553379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb3e29735758'
down_revision = 'd58613990eed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.drop_constraint('fk_carts_item_id_items', type_='foreignkey')
        batch_op.drop_column('item_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_carts_item_id_items', 'items', ['item_id'], ['id'])

    # ### end Alembic commands ###
