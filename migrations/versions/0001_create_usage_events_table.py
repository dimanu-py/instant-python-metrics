"""create usage_events table

Revision ID: 0001
Revises:
Create Date: 2026-06-07 12:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSON

# revision identifiers, used by Alembic.
revision: str = "0001"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the usage_events table."""
    op.create_table(
        "usage_events",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("ipy_version", sa.String(255), nullable=False),
        sa.Column("operating_system", sa.String(255), nullable=False),
        sa.Column("distinct_id", sa.String(255), nullable=False),
        sa.Column("command", sa.String(255), nullable=False),
        sa.Column("python_version", sa.String(255), nullable=False),
        sa.Column("dependency_manager", sa.String(255), nullable=False),
        sa.Column("template", sa.String(255), nullable=False),
        sa.Column("built_in_features", JSON, nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )


def downgrade() -> None:
    """Drop the usage_events table."""
    op.drop_table("usage_events")
