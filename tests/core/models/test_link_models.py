# tests/core/domain/test_link_models.py
from math import pi  # Add pi import

import pytest

from suspension.core.domain.link_models import (
    LinkMeasurements,
    LinkForces,
    SuspensionConfig,
    SuspensionResults,
)


def test_link_measurements():
    """Test LinkMeasurements creation and validation"""
    measurements = LinkMeasurements(
        length_3d=10.0, length_2d=9.5, convergence_angle=0.15
    )
    assert (
        measurements.length_3d > measurements.length_2d
    )  # 3D length should be greater
    assert (
        0 <= measurements.convergence_angle <= pi
    )  # Using math.pi instead of pytest.pi


def test_suspension_config_validation():
    """Test SuspensionConfig validation rules"""
    # Valid configuration
    valid_config = SuspensionConfig(
        upper_link_count=2,
        has_panhard=True,
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
    assert valid_config.upper_link_count in (1, 2)  # Should be 1 or 2

    # Test invalid upper_link_count
    with pytest.raises(ValueError):
        SuspensionConfig(
            upper_link_count=3,  # Invalid: must be 1 or 2
            has_panhard=True,
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


def test_link_forces():
    """Test LinkForces validation"""
    forces = LinkForces(max_force=1000.0, current_force=500.0)
    assert forces.current_force <= forces.max_force


def test_suspension_results():
    """Test SuspensionResults validation and structure"""
    results = SuspensionResults(
        anti_features=[0.0, 0.1, 0.2],
        roll_center_height=[100.0, 110.0, 120.0],
        roll_slope=[1.0, 1.1, 1.2],
        pinion_angle=[2.0, 2.1, 2.2],
        travel_positions=[-100.0, 0.0, 100.0],
    )
    assert len(results.anti_features) == len(results.travel_positions)
    assert len(results.roll_center_height) == len(results.travel_positions)
    assert len(results.roll_slope) == len(results.travel_positions)
    assert len(results.pinion_angle) == len(results.travel_positions)
