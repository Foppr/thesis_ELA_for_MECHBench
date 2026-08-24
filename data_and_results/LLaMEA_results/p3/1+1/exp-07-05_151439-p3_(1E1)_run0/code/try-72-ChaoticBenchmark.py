import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic mappings with altered frequencies and modified fractal noise
        chaotic_term = np.sum(np.sin(37 * np.sin(np.cos(x))) * np.cos(29 * np.cos(np.sin(x))) * 
                             (1 + 0.42 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)) * 
                              np.sin(np.sum(x**4)))) / self.dim
        
        # Modified polynomial with different degree terms and dynamic coefficients
        poly_term = np.sum((2.1 + 0.28 * np.sin(self.dim)) * x**8 - 
                          (2.3 + 0.22 * np.cos(self.dim)) * x**7 + 
                          (1.8 + 0.19 * np.sin(self.dim)) * x**6 - 
                          (1.6 + 0.15 * np.cos(self.dim)) * x**5 + 
                          (1.4 + 0.13 * np.sin(self.dim)) * x**4 - 
                          (1.2 + 0.11 * np.cos(self.dim)) * x**3 + 
                          (1.0 + 0.09 * np.sin(self.dim)) * x**2 - 
                          (0.8 + 0.07 * np.cos(self.dim)) * x) / self.dim
        
        # Modified quantum-inspired barrier with different modulation phases
        barrier_term = np.sum(np.exp(-x**2 / (2.3 + 1.1 * np.sin(self.dim))) * 
                             np.sin(6.8 * x + 0.4 * np.cos(self.dim)) * 
                             np.cos(2.3 * x + 0.25 * np.sin(self.dim)) * 
                             np.sin(x/2.5 + 0.12 * np.cos(self.dim)) * 
                             np.cos(x/3.5 + 0.10 * np.sin(self.dim))) / self.dim
        
        # Modified multi-scale chaotic attractor with different exponents
        attractor_term = np.sum(np.sin(np.exp(x/1.5 + 0.22 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/3.5 + 0.16 * np.cos(self.dim))) * 
                               np.sin(x/3.1 + 0.09 * np.sin(self.dim)) * 
                               np.cos(x/6.0 + 0.08 * np.cos(self.dim)) * 
                               np.sin(x/4.0 + 0.06 * np.sin(self.dim))) / self.dim
        
        # Adjusted adaptive cross-dimensional coupling with modified weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.8 + 0.4 * np.sin(i + self.dim * 0.95)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.7 + 0.3 * np.sin(i + 0.8 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Refined fractal-based noise with updated hierarchical scaling
        noise = (0.024 * np.random.rand() + 
                0.013 * np.sin(np.sum(x**2)) + 
                0.010 * np.cos(np.sum(x**3)) + 
                0.007 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.005 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.003 * np.cos(np.sum(x**6)) * np.sin(np.sum(x**7)) + 
                0.002 * np.sin(np.sum(x**8)) * np.cos(np.sum(x**9)))
        
        # Updated dynamic weighting with modified scale factors
        weights = [0.42 + 0.12 * np.sin(self.dim), 
                  0.35 + 0.10 * np.cos(self.dim), 
                  0.30 + 0.08 * np.sin(self.dim), 
                  0.24 + 0.06 * np.cos(self.dim), 
                  0.19 + 0.05 * np.sin(self.dim)]
        
        # Combine all terms with updated weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise