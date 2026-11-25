import numpy as np

class MultiModalAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with adaptive scaling
        exp_decay = np.sum(np.exp(-0.1 * np.abs(x)) * np.cos(2.0 * x))
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * i
            amp = 1.0 / (1.0 + 0.1 * i)
            trig_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * self.dim
        
        # Cross-dimensional interaction with varying coupling strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                coupling_strength = 1.0 / (1.0 + (i-j)**2)
                cross_term += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Polynomial and rational components for additional complexity
        poly_component = np.sum(x**4) / (1.0 + np.sum(x**2))
        rational_component = np.sum(1.0 / (1.0 + x**2)) * np.sin(0.5 * np.sum(x**2))
        
        # Final multi-modal combination with adaptive weights
        result = condition_factor * (exp_decay + trig_sum + cross_term + poly_component + rational_component)
        
        return result