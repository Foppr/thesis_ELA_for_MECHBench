import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with chaotic modulation and hyperbolic tangent
        exp_term = np.sum(np.exp(-x**2 / 3.0) * np.tanh(3 * x)) / self.dim
        
        # Multi-frequency trigonometric interference with radial symmetry breaking and cubic terms
        trig_term = np.sum(np.sin(x) * np.cos(2 * x) * np.sin(5 * x) * np.cos(7 * x) * np.tanh(x**3)) / self.dim
        
        # Saddle point structure with dynamic polynomial interaction, logarithmic perturbation and hyperbolic secant
        saddle_term = np.sum(x**6 * np.sin(x)**3 + x**4 * np.cos(x)**3 + np.log(1.0 + x**2) * np.sech(x)) / (self.dim * 15.0)
        
        # Chaos-inducing component with time-varying oscillation, radial gradient and Gaussian kernel
        chaos_term = np.sum(np.sin(x**2) * np.cos(x) * np.exp(-x**2 / 10.0) * np.exp(-x**4 / 50.0)) / self.dim
        
        # Additional multimodal component with dynamic scaling, cross-terms and hyperbolic cotangent
        multi_term = np.sum(np.sin(7 * x) * np.cos(3 * x) * np.exp(-x**2 / 6.0) + x**5 * np.sin(x)**2 * np.coth(x)) / self.dim
        
        # Hyperbolic tangent weighted dynamic difficulty factor
        weight_factor = 1.0 + 0.5 * np.mean(np.tanh(np.abs(x))) / 5.0
        
        # Additional hyperbolic sine component for increased complexity
        sinh_term = np.sum(np.sinh(x) * np.cos(4 * x)) / self.dim
        
        total = (0.2 * exp_term + 0.3 * trig_term + 0.15 * saddle_term + 
                0.15 * chaos_term + 0.1 * multi_term + 0.1 * sinh_term) * weight_factor
        
        return total