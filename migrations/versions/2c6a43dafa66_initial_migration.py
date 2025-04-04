"""Initial migration

Revision ID: 2c6a43dafa66
Revises: 
Create Date: 2025-03-30 22:48:06.752367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c6a43dafa66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assessment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('leadership_potential', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('team_size', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('strategic_initiatives', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('cross_functional_impact', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('technical_depth', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('system_complexity', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('architectural_influence', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('research_impact', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('innovation_score', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('publication_count', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('technical_contribution', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('code_quality', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('system_impact', sa.String(length=20), nullable=True))
        batch_op.alter_column('review_period',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=20),
               existing_nullable=False)
        batch_op.alter_column('performance_rating',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
        batch_op.alter_column('strengths',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('areas_for_improvement',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('goals',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('comments',
               existing_type=sa.TEXT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assessment', schema=None) as batch_op:
        batch_op.alter_column('comments',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('goals',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('areas_for_improvement',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('strengths',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('performance_rating',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('review_period',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
        batch_op.drop_column('system_impact')
        batch_op.drop_column('code_quality')
        batch_op.drop_column('technical_contribution')
        batch_op.drop_column('publication_count')
        batch_op.drop_column('innovation_score')
        batch_op.drop_column('research_impact')
        batch_op.drop_column('architectural_influence')
        batch_op.drop_column('system_complexity')
        batch_op.drop_column('technical_depth')
        batch_op.drop_column('cross_functional_impact')
        batch_op.drop_column('strategic_initiatives')
        batch_op.drop_column('team_size')
        batch_op.drop_column('leadership_potential')

    # ### end Alembic commands ###
