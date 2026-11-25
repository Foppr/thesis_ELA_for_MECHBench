import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with hyper-chaotic modulation
        exp_term = np.sum(np.exp(-x**2 / 2.5) * np.sin(4 * x) * np.cos(3 * x)) / self.dim
        
        # Multi-frequency trigonometric interference with fractional radial symmetry breaking
        trig_term = np.sum(np.sin(x) * np.cos(2 * x) * np.sin(6 * x) * np.cos(8 * x) * np.exp(-x**2 / 15.0)) / self.dim
        
        # Saddle point structure with dynamic polynomial interaction and hyperbolic perturbation
        saddle_term = np.sum(x**7 * np.sin(x)**4 + x**5 * np.cos(x)**4 + np.tanh(x**2)) / (self.dim * 20.0)
        
        # Chaos-inducing component with time-varying oscillation and fractional gradient
        chaos_term = np.sum(np.sin(x**2) * np.cos(x) * np.exp(-x**2 / 8.0) * np.tan(x/3)) / self.dim
        
        # Additional multimodal component with dynamic scaling, cross-terms, and hyperbolic functions
        multi_term = np.sum(np.sin(8 * x) * np.cos(4 * x) * np.exp(-x**2 / 5.0) + x**6 * np.sin(x)**3 + np.log(1.0 + np.abs(x))) / self.dim
        
        # Novel radial symmetry breaking component with fractional polynomial interactions and hyperbolic tangent
        radial_break = np.sum((np.abs(x) ** 1.9) * np.sin(5 * x) * np.cos(7 * x) * np.tanh(x)) / self.dim
        
        # Dynamic weighting based on input magnitude for adaptive difficulty with exponential factor
        weight_factor = 1.0 + 0.6 * np.mean(np.abs(x)) / 5.0 + 0.2 * np.std(x) / 5.0
        
        # Add a novel chaotic gradient modulation component with hyperbolic secant
        grad_mod = np.sum(np.sin(x) * np.cos(4 * x) * np.exp(-x**2 / 9.0) * (1.0 + 0.15 * np.sin(3 * x)) * np.sech(x)) / self.dim
        
        # Introduce a new hyper-chaotic component with multiple interacting frequencies and fractional exponents
        hyperchaos = np.sum(np.sin(x**3.5) * np.cos(x**2.5) * np.exp(-x**2 / 14.0) * np.tan(x/2.5)) / self.dim
        
        # Add a novel fractal-like component with recursive trigonometric interactions
        fractal_term = np.sum(np.sin(np.pi * x) * np.cos(np.pi * x) * np.exp(-x**2 / 10.0) * np.sin(9 * x)) / self.dim
        
        total = (0.2 * exp_term + 0.3 * trig_term + 0.15 * saddle_term + 
                0.1 * chaos_term + 0.08 * multi_term + 0.06 * radial_break + 
                0.05 * grad_mod + 0.04 * hyperchaos + 0.02 * fractal_term) * weight_factor
        
        return total