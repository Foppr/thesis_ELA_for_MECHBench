import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for performance
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
        self.centers = np.random.uniform(-3.0, 3.0, (dim, 4))
        self.scales = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with polynomial chaos scaling
        f_val = np.sum(x**2) * (1.0 + 0.1 * np.sum(np.sin(self.coeffs * x)))
        
        # Radial basis functions with varying centers and scales
        for i in range(4):
            rb_term = 0.0
            for j in range(self.dim):
                rb_term += (x[j] - self.centers[j, i])**2 / (2.0 * self.scales[j]**2)
            f_val += 0.5 * np.exp(-rb_term)
            
        # Sinusoidal modulations with increasing frequency
        for i in range(self.dim):
            f_val += 0.3 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.2 * abs(x[i]))
            
        # Cross-dimensional polynomial interactions with chaotic coupling
        if self.dim >= 3:
            poly_interaction = 0.0
            for i in range(self.dim - 2):
                poly_interaction += (x[i] + x[i+1])**2 * (x[i+2]**3) * np.sin(0.5 * (x[i] + x[i+1] + x[i+2]))
            f_val += 0.2 * poly_interaction
            
        # Chaotic saddle structure with dynamic scaling
        if self.dim >= 2:
            saddle = 0.0
            for i in range(self.dim - 1):
                saddle += (x[i]**2 - x[i+1]**2)**2 * np.cos(0.3 * x[i]) * np.sin(0.4 * x[i+1])
            f_val += 0.25 * saddle
            
        # Additional multimodal components with tunable complexity
        for i in range(self.dim):
            f_val += 0.2 * np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.exp(-0.15 * abs(x[i])) * (1.0 + 0.2 * np.sin(5 * x[i]))
            
        # High-order polynomial with chaotic modulation
        f_val += 0.1 * np.sum(x**4) * np.sin(np.sum(x)**2)
        
        # Asymmetric Gaussian peaks with dynamic positioning
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                f_val += 0.15 * np.exp(-0.5 * ((x[i] - 1.0)**2 + (x[i+1] + 1.5)**2 + (x[i+2] - 2.0)**2))
                
        return f_val