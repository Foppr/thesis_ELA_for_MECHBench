import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants for fractal structure
        self.logistic_r = 3.95
        self.logistic_seed = 0.7
        self.fractal_scale = 1.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal component using iterated logistic maps
        logistic_vals = np.full(self.dim, self.logistic_seed)
        for _ in range(10):  # Iterate logistic map for chaos
            logistic_vals = self.logistic_r * logistic_vals * (1 - logistic_vals)
        
        # Self-similar fractal polynomial with varying exponents
        fractal_poly = 0
        for i in range(self.dim):
            exp_factor = 2 + 3 * np.sin(logistic_vals[i] * np.pi)
            fractal_poly += (x[i]**exp_factor) * np.cos(2 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Saddle-point distribution with dynamic weights
        saddle = 0
        for i in range(self.dim):
            # Dynamic weight based on logistic map
            weight = 1.0 + 0.5 * np.sin(logistic_vals[i] * 2 * np.pi)
            saddle += weight * (x[i]**3 - 3 * x[i]) * np.sin(0.5 * x[i])
        
        # Complex-valued polynomial interactions
        complex_poly = 0
        for i in range(self.dim):
            # Use imaginary component for complex interactions
            z = x[i] + 1j * np.sin(x[i])
            complex_poly += np.real(z**3 + 0.5 * z**2 + 0.1 * z)
        
        # Adaptive conditioning through dynamic scaling
        adaptive_scale = np.mean(np.abs(x)) + 1.0
        conditioning = 0.5 * adaptive_scale * np.sum(x**2) * np.sin(0.1 * np.sum(x**2))
        
        # Combine all components with dynamic weighting
        return 0.3 * fractal_poly + 0.3 * saddle + 0.2 * complex_poly + 0.2 * conditioning