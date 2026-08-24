import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with frequency modulation and phase shifts
        chaotic_term = np.sum(np.sin(20 * np.sin(x)) * np.cos(7 * np.cos(x))) / self.dim
        
        # Higher-order polynomial terms to increase ruggedness
        poly_term = np.sum(x**6 + 0.3 * x**5 - 0.8 * x**4 + 2.0 * x**3 - 1.2 * x**2 + 0.8 * x) / self.dim
        
        # Modified exponential barrier with sharper transitions
        barrier_term = np.sum(np.exp(-x**2 / 2.0) * np.sin(3 * x) * np.cos(0.5 * x)) / self.dim
        
        # Novel chaotic attractor with multi-scale oscillations
        attractor_term = np.sum(np.sin(np.exp(x/1.5)) * np.cos(np.exp(-x/2.5)) * np.sin(x/2.0)) / self.dim
        
        # Enhanced cross-dimensional interactions with non-linear coupling
        cross_term = np.sum(np.abs(x[:-1] - x[1:])**1.5) / (self.dim - 1) if self.dim > 1 else 0
        
        # Add a composite noise term with temporal correlation
        noise = 0.005 * np.random.rand() + 0.003 * np.sin(np.sum(x))
        
        # Combine all terms with optimized weights
        result = 0.35 * chaotic_term + 0.3 * poly_term + 0.2 * barrier_term + 0.1 * attractor_term + 0.05 * cross_term
        
        return result + noise