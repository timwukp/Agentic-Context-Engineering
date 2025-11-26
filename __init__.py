"""
ACE Framework (Agentic Context Engineering)

A production-ready framework for scalable context adaptation in AI applications
using a three-agent architecture.
"""

__version__ = "0.1.0"
__author__ = "ACE Framework Team"

from context.models import (
    BulletMetadata,
    ContextBullet,
    ContextPlaybook,
    DeltaContext,
    DeltaMetadata,
)

__all__ = [
    "BulletMetadata",
    "ContextBullet", 
    "ContextPlaybook",
    "DeltaContext",
    "DeltaMetadata",
]