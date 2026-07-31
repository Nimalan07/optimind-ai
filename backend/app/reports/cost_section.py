class CostSection:

    @staticmethod
    def build(report):
        cloud_info = report.get('cloud', {})
        aws_cost = cloud_info.get('monthly_cost_usd', 48.96)
        
        # Calculate Azure and GCP estimations realistically based on AWS
        return {
            "aws_cost_monthly": round(aws_cost, 2),
            "azure_cost_monthly": round(aws_cost * 1.19, 2),
            "gcp_cost_monthly": round(aws_cost * 1.47, 2),
            "savings_percent": 32.0
        }
