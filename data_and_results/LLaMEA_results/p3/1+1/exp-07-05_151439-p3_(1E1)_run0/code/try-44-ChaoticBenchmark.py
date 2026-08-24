import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic mappings with higher frequency interactions and fractal-like coupling
        chaotic_term = np.sum(np.sin(31 * np.sin(np.cos(x))) * np.cos(17 * np.cos(np.sin(x))) * 
                             (1 + 0.23 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)) * np.sin(np.sum(x**4)))) / self.dim
        
        # Higher-order polynomial with increased complexity and dynamic coefficients
        poly_term = np.sum((1.7 + 0.19 * np.sin(self.dim)) * x**8 - 
                          (1.5 + 0.12 * np.cos(self.dim)) * x**7 + 
                          (1.3 + 0.15 * np.sin(self.dim)) * x**6 - 
                          (1.0 + 0.08 * np.cos(self.dim)) * x**5 + 
                          (0.7 + 0.06 * np.sin(self.dim)) * x**4 - 
                          (0.4 + 0.04 * np.cos(self.dim)) * x**3 + 
                          (0.2 + 0.03 * np.sin(self.dim)) * x**2 - 
                          (0.1 + 0.02 * np.cos(self.dim)) * x) / self.dim
        
        # Enhanced quantum-inspired barrier with multi-phase modulation and dynamic scaling
        barrier_term = np.sum(np.exp(-x**2 / (2.1 + 0.8 * np.sin(self.dim))) * 
                             np.sin(5.2 * x + 0.4 * np.cos(self.dim)) * 
                             np.cos(2.1 * x + 0.22 * np.sin(self.dim)) * 
                             np.sin(x/3.2 + 0.09 * np.cos(self.dim)) * 
                             np.cos(x/5.1 + 0.06 * np.sin(self.dim))) / self.dim
        
        # Enhanced multi-scale chaotic attractor with exponential coupling and dynamic exponents
        attractor_term = np.sum(np.sin(np.exp(x/2.1 + 0.18 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/3.1 + 0.12 * np.cos(self.dim))) * 
                               np.sin(x/4.2 + 0.07 * np.sin(self.dim)) * 
                               np.cos(x/6.3 + 0.05 * np.cos(self.dim)) * 
                               np.sin(x/7.4 + 0.03 * np.sin(self.dim))) / self.dim
        
        # Enhanced adaptive cross-dimensional coupling with non-linear weight functions and dynamic coupling
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.6 + 0.45 * np.sin(i + self.dim * 1.2)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.5 + 0.25 * np.sin(i + 0.9 * self.dim) + 0.15 * np.cos(i * 0.7 + self.dim * 0.5))
        cross_term /= (self.dim - 1)
        
        # Novel hybrid noise with multi-frequency components and dynamic amplitude modulation
        noise = (0.021 * np.random.rand() + 
                0.012 * np.sin(np.sum(x**2)) + 
                0.009 * np.cos(np.sum(x**3)) + 
                0.008 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.006 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.004 * np.cos(self.dim * 2) * np.sin(np.sum(x**6)) + 
                0.003 * np.sin(self.dim * 1.5) * np.cos(np.sum(x**7)))
        
        # Dynamic weighting with enhanced complexity and multi-scale modulation
        weights = [0.38 + 0.09 * np.sin(self.dim), 
                  0.32 + 0.07 * np.cos(self.dim), 
                  0.25 + 0.06 * np.sin(self.dim), 
                  0.20 + 0.05 * np.cos(self.dim), 
                  0.15 + 0.04 * np.sin(self.dim)]
        
        # Combine all terms with enhanced weighting and additional interaction
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise