import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested chaotic mappings with fractal noise injection
        chaotic_term = np.sum(np.sin(30 * np.sin(np.cos(x))) * np.cos(15 * np.cos(np.sin(x))) * 
                             (1 + 0.1 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)))) / self.dim
        
        # Higher-order polynomial with dynamic coefficients based on dimensionality
        poly_term = np.sum((1.5 + 0.1 * np.sin(self.dim)) * x**7 - 
                          (0.9 + 0.05 * np.cos(self.dim)) * x**6 + 
                          (1.2 + 0.08 * np.sin(self.dim)) * x**5 - 
                          (0.7 + 0.03 * np.cos(self.dim)) * x**4 + 
                          (0.3 + 0.02 * np.sin(self.dim)) * x**3 - 
                          (0.1 + 0.01 * np.cos(self.dim)) * x**2 + 
                          (0.8 + 0.04 * np.sin(self.dim)) * x) / self.dim
        
        # Quantum-inspired barrier with phase modulation and dynamic scaling
        barrier_term = np.sum(np.exp(-x**2 / (2.0 + 0.5 * np.sin(self.dim))) * 
                             np.sin(5 * x + 0.2 * np.cos(self.dim)) * 
                             np.cos(2 * x + 0.1 * np.sin(self.dim)) * 
                             np.sin(x/3.0 + 0.05 * np.cos(self.dim))) / self.dim
        
        # Multi-scale chaotic attractor with fractal-like behavior and dynamic exponents
        attractor_term = np.sum(np.sin(np.exp(x/2.0 + 0.1 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/3.0 + 0.05 * np.cos(self.dim))) * 
                               np.sin(x/4.0 + 0.03 * np.sin(self.dim)) * 
                               np.cos(x/5.0 + 0.02 * np.cos(self.dim))) / self.dim
        
        # Adaptive cross-dimensional coupling with dynamic weights and fractal scaling
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.0 + 0.3 * np.sin(i + self.dim)
                cross_term += weight * np.abs(x[i] - x[i+1])**(1.8 + 0.2 * np.sin(i + 0.5 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Composite noise with quantum-like randomness and fractal characteristics
        noise = (0.01 * np.random.rand() + 
                0.005 * np.sin(np.sum(x**2)) + 
                0.003 * np.cos(np.sum(x**3)) + 
                0.002 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.001 * np.sin(self.dim) * np.cos(np.sum(x)))
        
        # Dynamic weighting based on problem dimensionality
        weights = [0.35 + 0.05 * np.sin(self.dim), 
                  0.20 + 0.03 * np.cos(self.dim), 
                  0.25 + 0.02 * np.sin(self.dim), 
                  0.15 + 0.01 * np.cos(self.dim), 
                  0.05 + 0.01 * np.sin(self.dim)]
        
        # Combine all terms with dynamic weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise