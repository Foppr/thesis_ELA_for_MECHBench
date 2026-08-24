import numpy as np

class ExponentialWaveLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with adaptive rate
        exp_component = np.sum(0.3 * np.exp(-0.5 * np.abs(x)) * (1.0 + 0.2 * np.sin(0.8 * x)))
        
        # Trigonometric wave interference with frequency coupling
        wave = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.5 * i)
            wave += np.sin(freq * x[i] + 0.4 * np.cos(0.3 * x[i])) * np.cos(0.7 * x[i] + 0.2 * np.sin(0.6 * x[i]))
        
        # Logistic map dynamics with cross-dimensional coupling
        logistic = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic_val = 3.8 * x[i] * (1.0 - x[i])
            else:
                logistic_val = 3.8 * x[i] * (1.0 - x[i])
                logistic_val += 0.2 * np.sin(0.5 * x[i-1]) * np.cos(0.3 * x[i-1])
            logistic += logistic_val
        
        # Adaptive amplitude modulation with multi-scale harmonic components
        amp_mod = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.2 * np.sin(0.4 * i) + 0.1 * np.cos(0.3 * i)
            amp_mod += amp * np.sin(2.0 * x[i] + 0.3 * np.cos(1.5 * x[i]))
        
        # Cross-dimensional coupling with radial distance modulation
        radial = np.sum(0.4 * np.sqrt(np.sum(x**2)) * (1.0 + 0.2 * np.sin(0.6 * np.sum(x))))
        
        # Combined weighted components
        weight_exp = 1.0 + 0.15 * np.cos(0.3 * np.sum(x))
        weight_wave = 1.0 + 0.1 * np.sin(0.4 * np.sum(x))
        weight_logistic = 1.0 + 0.2 * np.cos(0.2 * np.sum(x))
        weight_amp = 1.0 + 0.1 * np.sin(0.5 * np.sum(x))
        weight_radial = 1.0 + 0.05 * np.cos(0.6 * np.sum(x))
        
        result = weight_exp * exp_component + weight_wave * wave + weight_logistic * logistic + weight_amp * amp_mod + weight_radial * radial
        
        return result