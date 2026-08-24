import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Polynomial chaos expansion with Hermite polynomials
        chaos_term = 0.0
        for i in range(min(4, self.dim)):
            # Hermite polynomial of degree i+1
            if i == 0:
                h = x_norm[i]
            elif i == 1:
                h = 2 * x_norm[i] * x_norm[i] - 1
            elif i == 2:
                h = 4 * x_norm[i] * x_norm[i] * x_norm[i] - 3 * x_norm[i]
            else:
                h = 8 * x_norm[i] * x_norm[i] * x_norm[i] * x_norm[i] - 8 * x_norm[i] * x_norm[i] + 1
            chaos_term += (i + 1) * h * np.exp(-0.5 * x_norm[i]**2)
        
        # Radial basis function with multiple centers and varying widths
        rbf_term = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        widths = np.linspace(0.1, 0.5, min(5, self.dim))
        for i in range(min(5, self.dim)):
            rbf_term += np.exp(-0.5 * np.sum((x_norm - centers[i])**2) / widths[i]**2)
        
        # Cross-dimensional coupling with interaction terms
        cross_term = 0.0
        if self.dim > 1:
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    cross_term += np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j])
        
        # Multi-scale sinusoidal modulation with frequency scaling
        scale_term = 0.0
        for i in range(min(6, self.dim)):
            freq = 2**(i+1) * np.pi
            scale_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * (1.0 / (1.0 + i * 0.2))
        
        # Exponential decay with radial component
        exp_term = np.sum(np.exp(-0.1 * x_norm**2) * x_norm**4)
        
        # Combine all terms with dynamic weights
        dim_factor = 1.0 + 0.1 * (self.dim - 1)
        result = (0.25 * chaos_term + 
                 0.20 * rbf_term + 
                 0.20 * cross_term + 
                 0.20 * scale_term + 
                 0.15 * exp_term) * dim_factor
        
        return result