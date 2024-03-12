"""empty message

Revision ID: 201e97554583
Revises: 
Create Date: 2024-03-11 17:51:44.760855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '201e97554583'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('business', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('level',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level', sa.String(length=3), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('social_name', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('mar_status', sa.String(length=15), nullable=False),
    sa.Column('occupation', sa.String(length=255), nullable=False),
    sa.Column('education', sa.String(length=255), nullable=False),
    sa.Column('health_insurance', sa.String(length=255), nullable=False),
    sa.Column('escort', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blood_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('maternal', sa.String(length=5), nullable=False),
    sa.Column('paternal', sa.String(length=5), nullable=False),
    sa.Column('m_hemoglobin', sa.Numeric(precision=3, scale=2), nullable=False),
    sa.Column('p_hemoglobin', sa.Numeric(precision=3, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['business_id'], ['business.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['business_id'], ['business.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('follow_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('dr_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('ga_chrono', sa.String(length=5), nullable=False),
    sa.Column('ga_echo', sa.String(length=5), nullable=False),
    sa.Column('weight', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.Column('gain', sa.Integer(), nullable=False),
    sa.Column('blood_pressure', sa.String(length=10), nullable=False),
    sa.Column('uterine_height', sa.Integer(), nullable=False),
    sa.Column('fetal_heartbeat', sa.Integer(), nullable=False),
    sa.Column('edema', sa.Integer(), nullable=False),
    sa.Column('show', sa.String(length=15), nullable=False),
    sa.Column('assessment', sa.Text(), nullable=False),
    sa.Column('conduct', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['dr_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('general_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('dr_id', sa.Integer(), nullable=False),
    sa.Column('height', sa.Numeric(precision=4, scale=2), nullable=False),
    sa.Column('weight', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.Column('imc', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['dr_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gest_age',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('last_period', sa.DateTime(), nullable=False),
    sa.Column('ga_chrono', sa.String(length=5), nullable=True),
    sa.Column('birth_prev', sa.DateTime(), nullable=False),
    sa.Column('first_ultrasound', sa.DateTime(), nullable=False),
    sa.Column('ga_first_ultrasound', sa.String(length=5), nullable=True),
    sa.Column('echo_birth_prev', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preg_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('pregnancies', sa.Integer(), nullable=False),
    sa.Column('normal_birth', sa.Integer(), nullable=False),
    sa.Column('cesarean_births', sa.Integer(), nullable=False),
    sa.Column('mole', sa.Integer(), nullable=False),
    sa.Column('abortions', sa.Integer(), nullable=False),
    sa.Column('ectopic', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile_pic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_level',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('level_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['level_id'], ['level.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vaccines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('tetanus', sa.Boolean(), nullable=False),
    sa.Column('whooping_cough', sa.Boolean(), nullable=False),
    sa.Column('hepatitis', sa.Boolean(), nullable=False),
    sa.Column('influenza', sa.Boolean(), nullable=False),
    sa.Column('covid_19', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccines')
    op.drop_table('user_level')
    op.drop_table('profile_pic')
    op.drop_table('preg_info')
    op.drop_table('gest_age')
    op.drop_table('general_info')
    op.drop_table('follow_history')
    op.drop_table('employees')
    op.drop_table('doctors')
    op.drop_table('blood_type')
    op.drop_table('user')
    op.drop_table('patients')
    op.drop_table('level')
    op.drop_table('business')
    # ### end Alembic commands ###
