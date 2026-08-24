import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic nested mappings with multi-scale resonance
        chaotic_term = np.sum(np.sin(50 * np.sin(np.cos(x))) * np.cos(25 * np.cos(np.sin(x))) * 
                             (1 + 0.15 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3)) * 
                              np.sin(np.sum(x**4)))) / self.dim
        
        # Higher-order polynomial with multi-scale dynamic coefficients
        poly_term = np.sum((2.0 + 0.2 * np.sin(self.dim)) * x**8 - 
                          (1.2 + 0.08 * np.cos(self.dim)) * x**7 + 
                          (1.8 + 0.12 * np.sin(self.dim)) * x**6 - 
                          (1.1 + 0.06 * np.cos(self.dim)) * x**5 + 
                          (0.9 + 0.05 * np.sin(self.dim)) * x**4 - 
                          (0.6 + 0.03 * np.cos(self.dim)) * x**3 + 
                          (0.4 + 0.02 * np.sin(self.dim)) * x**2 - 
                          (0.2 + 0.01 * np.cos(self.dim)) * x) / self.dim
        
        # Quantum-inspired barrier with multi-frequency phase modulation
        barrier_term = np.sum(np.exp(-x**2 / (1.5 + 0.3 * np.sin(self.dim))) * 
                             np.sin(7 * x + 0.3 * np.cos(self.dim)) * 
                             np.cos(3 * x + 0.15 * np.sin(self.dim)) * 
                             np.sin(x/2.0 + 0.07 * np.cos(self.dim)) * 
                             np.cos(x/4.0 + 0.04 * np.sin(self.dim))) / self.dim
        
        # Multi-scale chaotic attractor with hyper-fractal behavior
        attractor_term = np.sum(np.sin(np.exp(x/1.5 + 0.2 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/2.5 + 0.1 * np.cos(self.dim))) * 
                               np.sin(x/3.5 + 0.05 * np.sin(self.dim)) * 
                               np.cos(x/6.0 + 0.03 * np.cos(self.dim)) * 
                               np.sin(x/8.0 + 0.02 * np.sin(self.dim))) / self.dim
        
        # Hyperchaotic cross-dimensional coupling with multi-scale exponents
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.2 + 0.4 * np.sin(i + self.dim + 0.5 * np.cos(i))
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.0 + 0.3 * np.sin(i + 0.7 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Composite noise with hyper-quantum randomness and multi-fractal characteristics
        noise = (0.02 * np.random.rand() + 
                0.01 * np.sin(np.sum(x**2)) + 
                0.008 * np.cos(np.sum(x**3)) + 
                0.006 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.004 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.003 * np.cos(2 * self.dim) * np.sin(np.sum(x**6)))
        
        # Dynamic weighting with multi-scale parameters
        weights = [0.40 + 0.06 * np.sin(self.dim), 
                  0.18 + 0.04 * np.cos(self.dim), 
                  0.22 + 0.03 * np.sin(self.dim), 
                  0.12 + 0.02 * np.cos(self.dim), 
                  0.08 + 0.01 * np.sin(self.dim)]
        
        # Combine all terms with dynamic weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise