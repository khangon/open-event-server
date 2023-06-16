"""empty message

Revision ID: d3c32d203ef1
Revises: a45167cdc102
Create Date: 2023-06-15 08:53:12.741108

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'd3c32d203ef1'
down_revision = 'a45167cdc102'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('custom_form_ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('form_id', sa.String(), nullable=False),
    sa.Column('ticket_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('custom_forms', sa.Column('form_id', sa.String(), nullable=True))
    op.add_column('tickets', sa.Column('form_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tickets', 'form_id')
    op.drop_column('custom_forms', 'form_id')
    op.drop_table('custom_form_ticket')
    # ### end Alembic commands ###
