import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with chaotic modulation
        exp_term = np.sum(np.exp(-x**2 / 3.0) * np.sin(3 * x)) / self.dim
        
        # Multi-frequency trigonometric interference with radial symmetry breaking
        trig_term = np.sum(np.sin(x) * np.cos(2 * x) * np.sin(5 * x) * np.cos(7 * x)) / self.dim
        
        # Saddle point structure with dynamic polynomial interaction and logarithmic perturbation
        saddle_term = np.sum(x**6 * np.sin(x)**3 + x**4 * np.cos(x)**3 + np.log(1.0 + x**2)) / (self.dim * 15.0)
        
        # Chaos-inducing component with time-varying oscillation and radial gradient
        chaos_term = np.sum(np.sin(x**2) * np.cos(x) * np.exp(-x**2 / 10.0)) / self.dim
        
        # Additional multimodal component with dynamic scaling and cross-terms
        multi_term = np.sum(np.sin(7 * x) * np.cos(3 * x) * np.exp(-x**2 / 6.0) + x**5 * np.sin(x)**2) / self.dim
        
        # Novel radial symmetry breaking component with fractional polynomial interactions
        radial_break = np.sum((np.abs(x) ** 1.7) * np.sin(4 * x) * np.cos(6 * x)) / self.dim
        
        # Dynamic weighting based on input magnitude for adaptive difficulty
        weight_factor = 1.0 + 0.5 * np.mean(np.abs(x)) / 5.0
        
        # Add a novel chaotic gradient modulation component
        grad_mod = np.sum(np.sin(x) * np.cos(3 * x) * np.exp(-x**2 / 8.0) * (1.0 + 0.1 * np.sin(2 * x))) / self.dim
        
        # Introduce a new hyperchaotic component with multiple interacting frequencies
        hyperchaos = np.sum(np.sin(x**3) * np.cos(x**2) * np.exp(-x**2 / 12.0) * np.tan(x/2)) / self.dim
        
        total = (0.25 * exp_term + 0.35 * trig_term + 0.2 * saddle_term + 
                0.1 * chaos_term + 0.1 * multi_term + 0.05 * radial_break + 
                0.05 * grad_mod + 0.05 * hyperchaos) * weight_factor
        
        return total