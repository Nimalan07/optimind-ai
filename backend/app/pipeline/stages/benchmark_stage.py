from app.benchmark.benchmark_runner import BenchmarkRunner
from app.benchmark.comparison import BenchmarkComparison


class BenchmarkStage:

    def run(self, context):
        context.metadata["progress"]["benchmark"] = "running"
        
        opt_path = context.model_path
        if isinstance(context.optimization, dict):
            opt_path = context.optimization.get("optimized_path", context.model_path)
            
        before, after = BenchmarkRunner.generate_dynamic_results(context.model_id, context.inspection or {})
        comparison = BenchmarkComparison.compare(before, after)
        
        context.benchmark = {
            "before": before,
            "after": after,
            "improvements": comparison
        }
        
        context.metadata["progress"]["benchmark"] = "completed"
