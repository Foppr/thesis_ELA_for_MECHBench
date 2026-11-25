import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic tent map component for dynamic landscape modulation
        chaotic_term = 0
        a = 1.5
        for i in range(self.dim):
            xi = x_norm[i]
            if xi < 0.5:
                tent_val = a * xi
            else:
                tent_val = a * (1 - xi)
            chaotic_term += tent_val * np.sin(2 * np.pi * xi) * (1 + 0.3 * np.cos(5 * xi))
        
        # Spherical harmonic expansion with varying frequencies
        sph_harm_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                r = np.sqrt(x_norm[i]**2 + x_norm[j]**2)
                theta = np.arctan2(x_norm[j], x_norm[i])
                sph_harm_term += (r**2) * np.sin(3 * theta) * np.cos(4 * theta) * \
                                (1 + 0.2 * np.sin(7 * r) * np.cos(5 * r))
        
        # Asymmetric gradient flow with directional bias
        grad_term = 0
        for i in range(self.dim):
            # Directional bias based on dimension index
            bias = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            grad_term += (x_norm[i]**3) * (1 + 0.4 * np.cos(3 * x_norm[i])) * bias
            
        # Cross-dimensional coupling with exponential decay
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = np.exp(-dist) * (1 + 0.3 * np.sin(2 * dist))
                cross_term += coupling * x_norm[i]**2 * x_norm[j]**2
                
        # Non-linear transformation with piecewise polynomial
        poly_term = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                poly_val = x_norm[i]**4 + 0.5 * x_norm[i]**3 - 0.3 * x_norm[i]**2
            else:
                poly_val = x_norm[i]**5 - 0.4 * x_norm[i]**4 + 0.2 * x_norm[i]**3
            poly_term += poly_val * (1 + 0.25 * np.sin(6 * x_norm[i]))
        
        # Combine all components with optimized weights
        result = 1.8 * chaotic_term + 1.5 * sph_harm_term + 1.2 * grad_term + \
                1.0 * cross_term + 0.9 * poly_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise