import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave interactions with dynamic frequencies
        chaotic_term = np.sum(np.sin(31 * np.sin(np.cos(x))) * np.cos(17 * np.cos(np.sin(x))) * 
                             (1 + 0.23 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)))) / self.dim
        
        # Dynamic polynomial with varying exponents and adaptive coefficients
        poly_term = np.sum((1.7 + 0.19 * np.sin(self.dim)) * x**8 - 
                          (1.5 + 0.09 * np.cos(self.dim)) * x**7 + 
                          (1.3 + 0.12 * np.sin(self.dim)) * x**6 - 
                          (1.0 + 0.06 * np.cos(self.dim)) * x**5 + 
                          (0.7 + 0.05 * np.sin(self.dim)) * x**4 - 
                          (0.4 + 0.04 * np.cos(self.dim)) * x**3 + 
                          (0.2 + 0.03 * np.sin(self.dim)) * x**2 + 
                          (1.1 + 0.07 * np.cos(self.dim)) * x) / self.dim
        
        # Enhanced quantum-inspired barrier with phase modulation
        barrier_term = np.sum(np.exp(-x**2 / (2.1 + 0.8 * np.sin(self.dim))) * 
                             np.sin(5.2 * x + 0.4 * np.cos(self.dim)) * 
                             np.cos(2.1 * x + 0.21 * np.sin(self.dim)) * 
                             np.sin(x/3.2 + 0.08 * np.cos(self.dim))) / self.dim
        
        # Enhanced multi-scale chaotic attractor with modified exponents
        attractor_term = np.sum(np.sin(np.exp(x/2.1 + 0.17 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/3.1 + 0.11 * np.cos(self.dim))) * 
                               np.sin(x/4.1 + 0.06 * np.sin(self.dim)) * 
                               np.cos(x/5.1 + 0.05 * np.cos(self.dim))) / self.dim
        
        # Enhanced adaptive cross-dimensional coupling with dynamic weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.5 + 0.35 * np.sin(i + self.dim * 0.9)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.3 + 0.25 * np.sin(i + 0.8 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Enhanced composite noise with altered frequency characteristics
        noise = (0.018 * np.random.rand() + 
                0.009 * np.sin(np.sum(x**2)) + 
                0.006 * np.cos(np.sum(x**3)) + 
                0.005 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.003 * np.sin(self.dim) * np.cos(np.sum(x)))
        
        # Dynamic weighting based on problem dimensionality
        weights = [0.35 + 0.08 * np.sin(self.dim), 
                  0.30 + 0.06 * np.cos(self.dim), 
                  0.25 + 0.05 * np.sin(self.dim), 
                  0.20 + 0.04 * np.cos(self.dim), 
                  0.10 + 0.03 * np.sin(self.dim)]
        
        # Combine all terms with modified weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise