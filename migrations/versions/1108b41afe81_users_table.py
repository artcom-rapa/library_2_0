"""users table

Revision ID: 1108b41afe81
Revises: 
Create Date: 2020-07-30 14:44:29.827960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1108b41afe81'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('biography', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_author_biography'), 'author', ['biography'], unique=False)
    op.create_index(op.f('ix_author_name'), 'author', ['name'], unique=True)
    op.create_table('rented',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rented_status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('rented_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rented_id'], ['rented.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    op.create_table('authors',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('author_id', 'book_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('authors')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_table('book')
    op.drop_table('rented')
    op.drop_index(op.f('ix_author_name'), table_name='author')
    op.drop_index(op.f('ix_author_biography'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###
