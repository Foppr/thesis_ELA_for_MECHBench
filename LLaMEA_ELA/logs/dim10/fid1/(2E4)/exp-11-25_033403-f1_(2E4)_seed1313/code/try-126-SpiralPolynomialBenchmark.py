import numpy as np

class SpiralPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4.0
        self.exp_factor = 1.5
        self.log_weight = 2.0
        self.rotation_angle = np.pi / 6.0
        self.adaptive_scale = np.random.uniform(0.3, 2.5, dim)
        self.spiral_centers = np.random.uniform(-2.5, 2.5, (dim, dim))
        self.spiral_radii = np.random.uniform(0.5, 2.5, dim)
        self.barrier_height = np.random.uniform(1.0, 3.0, dim)
        self.barrier_width = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with higher degree and adaptive scaling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**2) * (x[i]**self.poly_degree) * self.adaptive_scale[i]
            
        # Exponential component with spiral rotation and modified decay
        exp_term = 0.0
        for i in range(self.dim):
            rotated_x = x[i] * np.cos(self.rotation_angle) - x[(i+1) % self.dim] * np.sin(self.rotation_angle)
            exp_term += self.exp_factor * np.exp(-0.3 * (rotated_x / 1.5)**2)
            
        # Logarithmic component with spiral structure and enhanced barrier effects
        log_term = 0.0
        for i in range(self.dim):
            center = self.spiral_centers[i, (i+1) % self.dim]
            radius = self.spiral_radii[i]
            distance = np.sqrt((x[i] - center)**2 + (x[(i+1) % self.dim] - center)**2)
            log_term += self.log_weight * np.log(1.0 + distance / radius)
            
        # Cross-dimensional spiral interaction with enhanced coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = x[(i+1) % self.dim] - x[(j+1) % self.dim]
                distance = np.sqrt(dx**2 + dy**2)
                cross_term += np.sin(2.0 * distance) * np.cos(0.3 * distance)
                
        # Adaptive conditioning with barrier mechanisms
        cond_term = 0.0
        for i in range(self.dim):
            # Add barrier effect to increase difficulty near boundaries
            barrier = self.barrier_height[i] * np.exp(-0.5 * ((x[i] - 5.0) / self.barrier_width[i])**2)
            barrier += self.barrier_height[i] * np.exp(-0.5 * ((x[i] + 5.0) / self.barrier_width[i])**2)
            cond_term += (np.exp(self.adaptive_scale[i] * x[i]) - 1.0) + barrier
            
        # Combined fitness function with balanced weights
        total = 0.8 * poly_term + 0.6 * exp_term + 0.7 * log_term + 0.5 * cross_term + 0.9 * cond_term
        
        return total