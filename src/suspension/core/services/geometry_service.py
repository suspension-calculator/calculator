# src/suspension/core/services/geometry_service.py
class GeometryService:
    """Handle geometric calculations"""

    def calculate_link_lengths(self, geometry: LinkGeometry) -> LinkGeometry:
        pass

    def calculate_instant_center(self, geometry: SuspensionGeometry) -> Point3D:
        pass


# src/suspension/core/services/analysis_service.py
class AnalysisService:
    """Handle suspension analysis"""

    def calculate_anti_features(self, geometry: SuspensionGeometry) -> AnalysisResults:
        pass
