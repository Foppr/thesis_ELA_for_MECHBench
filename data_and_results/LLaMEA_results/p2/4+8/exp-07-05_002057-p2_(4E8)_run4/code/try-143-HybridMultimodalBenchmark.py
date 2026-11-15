import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.weights = np.random.uniform(0.5, 3.0, 20)
        # Additional cross-dimensional interaction terms with quantic coupling
        self.cross_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Additional chaotic modulation parameters with dynamic frequencies
        self.chaotic_params = np.random.uniform(0.1, 3.0, 15)
        # Adaptive basin parameters
        self.basin_weights = np.random.uniform(0.1, 0.5, dim)
        # Quantic polynomial coupling coefficients
        self.poly_coupling = np.random.uniform(-0.3, 0.3, (dim, dim, dim))
    
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
        
        # Enhanced chaotic sinusoidal perturbation component with dynamic frequencies and adaptive modulation
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Dynamic frequency modulation with adaptive amplitudes
            chaotic_sum += (self.chaotic_params[0] * np.sin(11 * xi) * np.cos(7 * xi) * np.sin(13 * xi) * np.cos(9 * xi) + 
                           self.chaotic_params[1] * np.sin(17 * xi) * np.cos(13 * xi) * np.sin(19 * xi) * np.cos(15 * xi) + 
                           self.chaotic_params[2] * np.sin(23 * xi) * np.cos(19 * xi) * np.sin(25 * xi) * np.cos(21 * xi) +
                           self.chaotic_params[3] * np.sin(29 * xi) * np.cos(25 * xi) * np.sin(31 * xi) * np.cos(27 * xi) +
                           self.chaotic_params[4] * np.sin(37 * xi) * np.cos(33 * xi) * np.sin(39 * xi) * np.cos(35 * xi) +
                           self.chaotic_params[5] * np.sin(43 * xi) * np.cos(39 * xi) * np.sin(45 * xi) * np.cos(41 * xi) +
                           self.chaotic_params[6] * np.sin(49 * xi) * np.cos(45 * xi) * np.sin(51 * xi) * np.cos(47 * xi) +
                           self.chaotic_params[7] * np.sin(55 * xi) * np.cos(51 * xi) * np.sin(57 * xi) * np.cos(53 * xi) +
                           self.chaotic_params[8] * np.sin(61 * xi) * np.cos(57 * xi) * np.sin(63 * xi) * np.cos(59 * xi) +
                           self.chaotic_params[9] * np.sin(67 * xi) * np.cos(63 * xi) * np.sin(69 * xi) * np.cos(65 * xi) +
                           self.chaotic_params[10] * np.sin(73 * xi) * np.cos(69 * xi) * np.sin(75 * xi) * np.cos(71 * xi) +
                           self.chaotic_params[11] * np.sin(79 * xi) * np.cos(75 * xi) * np.sin(81 * xi) * np.cos(77 * xi) +
                           self.chaotic_params[12] * np.sin(85 * xi) * np.cos(81 * xi) * np.sin(87 * xi) * np.cos(83 * xi) +
                           self.chaotic_params[13] * np.sin(91 * xi) * np.cos(87 * xi) * np.sin(93 * xi) * np.cos(89 * xi) +
                           self.chaotic_params[14] * np.sin(97 * xi) * np.cos(93 * xi) * np.sin(99 * xi) * np.cos(95 * xi))
        
        # Logarithmic conditioning term with additional sine modulation and adaptive scaling
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi) + 0.3 * np.sin(3 * xi) + 
                                                        0.1 * np.sin(5 * xi) + 0.05 * np.sin(7 * xi))
        
        # Cross-dimensional cubic interaction terms with quantic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += self.cross_weights[i, j] * (x[i] ** 3) * x[j]
        
        # Quantic polynomial coupling component
        quantic_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        quantic_term += self.poly_coupling[i, j, k] * x[i] * (x[j] ** 2) * (x[k] ** 3)
        
        # Adaptive basin component with dynamic weights
        adaptive_basin = 0.0
        for i in range(self.dim):
            adaptive_basin += self.basin_weights[i] * (x[i] ** 4) + (x[i] ** 2) / self.dim
        
        # Add a novel hyperbolic tangent component for additional complexity
        tanh_component = 0.0
        for i in range(self.dim):
            tanh_component += np.tanh(x[i]) * np.sin(x[i]) + 0.5 * np.tanh(x[i]**2) * np.cos(x[i]**2)
        
        # Combine all components with different weights
        result = 0.25 * gaussian_sum + 0.2 * chaotic_sum + 0.15 * log_conditioning + 0.15 * cross_term + 0.1 * quantic_term + 0.1 * adaptive_basin + 0.05 * tanh_component
        
        return result