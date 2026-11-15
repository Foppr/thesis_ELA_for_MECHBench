import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.weights = np.random.uniform(0.3, 3.0, 20)
        # Additional cross-dimensional interaction terms
        self.cross_weights = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Additional chaotic components for increased complexity
        self.chaotic_coeffs = np.random.uniform(0.05, 1.5, (7, dim))
        # New hyperbolic tangent and polynomial components
        self.poly_weights = np.random.uniform(-0.5, 0.5, (3, dim))
        # Additional noise term
        self.noise_level = 0.05
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gaussian_sum = 0.0
        for i in range(20):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.25 ** 2))
        
        # Enhanced chaotic sinusoidal perturbation component with multiple frequencies
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(9 * xi) * np.cos(7 * xi) * np.sin(11 * xi) + 
                           0.7 * np.sin(15 * xi) * np.cos(5 * xi) * np.sin(13 * xi) + 
                           0.5 * np.sin(8 * xi) * np.cos(6 * xi) * np.sin(10 * xi) +
                           0.3 * np.sin(17 * xi) * np.cos(4 * xi) * np.sin(14 * xi) +
                           0.4 * np.sin(19 * xi) * np.cos(3 * xi) * np.sin(16 * xi) +
                           0.2 * np.sin(21 * xi) * np.cos(2 * xi) * np.sin(18 * xi) +
                           0.1 * np.sin(23 * xi) * np.cos(1 * xi) * np.sin(20 * xi))
        
        # Logarithmic conditioning term with additional sine modulation
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi) + 0.3 * np.sin(3 * xi) + 0.1 * np.sin(4 * xi))
        
        # Cross-dimensional cubic interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += self.cross_weights[i, j] * (x[i] ** 3) * x[j]
        
        # Quadratic basin component with conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Additional chaotic interaction term
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    chaotic_interaction += self.chaotic_coeffs[0, i] * self.chaotic_coeffs[1, j] * np.sin(x[i] * x[j])
        
        # Hyperbolic tangent and polynomial components
        tanh_term = 0.0
        poly_term = 0.0
        for i in range(self.dim):
            tanh_term += np.tanh(x[i]) * np.sin(2 * x[i])
            poly_term += self.poly_weights[0, i] * (x[i] ** 5) + self.poly_weights[1, i] * (x[i] ** 4) + self.poly_weights[2, i] * (x[i] ** 3)
        
        # Combine all components with different weights
        result = 0.25 * gaussian_sum + 0.2 * chaotic_sum + 0.15 * log_conditioning + 0.15 * cross_term + 0.1 * quadratic_term + 0.1 * chaotic_interaction + 0.05 * tanh_term + 0.05 * poly_term
        
        # Add noise to increase robustness testing
        result += np.random.normal(0, self.noise_level)
        
        return result