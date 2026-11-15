import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic mappings with altered frequency components and modified noise
        chaotic_term = np.sum(np.sin(47 * np.sin(np.cos(x))) * np.cos(29 * np.cos(np.sin(x))) * 
                             (1 + 0.4 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)) * 
                              np.sin(np.sum(x**4)))) / self.dim
        
        # Modified polynomial with altered degree terms and dynamic coefficients
        poly_term = np.sum((2.5 + 0.30 * np.sin(self.dim)) * x**9 - 
                          (2.3 + 0.25 * np.cos(self.dim)) * x**8 + 
                          (2.1 + 0.20 * np.sin(self.dim)) * x**7 - 
                          (1.9 + 0.18 * np.cos(self.dim)) * x**6 + 
                          (1.7 + 0.16 * np.sin(self.dim)) * x**5 - 
                          (1.5 + 0.14 * np.cos(self.dim)) * x**4 + 
                          (1.3 + 0.12 * np.sin(self.dim)) * x**3 - 
                          (1.1 + 0.10 * np.cos(self.dim)) * x**2 + 
                          (1.7 + 0.13 * np.sin(self.dim)) * x) / self.dim
        
        # Modified quantum-inspired barrier with different modulation
        barrier_term = np.sum(np.exp(-x**2 / (2.7 + 1.3 * np.sin(self.dim))) * 
                             np.sin(8.0 * x + 0.6 * np.cos(self.dim)) * 
                             np.cos(2.7 * x + 0.35 * np.sin(self.dim)) * 
                             np.sin(x/2.9 + 0.18 * np.cos(self.dim)) * 
                             np.cos(x/4.0 + 0.14 * np.sin(self.dim))) / self.dim
        
        # Modified multi-scale chaotic attractor with different exponents
        attractor_term = np.sum(np.sin(np.exp(x/1.9 + 0.30 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/4.0 + 0.20 * np.cos(self.dim))) * 
                               np.sin(x/3.5 + 0.12 * np.sin(self.dim)) * 
                               np.cos(x/6.5 + 0.10 * np.cos(self.dim)) * 
                               np.sin(x/4.5 + 0.08 * np.sin(self.dim))) / self.dim
        
        # Modified adaptive cross-dimensional coupling with altered weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 2.2 + 0.6 * np.sin(i + self.dim * 0.95)
                cross_term += weight * np.abs(x[i] - x[i+1])**(3.1 + 0.45 * np.sin(i + 0.85 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Modified fractal-based noise with different scaling factors
        noise = (0.028 * np.random.rand() + 
                0.016 * np.sin(np.sum(x**2)) + 
                0.013 * np.cos(np.sum(x**3)) + 
                0.009 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.007 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.005 * np.cos(np.sum(x**6)) * np.sin(np.sum(x**7)) + 
                0.004 * np.sin(np.sum(x**8)) * np.cos(np.sum(x**9)))
        
        # Modified dynamic weighting with adjusted factors
        weights = [0.47 + 0.14 * np.sin(self.dim), 
                  0.40 + 0.12 * np.cos(self.dim), 
                  0.33 + 0.10 * np.sin(self.dim), 
                  0.27 + 0.08 * np.cos(self.dim), 
                  0.22 + 0.07 * np.sin(self.dim)]
        
        # Combine all terms with modified weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise