import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested chaotic mappings with quantum-like interference
        chaotic_term = np.sum(np.sin(30 * np.sin(np.cos(x))) * np.cos(15 * np.cos(np.sin(x)))) / self.dim
        
        # Higher-order polynomial with adaptive coefficients
        poly_term = np.sum(1.5 * x**7 - 0.9 * x**6 + 1.2 * x**5 - 0.7 * x**4 + 0.3 * x**3 - 0.1 * x**2 + 0.8 * x) / self.dim
        
        # Quantum-inspired barrier with phase modulation
        barrier_term = np.sum(np.exp(-x**2 / 3.0) * np.sin(5 * x) * np.cos(2 * x) * np.sin(x/3.0)) / self.dim
        
        # Multi-scale chaotic attractor with fractal-like behavior
        attractor_term = np.sum(np.sin(np.exp(x/2.0)) * np.cos(np.exp(-x/3.0)) * np.sin(x/4.0) * np.cos(x/5.0)) / self.dim
        
        # Adaptive cross-dimensional coupling with dynamic weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_term += np.abs(x[i] - x[i+1])**(1.8 + 0.2 * np.sin(i))
        cross_term /= (self.dim - 1)
        
        # Composite noise with quantum-like randomness
        noise = 0.01 * np.random.rand() + 0.005 * np.sin(np.sum(x**2)) + 0.003 * np.cos(np.sum(x**3))
        
        # Combine all terms with dynamic weighting
        result = 0.4 * chaotic_term + 0.25 * poly_term + 0.2 * barrier_term + 0.1 * attractor_term + 0.05 * cross_term
        
        return result + noise