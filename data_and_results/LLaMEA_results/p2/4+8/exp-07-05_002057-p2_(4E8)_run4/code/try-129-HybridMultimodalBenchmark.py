import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.weights = np.random.uniform(0.5, 3.0, 20)
        # Additional cross-dimensional interaction terms with adaptive weights
        self.cross_weights = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Additional chaotic modulation parameters with fractal-like scaling
        self.chaotic_params = np.random.uniform(0.05, 2.5, 15)
        # Adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        # Trigonometric coupling coefficients
        self.coupling_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component with enhanced variance
        gaussian_sum = 0.0
        for i in range(20):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.2 ** 2))
        
        # Enhanced chaotic sinusoidal perturbation with fractal scaling
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Add more chaotic terms with varying frequencies and amplitudes
            chaotic_sum += (self.chaotic_params[0] * np.sin(11 * xi) * np.cos(7 * xi) * np.sin(13 * xi) + 
                           self.chaotic_params[1] * np.sin(17 * xi) * np.cos(9 * xi) * np.sin(19 * xi) + 
                           self.chaotic_params[2] * np.sin(15 * xi) * np.cos(11 * xi) * np.sin(21 * xi) +
                           self.chaotic_params[3] * np.sin(23 * xi) * np.cos(13 * xi) * np.sin(25 * xi) +
                           self.chaotic_params[4] * np.sin(27 * xi) * np.cos(17 * xi) * np.sin(29 * xi) +
                           self.chaotic_params[5] * np.sin(31 * xi) * np.cos(19 * xi) * np.sin(33 * xi) +
                           self.chaotic_params[6] * np.sin(35 * xi) * np.cos(21 * xi) * np.sin(37 * xi) +
                           self.chaotic_params[7] * np.sin(39 * xi) * np.cos(23 * xi) * np.sin(41 * xi) +
                           self.chaotic_params[8] * np.sin(43 * xi) * np.cos(25 * xi) * np.sin(45 * xi) +
                           self.chaotic_params[9] * np.sin(47 * xi) * np.cos(27 * xi) * np.sin(49 * xi) +
                           self.chaotic_params[10] * np.sin(51 * xi) * np.cos(29 * xi) * np.sin(53 * xi) +
                           self.chaotic_params[11] * np.sin(55 * xi) * np.cos(31 * xi) * np.sin(57 * xi) +
                           self.chaotic_params[12] * np.sin(59 * xi) * np.cos(33 * xi) * np.sin(61 * xi) +
                           self.chaotic_params[13] * np.sin(63 * xi) * np.cos(35 * xi) * np.sin(65 * xi) +
                           self.chaotic_params[14] * np.sin(67 * xi) * np.cos(37 * xi) * np.sin(69 * xi))
        
        # Logarithmic conditioning term with adaptive scaling
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi) + 0.3 * np.sin(3 * xi)) * self.conditioning_factors[i]
        
        # Cross-dimensional cubic interaction terms with trigonometric coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += self.cross_weights[i, j] * (x[i] ** 3) * x[j] * self.coupling_coeffs[i, j]
        
        # Quadratic basin component with adaptive conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Add a novel hyperbolic tangent component with fractal-like scaling
        tanh_component = 0.0
        for i in range(self.dim):
            tanh_component += np.tanh(x[i]) * np.sin(x[i]) * self.conditioning_factors[i]
        
        # Add self-similarity fractal-like component
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += np.sin(2 * np.pi * x[i]) * np.cos(2 * np.pi * x[i]) * np.sin(4 * np.pi * x[i])
        
        # Combine all components with different weights
        result = 0.25 * gaussian_sum + 0.2 * chaotic_sum + 0.15 * log_conditioning + 0.15 * cross_term + 0.1 * quadratic_term + 0.1 * tanh_component + 0.05 * fractal_component
        
        return result