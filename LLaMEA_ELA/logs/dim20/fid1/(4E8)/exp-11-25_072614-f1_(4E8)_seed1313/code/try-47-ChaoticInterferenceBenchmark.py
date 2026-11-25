import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay term with altered scaling
        exp_term = np.sum(np.exp(-x**2 / 3.0)) / self.dim
        
        # Trigonometric interference pattern with modified frequencies
        trig_term = np.sum(np.sin(1.5 * x) * np.cos(3 * x) * np.sin(5 * x)) / self.dim
        
        # Saddle point structure with enhanced polynomial interaction
        saddle_term = np.sum(x**5 * np.sin(x)**2 + x**4 * np.cos(x)**2) / (self.dim * 15.0)
        
        # Chaos-inducing logarithmic component with added oscillation
        chaos_term = np.sum(np.log(1.0 + x**2) * np.sin(1.2 * x)) / self.dim
        
        # Additional multimodal component for increased complexity
        multi_term = np.sum(np.sin(6 * x) * np.exp(-x**2 / 6.0)) / self.dim
        
        # Adaptive weighting to balance components
        total = 0.25 * exp_term + 0.45 * trig_term + 0.25 * saddle_term + 0.03 * chaos_term + 0.02 * multi_term
        
        return total