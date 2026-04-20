"""Implementações concretas de predictors Q-FENG.

Cada predictor implementa ``PredictorInterface`` e pode ser plugado
no pipeline sem modificar o motor de interferência.
"""

from qfeng.core.predictors.lightgbm_ceaf import LightGBMCEAFPredictor
from qfeng.core.predictors.ollama_qwen import OllamaQwenPredictor
from qfeng.core.predictors.timeseries_manaus import TimeSeriesManausPredictor

__all__ = [
    "LightGBMCEAFPredictor",
    "OllamaQwenPredictor",
    "TimeSeriesManausPredictor",
]
