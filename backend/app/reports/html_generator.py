class HTMLGenerator:

    @staticmethod
    def generate(report_content):
        # Generate an HTML representation
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Optimization Report - {report_content['model']}</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #F7FAFC; color: #2D3748; }}
        .container {{ max-width: 800px; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        h1 {{ color: #1A365D; border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; }}
        h2 {{ color: #2B6CB0; margin-top: 30px; }}
        .score {{ font-size: 24px; font-weight: bold; color: #38A169; }}
        .status {{ background-color: #EBF8FF; color: #2B6CB0; padding: 10px; border-radius: 4px; display: inline-block; font-weight: bold; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #E2E8F0; }}
        th {{ background-color: #EBF8FF; color: #2B6CB0; }}
        pre {{ background: #EDF2F7; padding: 15px; border-radius: 4px; font-family: monospace; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>AI Optimization Report</h1>
        <p><strong>Model:</strong> {report_content['model']}</p>
        <p><strong>Optimization Score:</strong> <span class="score">{report_content['optimization_score']}/100</span></p>
        <p><strong>Status:</strong> <span class="status">{report_content['status']}</span></p>
        
        <h2>Executive Summary</h2>
        <pre>{report_content['executive_summary']['summary']}</pre>
        
        <h2>Deployment Readiness</h2>
        <ul>
            <li><strong>Docker:</strong> {report_content['deployment']['docker']}</li>
            <li><strong>Kubernetes:</strong> {report_content['deployment']['kubernetes']}</li>
            <li><strong>FastAPI:</strong> {report_content['deployment']['fastapi']}</li>
            <li><strong>ONNX Runtime:</strong> {report_content['deployment']['onnx_runtime']}</li>
        </ul>
        
        <h2>Visual Comparison Charts</h2>
        <h3>Latency Comparison</h3>
        <pre>{report_content['charts']['latency']}</pre>
        <h3>Memory Comparison</h3>
        <pre>{report_content['charts']['memory']}</pre>
        <h3>Model Size Comparison</h3>
        <pre>{report_content['charts']['model_size']}</pre>
    </div>
</body>
</html>
"""
        return html
