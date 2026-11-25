import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with radial distance
        r = np.sqrt(np.sum(x**2))
        exp_decay = np.exp(-0.1 * r) * np.sin(2.0 * r)
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.5
            amp = 1.0 / (1.0 + i * 0.2)
            trig_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0
        if self.dim > 5:
            condition_factor = 1.0 + 0.1 * (self.dim - 5)
        
        # Cross-dimensional interaction with polynomial coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                poly_coupling += 0.3 * (x[i]**2) * (x[j]**2) * np.sin(0.5 * x[i] * x[j])
        
        # Additional harmonic components with different phase shifts
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += np.sin(x[i] + np.cos(x[i])) * np.exp(-0.05 * x[i]**2)
        
        # Final combination with scaling and offset
        result = condition_factor * (exp_decay + trig_sum + poly_coupling + harmonic_sum) + 0.1 * r
        
        return result