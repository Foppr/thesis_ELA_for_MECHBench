import numpy as np

class ExponentialWaveLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with multi-dimensional modulation
        exp_component = np.sum(0.8 * np.exp(-0.5 * np.sum(x**2)) * (1.0 + 0.3 * np.sin(2.0 * x)))
        
        # Trigonometric wave interference with phase coupling and amplitude modulation
        wave = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sum(x[:i]) if i > 0 else 0.0
            wave += 1.2 * np.sin(3.0 * x[i] + 0.4 * np.cos(1.5 * x[i]) + phase) * np.cos(2.0 * x[i] + 0.3 * np.sin(1.2 * x[i]))
        
        # Modified logistic map with time-delayed feedback and dynamic scaling
        logistic = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic_val = 3.8 * x[i] * (1.0 - x[i])
            else:
                # Time-delayed feedback with dynamic scaling factor
                delay = max(0, i - 2)
                scale_factor = 1.0 + 0.2 * np.sin(0.3 * i) * np.cos(0.1 * x[i-1])
                logistic_val = 3.8 * x[i] * (1.0 - x[i]) * scale_factor
                logistic_val += 0.1 * np.sin(0.5 * x[delay] + 0.2 * np.cos(x[delay])) if delay < self.dim else 0.0
            logistic += logistic_val
        
        # Dynamic scaling with multi-scale modulation
        scale = 1.0 + 0.1 * np.sin(0.2 * np.sum(x)) + 0.05 * np.cos(0.1 * np.sum(x**2))
        
        # Combined fitness function with adaptive weighting
        weight_exp = 1.0 + 0.15 * np.sin(0.1 * np.sum(x))
        weight_wave = 1.0 + 0.1 * np.cos(0.2 * np.sum(x))
        weight_logistic = 1.0 + 0.2 * np.sin(0.15 * np.sum(x))
        
        result = weight_exp * exp_component + weight_wave * wave + weight_logistic * logistic * scale
        
        return result