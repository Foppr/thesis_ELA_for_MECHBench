import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic mappings with higher frequency components and fractal modulation
        chaotic_term = np.sum(np.sin(41 * np.sin(np.cos(x))) * np.cos(23 * np.cos(np.sin(x))) * 
                             (1 + 0.32 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)) * 
                              np.sin(np.sum(x**4)))) / self.dim
        
        # Highly modified polynomial with increased degree terms and dynamic coefficients
        poly_term = np.sum((2.1 + 0.23 * np.sin(self.dim)) * x**9 - 
                          (1.9 + 0.18 * np.cos(self.dim)) * x**8 + 
                          (1.7 + 0.16 * np.sin(self.dim)) * x**7 - 
                          (1.5 + 0.14 * np.cos(self.dim)) * x**6 + 
                          (1.3 + 0.12 * np.sin(self.dim)) * x**5 - 
                          (1.1 + 0.10 * np.cos(self.dim)) * x**4 + 
                          (0.9 + 0.08 * np.sin(self.dim)) * x**3 - 
                          (0.7 + 0.06 * np.cos(self.dim)) * x**2 + 
                          (1.3 + 0.09 * np.sin(self.dim)) * x) / self.dim
        
        # Enhanced quantum-inspired barrier with multi-phase modulation and complex interference
        barrier_term = np.sum(np.exp(-x**2 / (2.2 + 1.1 * np.sin(self.dim))) * 
                             np.sin(7.0 * x + 0.45 * np.cos(self.dim)) * 
                             np.cos(2.2 * x + 0.25 * np.sin(self.dim)) * 
                             np.sin(x/2.5 + 0.12 * np.cos(self.dim)) * 
                             np.cos(x/3.5 + 0.09 * np.sin(self.dim))) / self.dim
        
        # Complex multi-scale chaotic attractor with non-integer exponents and dynamic scaling
        attractor_term = np.sum(np.sin(np.exp(x/1.5 + 0.22 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/3.5 + 0.15 * np.cos(self.dim))) * 
                               np.sin(x/3.0 + 0.08 * np.sin(self.dim)) * 
                               np.cos(x/6.0 + 0.07 * np.cos(self.dim)) * 
                               np.sin(x/4.0 + 0.05 * np.sin(self.dim))) / self.dim
        
        # Advanced adaptive cross-dimensional coupling with dynamic weights and fractional exponents
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.8 + 0.45 * np.sin(i + self.dim * 0.95)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.7 + 0.35 * np.sin(i + 0.85 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Novel fractal-based noise with hierarchical scaling and multi-frequency components
        noise = (0.024 * np.random.rand() + 
                0.012 * np.sin(np.sum(x**2)) + 
                0.009 * np.cos(np.sum(x**3)) + 
                0.007 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.005 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.003 * np.cos(np.sum(x**6)) * np.sin(np.sum(x**7)) + 
                0.002 * np.sin(np.sum(x**8)) * np.cos(np.sum(x**9)))
        
        # Enhanced dynamic weighting with multi-scale factors and dimensionality-dependent adjustments
        weights = [0.42 + 0.12 * np.sin(self.dim), 
                  0.35 + 0.10 * np.cos(self.dim), 
                  0.28 + 0.08 * np.sin(self.dim), 
                  0.22 + 0.06 * np.cos(self.dim), 
                  0.18 + 0.05 * np.sin(self.dim)]
        
        # Combine all terms with enhanced weighting and added interaction effects
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise