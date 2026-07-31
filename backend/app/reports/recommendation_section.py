class RecommendationSection:

    @staticmethod
    def build(report):
        backend_info = report.get('backend', {})
        cloud_info = report.get('cloud', {})
        
        return {
            "backend": backend_info.get('backend', 'Unknown'),
            "backend_reason": ", ".join(backend_info.get('reason', [])),
            "cloud_provider": cloud_info.get('provider', 'Unknown'),
            "cloud_instance": cloud_info.get('instance', 'Unknown'),
            "cloud_processor": cloud_info.get('processor', 'Unknown'),
            "cloud_reason": ", ".join(cloud_info.get('reason', []))
        }
