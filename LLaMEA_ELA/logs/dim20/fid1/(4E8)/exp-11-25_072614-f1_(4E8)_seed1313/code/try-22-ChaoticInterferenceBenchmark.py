import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay term
        exp_term = np.sum(np.exp(-x**2 / 10.0)) / self.dim
        
        # Trigonometric interference pattern
        trig_term = np.sum(np.sin(x) * np.cos(3 * x)) / self.dim
        
        # Saddle point structure with polynomial interaction
        saddle_term = np.sum(x**2 * np.sin(x)**2) / (self.dim * 10.0)
        
        # Chaos-inducing logarithmic component
        chaos_term = np.sum(np.log(1.0 + x**2)) / self.dim
        
        return exp_term + trig_term + saddle_term + chaos_term