import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested chaotic mappings with fractal noise injection
        chaotic_term = np.sum(np.sin(35 * np.sin(np.cos(x))) * np.cos(12 * np.cos(np.sin(x))) * 
                             (1 + 0.15 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)))) / self.dim
        
        # Higher-order polynomial with dynamic coefficients based on dimensionality
        poly_term = np.sum((1.8 + 0.12 * np.sin(self.dim)) * x**7 - 
                          (1.1 + 0.06 * np.cos(self.dim)) * x**6 + 
                          (1.4 + 0.09 * np.sin(self.dim)) * x**5 - 
                          (0.8 + 0.04 * np.cos(self.dim)) * x**4 + 
                          (0.4 + 0.03 * np.sin(self.dim)) * x**3 - 
                          (0.15 + 0.015 * np.cos(self.dim)) * x**2 + 
                          (0.9 + 0.05 * np.sin(self.dim)) * x) / self.dim
        
        # Quantum-inspired barrier with phase modulation and dynamic scaling
        barrier_term = np.sum(np.exp(-x**2 / (1.8 + 0.6 * np.sin(self.dim))) * 
                             np.sin(6 * x + 0.25 * np.cos(self.dim)) * 
                             np.cos(2.5 * x + 0.15 * np.sin(self.dim)) * 
                             np.sin(x/2.5 + 0.06 * np.cos(self.dim))) / self.dim
        
        # Multi-scale chaotic attractor with fractal-like behavior and dynamic exponents
        attractor_term = np.sum(np.sin(np.exp(x/1.8 + 0.12 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/2.8 + 0.06 * np.cos(self.dim))) * 
                               np.sin(x/3.8 + 0.04 * np.sin(self.dim)) * 
                               np.cos(x/4.8 + 0.03 * np.cos(self.dim))) / self.dim
        
        # Adaptive cross-dimensional coupling with dynamic weights and fractal scaling
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.2 + 0.25 * np.sin(i + self.dim)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.0 + 0.15 * np.sin(i + 0.6 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Composite noise with quantum-like randomness and fractal characteristics
        noise = (0.012 * np.random.rand() + 
                0.006 * np.sin(np.sum(x**2)) + 
                0.004 * np.cos(np.sum(x**3)) + 
                0.003 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.0015 * np.sin(self.dim) * np.cos(np.sum(x)))
        
        # Dynamic weighting based on problem dimensionality
        weights = [0.32 + 0.06 * np.sin(self.dim), 
                  0.22 + 0.04 * np.cos(self.dim), 
                  0.23 + 0.03 * np.sin(self.dim), 
                  0.17 + 0.02 * np.cos(self.dim), 
                  0.06 + 0.015 * np.sin(self.dim)]
        
        # Combine all terms with dynamic weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise