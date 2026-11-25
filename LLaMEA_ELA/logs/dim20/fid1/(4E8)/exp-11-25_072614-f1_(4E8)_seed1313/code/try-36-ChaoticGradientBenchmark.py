import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial decay term with varying exponents
        polynomial = np.sum(x**2) + 0.5 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Chaotic gradient components using trigonometric functions
        chaotic = np.sum(np.sin(x) * np.cos(2.0 * x)) + 0.3 * np.sum(np.sin(3.0 * x) * np.cos(x))
        
        # Saddle point structure with hyperbolic tangent
        saddle = np.sum(np.tanh(x) * x**2) + 0.2 * np.sum(np.tanh(x**3))
        
        # Logarithmic perturbations to create irregularity and fine-scale structure
        log_perturbation = np.sum(np.log(1.0 + 0.1 * x**2)) + 0.05 * np.sum(np.log(1.0 + x**4))
        
        # Combined function with global minimum at origin
        return polynomial + chaotic + saddle + log_perturbation + 0.01 * np.sum(x**8)