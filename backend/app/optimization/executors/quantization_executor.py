from pathlib import Path

import onnx
from onnx import shape_inference
from onnxruntime.quantization import (
    QuantType,
    quantize_dynamic,
)


class QuantizationExecutor:

    @staticmethod
    def execute(onnx_model_path: str):

        onnx_model = Path(onnx_model_path)

        if not onnx_model.exists():
            raise FileNotFoundError(
                f"ONNX model not found: {onnx_model}"
            )

        output_model = onnx_model.parent / "model_int8.onnx"

        try:
            # Validate model
            model = onnx.load(str(onnx_model))
            onnx.checker.check_model(model)

            # Infer shapes (helps some transformer models)
            model = shape_inference.infer_shapes(model)
            onnx.save(model, str(onnx_model))

            # Dynamic INT8 quantization
            quantize_dynamic(
                model_input=str(onnx_model),
                model_output=str(output_model),
                weight_type=QuantType.QInt8,
                op_types_to_quantize=[
                    "MatMul",
                    "Gemm",
                ],
            )

            if output_model.exists():
                return {
                    "plugin": "Quantization",
                    "stage": "INT8 Dynamic Quantization",
                    "status": "success",
                    "backend": "ONNX Runtime",
                    "optimized_path": str(output_model),
                }

            raise RuntimeError(
                "Quantized model was not generated."
            )

        except Exception as e:

            # Continue the pipeline with the ONNX model
            return {
                "plugin": "Quantization",
                "stage": "INT8 Dynamic Quantization",
                "status": "skipped",
                "reason": str(e),
                "backend": "ONNX Runtime",
                "optimized_path": str(onnx_model),
            }