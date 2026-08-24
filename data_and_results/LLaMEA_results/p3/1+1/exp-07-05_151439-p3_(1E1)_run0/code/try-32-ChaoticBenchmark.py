import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic mappings with multi-fractal scaling and dynamic phase modulation
        chaotic_term = np.sum(np.sin(35 * np.sin(np.cos(x))) * np.cos(20 * np.cos(np.sin(x))) * 
                             (1 + 0.15 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)) + 
                              0.05 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)))) / self.dim
        
        # Higher-order polynomial with dynamic coefficients and multi-scale exponents
        poly_term = np.sum((2.0 + 0.15 * np.sin(self.dim)) * x**8 - 
                          (1.2 + 0.08 * np.cos(self.dim)) * x**7 + 
                          (1.8 + 0.12 * np.sin(self.dim)) * x**6 - 
                          (1.1 + 0.06 * np.cos(self.dim)) * x**5 + 
                          (0.9 + 0.05 * np.sin(self.dim)) * x**4 - 
                          (0.6 + 0.03 * np.cos(self.dim)) * x**3 + 
                          (0.5 + 0.02 * np.sin(self.dim)) * x**2 - 
                          (0.3 + 0.01 * np.cos(self.dim)) * x) / self.dim
        
        # Quantum-inspired barrier with phase modulation, dynamic scaling, and complex coupling
        barrier_term = np.sum(np.exp(-x**2 / (2.5 + 0.6 * np.sin(self.dim))) * 
                             np.sin(6 * x + 0.25 * np.cos(self.dim)) * 
                             np.cos(3 * x + 0.15 * np.sin(self.dim)) * 
                             np.sin(x/2.5 + 0.06 * np.cos(self.dim)) * 
                             np.cos(x/4.0 + 0.04 * np.sin(self.dim))) / self.dim
        
        # Multi-scale chaotic attractor with fractal-like behavior, dynamic exponents, and hybrid coupling
        attractor_term = np.sum(np.sin(np.exp(x/1.5 + 0.15 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/2.5 + 0.08 * np.cos(self.dim))) * 
                               np.sin(x/3.5 + 0.04 * np.sin(self.dim)) * 
                               np.cos(x/6.0 + 0.03 * np.cos(self.dim)) * 
                               np.sin(x/8.0 + 0.02 * np.sin(self.dim))) / self.dim
        
        # Adaptive cross-dimensional coupling with dynamic weights, fractal scaling, and hybrid interaction
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.2 + 0.4 * np.sin(i + self.dim + 0.5 * np.cos(i))
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.0 + 0.3 * np.sin(i + 0.6 * self.dim) + 
                                                              0.1 * np.cos(i + 0.4 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Composite noise with quantum-like randomness, fractal characteristics, and dynamic amplitude modulation
        noise = (0.015 * np.random.rand() + 
                0.008 * np.sin(np.sum(x**2)) + 
                0.005 * np.cos(np.sum(x**3)) + 
                0.004 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.003 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.002 * np.cos(self.dim) * np.sin(np.sum(x**2)) + 
                0.001 * np.sin(2 * self.dim) * np.cos(np.sum(x**3)))
        
        # Dynamic weighting with enhanced multi-scale characteristics and hybrid term interactions
        weights = [0.40 + 0.06 * np.sin(self.dim), 
                  0.25 + 0.04 * np.cos(self.dim), 
                  0.20 + 0.03 * np.sin(self.dim), 
                  0.10 + 0.02 * np.cos(self.dim), 
                  0.05 + 0.01 * np.sin(self.dim)]
        
        # Combine all terms with dynamic weighting and enhanced interaction
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise