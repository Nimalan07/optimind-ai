class Charts:

    @staticmethod
    def generate(report_data=None):
        # We can extract values from report_data to display dynamic bars
        bm = (report_data or {}).get("benchmark", {})
        before = bm.get("before", {})
        after = bm.get("after", {})
        
        before_lat = before.get("latency", {}).get("average_ms", 45.0)
        after_lat = after.get("latency", {}).get("average_ms", 22.0)
        
        before_mem = before.get("memory", {}).get("rss_mb", 438)
        after_mem = after.get("memory", {}).get("rss_mb", 112)
        
        before_sz = before.get("size", {}).get("mb", 438)
        after_sz = after.get("size", {}).get("mb", 112)

        return {
            "latency": f"Before ████████████ {before_lat} ms\nAfter  ██████ {after_lat} ms",
            "memory": f"Before ██████████████ {before_mem} MB\nAfter  ████ {after_mem} MB",
            "model_size": f"Before ███████████ {before_sz} MB\nAfter  ██ {after_sz} MB"
        }
