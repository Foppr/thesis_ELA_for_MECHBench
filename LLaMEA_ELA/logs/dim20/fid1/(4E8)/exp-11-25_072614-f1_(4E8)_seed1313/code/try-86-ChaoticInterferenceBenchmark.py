import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with chaotic modulation
        exp_term = np.sum(np.exp(-x**2 / 2.5) * np.sin(4 * x) * np.cos(2 * x)) / self.dim
        
        # Multi-frequency trigonometric interference with radial symmetry breaking
        trig_term = np.sum(np.sin(x) * np.cos(3 * x) * np.sin(6 * x) * np.cos(8 * x) * np.exp(-x**2 / 4.0)) / self.dim
        
        # Saddle point structure with dynamic polynomial interaction and logarithmic perturbation
        saddle_term = np.sum(x**7 * np.sin(x)**4 + x**5 * np.cos(x)**4 + np.log(1.0 + x**3)) / (self.dim * 20.0)
        
        # Chaos-inducing component with time-varying oscillation and radial gradient
        chaos_term = np.sum(np.sin(x**2) * np.cos(x) * np.exp(-x**2 / 8.0) * np.tan(x/3)) / self.dim
        
        # Additional multimodal component with dynamic scaling and cross-terms
        multi_term = np.sum(np.sin(8 * x) * np.cos(4 * x) * np.exp(-x**2 / 5.0) + x**6 * np.sin(x)**3) / self.dim
        
        # Novel radial symmetry breaking component with fractional polynomial interactions
        radial_break = np.sum((np.abs(x) ** 2.1) * np.sin(5 * x) * np.cos(7 * x) * np.exp(-x**2 / 6.0)) / self.dim
        
        # Dynamic weighting based on input magnitude for adaptive difficulty
        weight_factor = 1.0 + 0.7 * np.mean(np.abs(x)) / 5.0
        
        # Add a novel chaotic gradient modulation component
        grad_mod = np.sum(np.sin(x) * np.cos(4 * x) * np.exp(-x**2 / 9.0) * (1.0 + 0.15 * np.sin(3 * x))) / self.dim
        
        # Introduce a new hyperchaotic component with multiple interacting frequencies
        hyperchaos = np.sum(np.sin(x**4) * np.cos(x**3) * np.exp(-x**2 / 15.0) * np.tan(x/4)) / self.dim
        
        # Add a novel fractional-order chaotic component for increased complexity
        frac_chaos = np.sum((np.abs(x) ** 1.3) * np.sin(2 * x) * np.cos(5 * x) * np.exp(-x**2 / 7.0)) / self.dim
        
        # Introduce a novel harmonic interference term with variable amplitude
        harmonic_term = np.sum(np.sin(9 * x) * np.cos(3 * x) * np.exp(-x**2 / 10.0) * (1.0 + 0.2 * np.cos(x))) / self.dim
        
        # Introduce a new component for better fitness score optimization
        novel_component = np.sum(np.sin(7 * x) * np.cos(5 * x) * np.exp(-x**2 / 3.0) * (1.0 + 0.1 * np.sin(2 * x))) / self.dim
        
        total = (0.2 * exp_term + 0.3 * trig_term + 0.15 * saddle_term + 
                0.1 * chaos_term + 0.08 * multi_term + 0.06 * radial_break + 
                0.05 * grad_mod + 0.04 * hyperchaos + 0.03 * frac_chaos + 
                0.02 * harmonic_term + 0.01 * novel_component) * weight_factor
        
        return total