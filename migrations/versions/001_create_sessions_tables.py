"""Create session state and audit tables."""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa

revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply schema changes for session persistence."""

    op.create_table(
        "session_state",
        sa.Column("session_id", sa.String(length=64), primary_key=True),
        sa.Column("payload", sa.LargeBinary(), nullable=False),
        sa.Column("payload_hash", sa.String(length=64), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_table(
        "state_audit",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("session_id", sa.String(length=64), nullable=False),
        sa.Column("payload_hash", sa.String(length=64), nullable=False),
        sa.Column("event", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("idx_state_audit_session", "state_audit", ["session_id"])
    op.create_table(
        "state_hash_index",
        sa.Column("hash", sa.String(length=64), primary_key=True),
        sa.Column("session_id", sa.String(length=64), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    """Revert schema changes."""

    op.drop_table("state_hash_index")
    op.drop_index("idx_state_audit_session", table_name="state_audit")
    op.drop_table("state_audit")
    op.drop_table("session_state")
