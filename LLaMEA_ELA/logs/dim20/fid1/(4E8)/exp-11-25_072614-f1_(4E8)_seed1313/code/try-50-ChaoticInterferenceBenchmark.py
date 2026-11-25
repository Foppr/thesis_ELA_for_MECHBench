import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with chaotic modulation
        exp_term = np.sum(np.exp(-x**2 / 3.0) * np.sin(3 * x)) / self.dim
        
        # Multi-frequency trigonometric interference with dynamic phase shifts
        trig_term = np.sum(np.sin(x) * np.cos(2 * x) * np.sin(4 * x) * np.cos(5 * x)) / self.dim
        
        # Dynamic saddle point structure with radial symmetry and polynomial coupling
        saddle_term = np.sum((x**4 + x**2) * np.sin(x)**2 * np.cos(x)**2) / (self.dim * 5.0)
        
        # Chaos-inducing logarithmic perturbation with adaptive scaling
        chaos_term = np.sum(np.log(1.0 + x**2) * np.sin(x) * np.exp(-x**2 / 10.0)) / self.dim
        
        # Enhanced multimodal component with radial basis and cross-terms
        multi_term = np.sum(np.sin(7 * x) * np.exp(-x**2 / 6.0) + x**3 * np.cos(3 * x)) / self.dim
        
        # Additional radial symmetry and higher-order polynomial coupling
        radial_term = np.sum((np.linalg.norm(x)**2) * np.sin(x)**3 + (np.linalg.norm(x)**3) * np.cos(x)**2) / (self.dim * 8.0)
        
        # Adaptive weighting with chaotic scaling factors
        total = 0.25 * exp_term + 0.35 * trig_term + 0.15 * saddle_term + 0.08 * chaos_term + 0.07 * multi_term + 0.1 * radial_term
        
        return total