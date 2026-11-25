import numpy as np

class SpiralPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4
        self.exp_factor = 0.5
        self.log_factor = 1.0
        self.rotation_scale = 0.3
        self.adaptive_conditioning = np.random.uniform(0.5, 2.0, dim)
        self.spiral_coefficients = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            degree = self.poly_degree + int(i * 0.3) % 3
            poly_term += (x[i] ** degree) * np.cos(0.5 * x[i])
            
        # Exponential component with adaptive scaling
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(self.exp_factor * x[i]) * np.sin(x[i] * self.adaptive_conditioning[i])
            
        # Logarithmic component with spiral-like structure
        log_term = 0.0
        for i in range(self.dim):
            # Create spiral effect using rotation and logarithmic scaling
            spiral_angle = self.spiral_coefficients[i] * np.sum(x[:i]) if i > 0 else 0
            rotated_x = x[i] * np.cos(spiral_angle) - x[(i+1) % self.dim] * np.sin(spiral_angle)
            log_term += np.log(np.abs(rotated_x) + 1.0) * np.sin(0.3 * rotated_x)
            
        # Cross-dimensional spiral coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create spiral-like interaction between dimensions
                dist = np.sqrt((x[i] - x[j])**2 + (x[(i+1) % self.dim] - x[(j+1) % self.dim])**2)
                cross_term += np.sin(dist * self.rotation_scale) * np.cos(dist * self.rotation_scale)
                
        # Adaptive conditioning with polynomial scaling
        cond_term = 0.0
        for i in range(self.dim):
            cond_factor = self.adaptive_conditioning[i] * (1.0 + 0.2 * np.sin(i * 0.7))
            cond_term += cond_factor * x[i]**(self.poly_degree - 1)
            
        # Combined fitness function
        total = poly_term + exp_term + log_term + cross_term + cond_term
        
        return total