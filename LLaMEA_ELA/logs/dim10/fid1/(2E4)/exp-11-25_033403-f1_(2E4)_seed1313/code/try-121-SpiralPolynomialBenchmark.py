import numpy as np

class SpiralPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 3.0
        self.exp_factor = 2.0
        self.log_factor = 1.5
        self.rotation_angle = np.pi / 4.0
        self.adaptive_scale = np.random.uniform(0.5, 2.0, dim)
        self.spiral_centers = np.random.uniform(-3.0, 3.0, (dim, dim))
        self.spiral_radii = np.random.uniform(1.0, 3.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with adaptive scaling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**2) * (x[i]**self.poly_degree) * self.adaptive_scale[i]
            
        # Exponential component with spiral rotation
        exp_term = 0.0
        for i in range(self.dim):
            rotated_coord = x[i] * np.cos(self.rotation_angle) - x[(i+1) % self.dim] * np.sin(self.rotation_angle)
            exp_term += self.exp_factor * np.exp(-0.5 * (rotated_coord / 2.0)**2)
            
        # Logarithmic component with spiral structure
        log_term = 0.0
        for i in range(self.dim):
            spiral_radius = np.sqrt((x[i] - self.spiral_centers[i, 0])**2 + (x[(i+1) % self.dim] - self.spiral_centers[i, 1])**2)
            log_term += self.log_factor * np.log(spiral_radius + 1e-8)
            
        # Cross-dimensional spiral interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + (x[(i+1) % self.dim] - x[(j+1) % self.dim])**2)
                cross_term += np.sin(dist * 0.5) * np.cos(0.3 * dist)
                
        # Adaptive conditioning with spiral modulation
        cond_term = 0.0
        for i in range(self.dim):
            modulator = 1.0 + 0.5 * np.sin(i * self.rotation_angle)
            cond_term += modulator * x[i]**4
            
        # Combined fitness function
        total = poly_term + exp_term + log_term + cross_term + cond_term
        
        return total