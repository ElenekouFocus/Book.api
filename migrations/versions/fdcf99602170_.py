"""empty message

Revision ID: fdcf99602170
Revises: 
Create Date: 2022-07-23 13:39:40.299675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdcf99602170'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('livres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('isbn', sa.String(length=50), nullable=False),
    sa.Column('titre', sa.String(length=100), nullable=False),
    sa.Column('date_parution', sa.Date(), nullable=False),
    sa.Column('editeur', sa.String(length=100), nullable=False),
    sa.Column('version', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle_categorie', sa.String(length=100), nullable=False),
    sa.Column('description_categorie', sa.String(length=100), nullable=False),
    sa.Column('livre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['livre_id'], ['livres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    op.drop_table('livres')
    # ### end Alembic commands ###