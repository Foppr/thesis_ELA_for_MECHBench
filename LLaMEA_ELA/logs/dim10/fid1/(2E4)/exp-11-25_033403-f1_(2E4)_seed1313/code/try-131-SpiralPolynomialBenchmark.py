import numpy as np

class SpiralPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4
        self.exp_factor = 0.8
        self.log_factor = 1.2
        self.rotation_scale = 0.5
        self.adaptive_conditioning = np.random.uniform(0.4, 2.8, dim)
        self.spiral_coefficients = np.random.uniform(-0.9, 0.9, dim)
        self.barrier_strength = np.random.uniform(1.2, 3.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying degrees and barrier effects
        poly_term = 0.0
        for i in range(self.dim):
            degree = self.poly_degree + int(i * 0.3) % 5
            barrier = 1.0 / (1.0 + np.exp(-self.barrier_strength[i] * x[i]))
            poly_term += (x[i] ** degree) * barrier * np.cos(0.25 * x[i])
            
        # Exponential component with enhanced adaptive scaling and coupling
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(self.exp_factor * x[i]) * np.sin(x[i] * self.adaptive_conditioning[i]) * np.cos(0.15 * x[i])
            
        # Logarithmic component with improved spiral-like structure and multi-scale interactions
        log_term = 0.0
        for i in range(self.dim):
            # Create enhanced spiral effect using multiple rotation angles
            spiral_angle = 0.0
            for j in range(min(4, i)):
                spiral_angle += self.spiral_coefficients[j] * x[i-j-1]
            spiral_angle += self.spiral_coefficients[i] * np.sum(x[:i]) if i > 0 else 0
            
            rotated_x = x[i] * np.cos(spiral_angle) - x[(i+1) % self.dim] * np.sin(spiral_angle)
            log_term += np.log(np.abs(rotated_x) + 0.6) * np.sin(0.35 * rotated_x) * (1.0 + 0.15 * np.sin(i * 0.4))
            
        # Cross-dimensional spiral coupling with enhanced complexity
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create complex interaction pattern with multiple distance metrics
                dist1 = np.sqrt((x[i] - x[j])**2 + (x[(i+1) % self.dim] - x[(j+1) % self.dim])**2)
                dist2 = np.abs(x[i] - x[j]) + np.abs(x[(i+1) % self.dim] - x[(j+1) % self.dim])
                cross_term += (np.sin(dist1 * self.rotation_scale) * np.cos(dist2 * self.rotation_scale) + 
                              0.6 * np.sin(dist1 * dist2 * 0.12)) * (1.0 + 0.35 * np.sin(i * j * 0.25))
                
        # Adaptive conditioning with enhanced polynomial scaling and multi-dimensional coupling
        cond_term = 0.0
        for i in range(self.dim):
            cond_factor = self.adaptive_conditioning[i] * (1.0 + 0.35 * np.sin(i * 0.9))
            cond_term += cond_factor * x[i]**(self.poly_degree + 2) * np.cos(0.12 * x[i])
            
        # Additional barrier and conditioning terms to improve discrimination
        barrier_term = 0.0
        for i in range(self.dim):
            # Add steeper barriers near the boundaries
            barrier_term += 12.0 * (1.0 / (1.0 + np.exp(-6.0 * (x[i] - 4.0))) + 
                                  1.0 / (1.0 + np.exp(6.0 * (x[i] + 4.0))))
            
        # Combined fitness function with balanced weighting
        total = 0.75 * poly_term + 0.65 * exp_term + 0.75 * log_term + 0.55 * cross_term + 0.85 * cond_term + 0.45 * barrier_term
        
        return total