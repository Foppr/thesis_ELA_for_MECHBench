import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with multiple nested mappings and fractal scaling
        chaotic_term = np.sum(np.sin(25 * np.sin(np.cos(x))) * np.cos(12 * np.cos(np.sin(x))) * 
                             (1 + 0.15 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3))) * 
                             np.exp(-0.1 * np.sum(x**2))) / self.dim
        
        # Modified polynomial with dynamic exponents and adaptive coefficients
        poly_term = np.sum((2.0 + 0.2 * np.sin(self.dim)) * x**8 - 
                          (1.0 + 0.1 * np.cos(self.dim)) * x**7 + 
                          (1.5 + 0.15 * np.sin(self.dim)) * x**6 - 
                          (0.8 + 0.08 * np.cos(self.dim)) * x**5 + 
                          (0.4 + 0.04 * np.sin(self.dim)) * x**4 - 
                          (0.2 + 0.02 * np.cos(self.dim)) * x**3 + 
                          (0.9 + 0.05 * np.sin(self.dim)) * x**2 - 
                          (0.3 + 0.03 * np.cos(self.dim)) * x) / self.dim
        
        # Quantum-inspired oscillatory barrier with enhanced phase modulation
        barrier_term = np.sum(np.exp(-x**2 / (1.5 + 0.3 * np.sin(self.dim))) * 
                             np.sin(6 * x + 0.25 * np.cos(self.dim)) * 
                             np.cos(3 * x + 0.15 * np.sin(self.dim)) * 
                             np.sin(x/2.5 + 0.06 * np.cos(self.dim)) * 
                             np.exp(-0.05 * np.sum(x**2))) / self.dim
        
        # Multi-scale chaotic attractor with enhanced fractal-like behavior and dynamic exponents
        attractor_term = np.sum(np.sin(np.exp(x/1.5 + 0.15 * np.sin(self.dim))) * 
                               np.cos(np.exp(-x/2.5 + 0.1 * np.cos(self.dim))) * 
                               np.sin(x/3.5 + 0.04 * np.sin(self.dim)) * 
                               np.cos(x/4.5 + 0.03 * np.cos(self.dim)) * 
                               np.exp(-0.02 * np.sum(x**2))) / self.dim
        
        # Enhanced adaptive cross-dimensional coupling with dynamic weights and fractal scaling
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.2 + 0.4 * np.sin(i + self.dim)
                cross_term += weight * np.abs(x[i] - x[i+1])**(2.0 + 0.3 * np.sin(i + 0.6 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Improved composite noise with quantum-like randomness and fractal characteristics
        noise = (0.015 * np.random.rand() + 
                0.008 * np.sin(np.sum(x**2)) + 
                0.005 * np.cos(np.sum(x**3)) + 
                0.004 * np.sin(np.sum(x**4)) * np.cos(np.sum(x**5)) + 
                0.003 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.002 * np.cos(self.dim) * np.sin(np.sum(x**2)))
        
        # Dynamic weighting based on problem dimensionality with improved balance
        weights = [0.30 + 0.04 * np.sin(self.dim), 
                  0.25 + 0.04 * np.cos(self.dim), 
                  0.20 + 0.03 * np.sin(self.dim), 
                  0.18 + 0.02 * np.cos(self.dim), 
                  0.07 + 0.01 * np.sin(self.dim)]
        
        # Combine all terms with dynamic weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise