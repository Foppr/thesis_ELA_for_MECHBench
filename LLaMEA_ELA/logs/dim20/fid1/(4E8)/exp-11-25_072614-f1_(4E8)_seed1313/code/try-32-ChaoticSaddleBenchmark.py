import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with logarithmic barrier near origin
        r = np.sqrt(np.sum(x**2))
        radial = r * (1.0 + 0.5 * np.sin(r)) + 0.1 * np.log(r + 1e-8)
        
        # Saddle-point structure with alternating hyperbolic tangents
        saddle = np.sum(np.tanh(x) * x**2) + 0.3 * np.sum(np.tanh(x**3))
        
        # Chaotic perturbation using sine of exponential terms
        chaotic = np.sum(np.sin(np.exp(x))) + 0.2 * np.sum(np.cos(np.exp(0.5 * x**2)))
        
        # Gradient variation with polynomial modulation
        gradient_mod = np.sum((x**2 + 0.1 * x**4) * np.cos(2.0 * x))
        
        # Combine all components with global minimum at origin
        return radial + saddle + chaotic + gradient_mod + 0.05 * np.sum(x**8)