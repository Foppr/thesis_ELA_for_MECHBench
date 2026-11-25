import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with modified scaling
        exp_term = np.sum(np.exp(-x**2 / 2.0)) / self.dim
        
        # Modified trigonometric frequencies with coupling terms
        trig_term = np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) + np.sin(3.0 * x) * np.cos(6.0 * x)) / self.dim
        
        # Saddle point structure with increased polynomial complexity
        saddle_term = np.sum(x**6 * np.sin(x)**2 + x**5 * np.cos(x)**2) / (self.dim * 20.0)
        
        # Chaos-inducing logarithmic component with additional oscillation
        chaos_term = np.sum(np.log(1.0 + x**2) * np.sin(1.5 * x) * np.cos(0.8 * x)) / self.dim
        
        # Additional multimodal component with altered amplitude
        multi_term = np.sum(np.sin(7 * x) * np.exp(-x**2 / 5.0)) / self.dim
        
        # Adaptive weighting to balance components
        total = 0.30 * exp_term + 0.40 * trig_term + 0.20 * saddle_term + 0.05 * chaos_term + 0.05 * multi_term
        
        return total