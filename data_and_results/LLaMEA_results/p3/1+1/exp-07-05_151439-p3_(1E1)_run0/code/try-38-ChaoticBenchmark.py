import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic mapping with higher dimensional coupling
        chaotic_term = np.sum(np.sin(30 * np.sin(np.cos(x))) * np.cos(15 * np.cos(np.sin(x))) * 
                             (1 + 0.2 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)) * np.sin(np.sum(x**4)))) / self.dim
        
        # Higher-order polynomial with dynamic coefficients and additional terms
        poly_term = np.sum((1.5 + 0.15 * np.sin(self.dim)) * x**8 - 
                          (1.3 + 0.08 * np.cos(self.dim)) * x**7 + 
                          (1.2 + 0.07 * np.sin(self.dim)) * x**6 - 
                          (1.0 + 0.05 * np.cos(self.dim)) * x**5 + 
                          (0.8 + 0.04 * np.sin(self.dim)) * x**4 - 
                          (0.6 + 0.03 * np.cos(self.dim)) * x**3 + 
                          (0.5 + 0.02 * np.sin(self.dim)) * x**2 - 
                          (0.3 + 0.01 * np.cos(self.dim)) * x) / self.dim
        
        # Enhanced quantum-inspired barrier with multi-frequency modulation
        barrier_term = np.sum(np.exp(-x**2 / (2.0 + 0.7 * np.sin(self.dim))) * 
                             np.sin(5 * x + 0.3 * np.cos(self.dim)) * 
                             np.cos(2.0 * x + 0.2 * np.sin(self.dim)) * 
                             np.sin(x/3.0 + 0.07 * np.cos(self.dim)) * 
                             np.cos(x/4.0 + 0.05 * np.sin(self.dim))) / self.dim
        
        # Enhanced multi-scale chaotic attractor with dynamic exponents
        attractor_term = np.sum(np.sin(np.exp(x/2.0 + 0.15 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/3.0 + 0.10 * np.cos(self.dim))) * 
                               np.sin(x/4.0 + 0.05 * np.sin(self.dim)) * 
                               np.cos(x/5.0 + 0.04 * np.cos(self.dim)) * 
                               np.sin(x/6.0 + 0.03 * np.sin(self.dim))) / self.dim
        
        # Complex adaptive cross-dimensional coupling with non-linear weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.5 + 0.3 * np.sin(i + self.dim * 0.8)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.5 + 0.2 * np.sin(i + 0.7 * self.dim) + 0.1 * np.cos(i + 0.5 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Novel hybrid fractal noise with chaotic modulation
        noise = (0.015 * np.random.rand() + 
                0.008 * np.sin(np.sum(x**2)) + 
                0.005 * np.cos(np.sum(x**3)) + 
                0.004 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.003 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.002 * np.cos(self.dim) * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)) + 
                0.001 * np.sin(np.sum(x**6)) * np.cos(np.sum(x**7)))
        
        # Dynamic weighting with enhanced complexity
        weights = [0.35 + 0.07 * np.sin(self.dim), 
                  0.28 + 0.05 * np.cos(self.dim), 
                  0.22 + 0.04 * np.sin(self.dim), 
                  0.15 + 0.03 * np.cos(self.dim), 
                  0.08 + 0.02 * np.sin(self.dim)]
        
        # Combine all terms with enhanced weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise