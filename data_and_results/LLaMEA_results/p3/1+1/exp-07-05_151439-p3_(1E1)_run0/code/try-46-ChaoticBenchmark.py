import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Modified chaotic mappings with altered frequencies and amplitudes
        chaotic_term = np.sum(np.sin(31 * np.sin(np.cos(x))) * np.cos(17 * np.cos(np.sin(x))) * 
                             (1 + 0.21 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)))) / self.dim
        
        # Adjusted higher-order polynomial with modified coefficients and exponents
        poly_term = np.sum((1.6 + 0.15 * np.sin(self.dim)) * x**8 - 
                          (1.4 + 0.09 * np.cos(self.dim)) * x**7 + 
                          (1.3 + 0.12 * np.sin(self.dim)) * x**6 - 
                          (1.1 + 0.06 * np.cos(self.dim)) * x**5 + 
                          (0.7 + 0.05 * np.sin(self.dim)) * x**4 - 
                          (0.5 + 0.04 * np.cos(self.dim)) * x**3 + 
                          (1.2 + 0.08 * np.sin(self.dim)) * x**2 - 
                          (0.8 + 0.03 * np.cos(self.dim)) * x) / self.dim
        
        # Modified quantum-inspired barrier with different phase modulation
        barrier_term = np.sum(np.exp(-x**2 / (1.8 + 0.8 * np.sin(self.dim))) * 
                             np.sin(5.0 * x + 0.35 * np.cos(self.dim)) * 
                             np.cos(1.8 * x + 0.20 * np.sin(self.dim)) * 
                             np.sin(x/3.0 + 0.08 * np.cos(self.dim))) / self.dim
        
        # Modified multi-scale chaotic attractor with altered exponents
        attractor_term = np.sum(np.sin(np.exp(x/2.0 + 0.16 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/3.0 + 0.11 * np.cos(self.dim))) * 
                               np.sin(x/4.0 + 0.06 * np.sin(self.dim)) * 
                               np.cos(x/5.0 + 0.05 * np.cos(self.dim))) / self.dim
        
        # Modified adaptive cross-dimensional coupling with different weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.5 + 0.35 * np.sin(i + self.dim * 0.9)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.3 + 0.25 * np.sin(i + 0.8 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Modified composite noise with altered characteristics
        noise = (0.016 * np.random.rand() + 
                0.008 * np.sin(np.sum(x**2)) + 
                0.006 * np.cos(np.sum(x**3)) + 
                0.005 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.003 * np.sin(self.dim) * np.cos(np.sum(x)))
        
        # Modified dynamic weighting based on problem dimensionality
        weights = [0.35 + 0.08 * np.sin(self.dim), 
                  0.30 + 0.06 * np.cos(self.dim), 
                  0.25 + 0.05 * np.sin(self.dim), 
                  0.23 + 0.04 * np.cos(self.dim), 
                  0.12 + 0.03 * np.sin(self.dim)]
        
        # Combine all terms with modified weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise