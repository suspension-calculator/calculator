# tests/conftest.py
import pytest
from suspension.core.domain.geometry import Point3D, LinkMountPoints
from suspension.core.domain.link_models import SuspensionConfig


@pytest.fixture
def basic_point3d():
    """Basic 3D point for testing"""
    return Point3D(x=1.0, y=2.0, z=3.0)


@pytest.fixture
def basic_link_mount():
    """Basic link mount points for testing"""
    frame = Point3D(x=0.0, y=0.0, z=0.0)
    axle = Point3D(x=3.0, y=4.0, z=0.0)
    return LinkMountPoints(frame=frame, axle=axle)


@pytest.fixture
def basic_suspension_config():
    """Basic suspension configuration for testing"""
    return SuspensionConfig(
        upper_link_count=2,
        has_panhard=False,
        bump_travel=100.0,
        droop_travel=100.0,
        unsprung_mass=50.0,
        tire_radius=400.0,
        track_width=1800.0,
        portal_height=0.0,
        axle_tube_diameter=80.0,
        tire_diameter=800.0,
        tire_width=300.0,
    )
