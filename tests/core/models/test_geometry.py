# tests/core/domain/test_geometry.py
from math import pi  # Add pi import

import pytest

from suspension.core.domain.geometry import Point3D, LinkMountPoints


def test_point3d_creation():
    """Test basic Point3D creation and validation"""
    point = Point3D(x=1.0, y=2.0, z=3.0)
    assert point.x == 1.0
    assert point.y == 2.0
    assert point.z == 3.0


def test_point3d_computed_fields():
    """Test Point3D computed fields for length calculations"""
    point = Point3D(x=3.0, y=4.0, z=0.0)
    assert point.length_2d == pytest.approx(3.0)  # x-z plane
    assert point.length_3d == pytest.approx(5.0)  # full 3D length


def test_link_mount_points():
    """Test LinkMountPoints creation and validation"""
    frame = Point3D(x=0.0, y=0.0, z=0.0)
    axle = Point3D(x=3.0, y=4.0, z=0.0)
    mount = LinkMountPoints(frame=frame, axle=axle)
    assert mount.length_3d == pytest.approx(5.0)
    assert mount.length_2d == pytest.approx(3.0)


def test_link_mount_points_convergence():
    """Test convergence angle calculation"""
    frame = Point3D(x=0.0, y=0.0, z=0.0)
    axle = Point3D(x=3.0, y=4.0, z=0.0)
    mount = LinkMountPoints(frame=frame, axle=axle)
    # Convergence angle should be calculated correctly
    expected_angle = mount.convergence_angle
    assert expected_angle is not None
    assert 0 <= expected_angle <= pi  # Using math.pi instead of pytest.pi
