# tests/core/calculations/test_link_sizing.py
from unittest.mock import patch
import pytest
from math import pi
from suspension.core.calculations.link_sizing import run_link_sizing
from suspension.io.variables import constant, travel, S, x, y, z


def setup_test_data():
    """Set up test data for link sizing calculations"""
    # Front upper link
    constant.F.U_OD = 1.0  # 1 inch outer diameter
    constant.F.U_wall = 0.125  # 1/8 inch wall thickness
    constant.F.U_length_3D = 12.0  # 12 inch length
    constant.F.U_force = 1000.0  # 1000 lbs force
    constant.F.U_material = "4130"  # Using 4130 steel
    constant.F.U_rod_end = "CM8"  # Example rod end
    constant.F.U_count = 2  # Number of upper links
    constant.F.U_solid = False

    # Front lower link (new)
    constant.F.L_OD = 1.0
    constant.F.L_wall = 0.125
    constant.F.L_length_3D = 12.0
    constant.F.L_force = 1000.0
    constant.F.L_material = "4130"
    constant.F.L_rod_end = "CM8"
    constant.F.L_solid = False

    # Rear upper link (new)
    constant.R.U_OD = 1.0
    constant.R.U_wall = 0.125
    constant.R.U_length_3D = 12.0
    constant.R.U_force = 1000.0
    constant.R.U_material = "4130"
    constant.R.U_rod_end = "CM8"
    constant.R.U_count = 2
    constant.R.U_solid = False

    # Rear lower link (new)
    constant.R.L_OD = 1.0
    constant.R.L_wall = 0.125
    constant.R.L_length_3D = 12.0
    constant.R.L_force = 1000.0
    constant.R.L_material = "4130"
    constant.R.L_rod_end = "CM8"
    constant.R.L_solid = False

    # Panhard settings
    constant.F.panhard = False
    constant.R.panhard = False

    # Panhard properties
    constant.F.P_material = "4130"
    constant.F.P_OD = 1.0
    constant.F.P_wall = 0.125
    constant.F.P_length_3D = 12.0
    constant.F.P_force = 1000.0
    constant.F.P_rod_end = "CM8"
    constant.F.P_solid = False

    constant.R.P_material = "4130"
    constant.R.P_OD = 1.0
    constant.R.P_wall = 0.125
    constant.R.P_length_3D = 12.0
    constant.R.P_force = 1000.0
    constant.R.P_rod_end = "CM8"
    constant.R.P_solid = False

    # Mock material properties
    constant.materials.name = ["4130"]
    constant.materials.yield_strength = [90000]  # 90 ksi
    constant.materials.modulus_elasticity = [29700000]  # 29.7M psi
    constant.materials.density = [0.284]  # lb/in^3

    # Mock rod end properties
    constant.rod_ends.name = ["CM8"]
    constant.rod_ends.radial_load = [5000]  # 5000 lb load rating
    constant.rod_ends.weight = [0.25]  # 0.25 lb each
    constant.rod_ends.hole_diameter = [0.5]
    constant.rod_ends.shank_diameter = [0.5]
    constant.rod_ends.thread = ["1/2-20"]

    # Vehicle mass for bending calcs
    constant.V.mass = 2000  # 2000 lbs

    # Initialize sizing properties if they don't exist
    if not hasattr(constant, 'sizing'):
        class Sizing:
            pass
        constant.sizing = Sizing()

    constant.sizing.link_weight = [0] * 6
    constant.sizing.RE_weight = [0] * 6
    constant.sizing.total_link_weight = [0] * 6
    constant.sizing.FS_yield = [0] * 6
    constant.sizing.FS_buckling = [0] * 6
    constant.sizing.FS_bending = [0] * 6
    constant.sizing.FS_RE = [0] * 6
    constant.sizing.dent_resistance = [0] * 6


@patch('suspension.io.IO_Conversion.link_sizing_IO.input_processing_link_sizing')
@patch('suspension.io.IO_Conversion.link_sizing_IO.output_processing_link_sizing')
def test_link_weight_calculation(mock_output_process, mock_input_process):
    """Test the link weight calculation"""
    setup_test_data()
    run_link_sizing()

    # Calculate expected weight
    OD = constant.F.U_OD
    wall = constant.F.U_wall
    length = constant.F.U_length_3D
    density = constant.materials.density[0]

    # Link weight calculation: π*(OD²-(OD-2*wall)²)/4 * length * density
    expected_area = pi * (OD ** 2 - (OD - 2 * wall) ** 2) / 4
    expected_weight = expected_area * length * density

    assert abs(constant.sizing.link_weight[0] - expected_weight) < 0.001, \
        f"Expected link weight {expected_weight}, got {constant.sizing.link_weight[0]}"


@patch('suspension.io.IO_Conversion.link_sizing_IO.input_processing_link_sizing')
@patch('suspension.io.IO_Conversion.link_sizing_IO.output_processing_link_sizing')
def test_safety_factors(mock_output_process, mock_input_process):
    """Test safety factor calculations"""
    setup_test_data()
    run_link_sizing()

    # Safety factors should be positive and reasonable
    assert constant.sizing.FS_yield[0] > 0, "Yield safety factor should be positive"
    assert constant.sizing.FS_buckling[0] > 0, "Buckling safety factor should be positive"
    assert constant.sizing.FS_bending[0] > 0, "Bending safety factor should be positive"
    assert constant.sizing.FS_RE[0] > 0, "Rod end safety factor should be positive"

    # Rod end safety factor should be close to expected
    expected_RE_SF = constant.rod_ends.radial_load[0] / constant.F.U_force
    assert abs(constant.sizing.FS_RE[0] - expected_RE_SF) < 0.001, \
        f"Expected rod end SF {expected_RE_SF}, got {constant.sizing.FS_RE[0]}"