import numpy as np

class ExponentialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay and oscillation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-0.1 * r) * np.sin(2.0 * r) * np.cos(0.5 * r)
        
        # Exponential decay with trigonometric modulation
        exp_decay_sum = 0.0
        for i in range(self.dim):
            exp_decay_sum += np.exp(-0.5 * x[i]**2) * np.sin(3.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Asymmetric coupling between dimensions
        asym_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_coupling += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Polynomial and hyperbolic components for added complexity
        poly_term = np.sum(x**4) * np.tanh(0.1 * r)
        hyperbolic_term = np.sum(np.sinh(0.3 * x)) * np.cosh(0.2 * r)
        
        # Final combination with weight adjustments
        result = 0.5 * radial_term + 0.3 * exp_decay_sum + 0.2 * asym_coupling + 0.1 * poly_term + 0.1 * hyperbolic_term
        
        return result