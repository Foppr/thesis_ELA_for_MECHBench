import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Chaotic sine-wave interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 2.0 * np.sin(10 * x[i]) * np.cos(7 * x[i]) + 1.5 * np.sin(15 * x[i])
            
        # Adaptive polynomial conditioning with dimension-dependent exponents
        for i in range(self.dim):
            exponent = 2 + 0.5 * (i % 4)
            f_val += 0.8 * (x[i]**exponent) * np.sin(3 * x[i]) + 0.3 * (x[i]**(exponent + 1)) * np.cos(2 * x[i])
            
        # Cross-dimensional exponential penalties with varying decay rates
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                distance = np.sqrt((x[i] - x[j])**2 + 0.01)
                decay_rate = 0.5 + 0.3 * (i % 3) / 2.0
                f_val += 1.2 * np.exp(-decay_rate * distance**2) * np.sin(5 * (x[i] + x[j]))
                
        # Radial basis function interactions with dynamic centers and varying scales
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            for j in range(min(3, self.dim)):
                if i + j < self.dim:
                    center = centers[j % len(centers)]
                    distance = np.sqrt((x[i] - center)**2 + 0.1)
                    f_val += 0.5 * np.exp(-distance**2) * np.cos(4 * x[i]) * np.sin(3 * x[i+j])
                    
        # Multi-scale harmonic terms with varying frequencies and coupling strengths
        for i in range(self.dim):
            f_val += 0.6 * np.sin(12 * x[i]) * np.cos(5 * x[i]) + 0.4 * np.sin(20 * x[i]) * np.cos(8 * x[i])
            
        # Additional chaotic polynomial interactions
        for i in range(self.dim):
            f_val += 0.1 * (x[i]**7) * np.sin(0.5 * x[i]) + 0.05 * (x[i]**9) * np.cos(0.3 * x[i])
            
        # Global conditioning with high-order polynomial terms
        f_val += 0.02 * np.sum(x**14) + 0.01 * np.sum(x**16)
        
        # Cross-dimensional coupling with non-linear transformations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if (i + j) % 3 == 0:
                    f_val += 0.25 * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    
        return f_val