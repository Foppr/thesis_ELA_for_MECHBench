import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic mappings with increased frequency modulation and amplitude scaling
        chaotic_term = np.sum(np.sin(31 * np.sin(np.cos(x))) * np.cos(17 * np.cos(np.sin(x))) * 
                             (1 + 0.25 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3))) * 
                             np.exp(-0.1 * np.sum(x**2))) / self.dim
        
        # Refined higher-order polynomial with adaptive coefficients and additional terms
        poly_term = np.sum((1.7 + 0.2 * np.sin(self.dim)) * x**7 - 
                          (1.5 + 0.1 * np.cos(self.dim)) * x**6 + 
                          (1.4 + 0.15 * np.sin(self.dim)) * x**5 - 
                          (1.2 + 0.08 * np.cos(self.dim)) * x**4 + 
                          (0.8 + 0.06 * np.sin(self.dim)) * x**3 - 
                          (0.5 + 0.05 * np.cos(self.dim)) * x**2 + 
                          (1.2 + 0.08 * np.sin(self.dim)) * x + 
                          0.1 * np.sin(np.sum(x))) / self.dim
        
        # Enhanced quantum-inspired barrier with phase modulation and exponential scaling
        barrier_term = np.sum(np.exp(-x**2 / (2.0 + 0.9 * np.sin(self.dim))) * 
                             np.sin(6.0 * x + 0.4 * np.cos(self.dim)) * 
                             np.cos(2.0 * x + 0.25 * np.sin(self.dim)) * 
                             np.sin(x/2.5 + 0.1 * np.cos(self.dim)) * 
                             np.exp(-0.05 * np.sum(x**2))) / self.dim
        
        # Advanced multi-scale chaotic attractor with modified exponents and coupling
        attractor_term = np.sum(np.sin(np.exp(x/2.0 + 0.2 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/3.0 + 0.15 * np.cos(self.dim))) * 
                               np.sin(x/3.5 + 0.08 * np.sin(self.dim)) * 
                               np.cos(x/4.5 + 0.07 * np.cos(self.dim)) * 
                               np.exp(-0.1 * np.sum(x**2))) / self.dim
        
        # Improved adaptive cross-dimensional coupling with dynamic weights and modified exponents
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.6 + 0.4 * np.sin(i + self.dim * 0.9)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.5 + 0.3 * np.sin(i + 0.8 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Refined composite noise with enhanced stochastic characteristics
        noise = (0.02 * np.random.rand() + 
                0.01 * np.sin(np.sum(x**2)) + 
                0.008 * np.cos(np.sum(x**3)) + 
                0.007 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.005 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.003 * np.cos(np.sum(x**2)) * np.sin(np.sum(x**3)))
        
        # Dynamic weighting with improved balance between terms
        weights = [0.38 + 0.09 * np.sin(self.dim), 
                  0.28 + 0.07 * np.cos(self.dim), 
                  0.22 + 0.06 * np.sin(self.dim), 
                  0.18 + 0.05 * np.cos(self.dim), 
                  0.14 + 0.04 * np.sin(self.dim)]
        
        # Combine all terms with refined weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise