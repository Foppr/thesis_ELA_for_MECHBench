import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Modified chaotic mappings with altered frequencies and coupling
        chaotic_term = np.sum(np.sin(25 * np.sin(np.cos(x))) * np.cos(20 * np.cos(np.sin(x))) * 
                             (1 + 0.15 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)))) / self.dim
        
        # Modified polynomial with different dynamic coefficients
        poly_term = np.sum((2.0 + 0.12 * np.sin(self.dim)) * x**7 - 
                          (1.1 + 0.06 * np.cos(self.dim)) * x**6 + 
                          (1.4 + 0.09 * np.sin(self.dim)) * x**5 - 
                          (0.8 + 0.04 * np.cos(self.dim)) * x**4 + 
                          (0.4 + 0.03 * np.sin(self.dim)) * x**3 - 
                          (0.15 + 0.015 * np.cos(self.dim)) * x**2 + 
                          (0.9 + 0.05 * np.sin(self.dim)) * x) / self.dim
        
        # Modified quantum-inspired barrier with altered phase modulation
        barrier_term = np.sum(np.exp(-x**2 / (1.5 + 0.6 * np.sin(self.dim))) * 
                             np.sin(6 * x + 0.25 * np.cos(self.dim)) * 
                             np.cos(2.5 * x + 0.12 * np.sin(self.dim)) * 
                             np.sin(x/2.5 + 0.06 * np.cos(self.dim))) / self.dim
        
        # Modified multi-scale chaotic attractor with different exponents
        attractor_term = np.sum(np.sin(np.exp(x/1.5 + 0.12 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/2.5 + 0.06 * np.cos(self.dim))) * 
                               np.sin(x/3.5 + 0.04 * np.sin(self.dim)) * 
                               np.cos(x/4.5 + 0.03 * np.cos(self.dim))) / self.dim
        
        # Modified adaptive cross-dimensional coupling with different weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.2 + 0.25 * np.sin(i + self.dim)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.0 + 0.15 * np.sin(i + 0.6 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Modified composite noise with altered fractal characteristics
        noise = (0.012 * np.random.rand() + 
                0.006 * np.sin(np.sum(x**2)) + 
                0.004 * np.cos(np.sum(x**3)) + 
                0.003 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.0015 * np.sin(self.dim) * np.cos(np.sum(x)))
        
        # Modified dynamic weighting based on problem dimensionality
        weights = [0.30 + 0.06 * np.sin(self.dim), 
                  0.25 + 0.04 * np.cos(self.dim), 
                  0.20 + 0.03 * np.sin(self.dim), 
                  0.18 + 0.02 * np.cos(self.dim), 
                  0.07 + 0.015 * np.sin(self.dim)]
        
        # Combine all terms with modified weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise