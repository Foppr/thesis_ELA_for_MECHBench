import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay term with adaptive scaling
        exp_term = np.sum(np.exp(-x**2 / 5.0)) / self.dim
        
        # Trigonometric interference pattern with multiple frequencies
        trig_term = np.sum(np.sin(x) * np.cos(2 * x) * np.sin(4 * x)) / self.dim
        
        # Saddle point structure with higher-order polynomial interaction
        saddle_term = np.sum(x**4 * np.sin(x)**2 + x**3 * np.cos(x)**2) / (self.dim * 10.0)
        
        # Chaos-inducing logarithmic component with added oscillation
        chaos_term = np.sum(np.log(1.0 + x**2) * np.sin(x)) / self.dim
        
        # Additional multimodal component for increased complexity
        multi_term = np.sum(np.sin(5 * x) * np.exp(-x**2 / 8.0)) / self.dim
        
        # Adaptive weighting to balance components
        total = 0.3 * exp_term + 0.4 * trig_term + 0.2 * saddle_term + 0.05 * chaos_term + 0.05 * multi_term
        
        return total