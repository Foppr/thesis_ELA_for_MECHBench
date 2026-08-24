import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        # Additional random scaling for each dimension
        self.scales = np.random.uniform(0.5, 2.0, dim)
        # Adaptive noise parameters
        self.noise_scale = 1.2
        self.noise_frequency = 5.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add exponential chaotic sine-wave perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 8.0 * np.exp(-0.5 * x_transformed[i]**2) * np.sin(7.0 * x_transformed[i] + 2.0 * np.sin(4.0 * x_transformed[i])) * \
                     np.cos(5.0 * x_transformed[i] + 1.5 * np.cos(3.0 * x_transformed[i])) + \
                     3.0 * np.exp(-0.3 * x_transformed[i]**2) * np.sin(8.0 * x_transformed[i] + 1.0 * np.sin(5.0 * x_transformed[i]))
            
        # Add complex interaction terms between dimensions with higher-order and chaotic coupling
        for i in range(self.dim - 4):
            f_val += 2.0 * x_transformed[i] * x_transformed[i+1] * x_transformed[i+2] * x_transformed[i+3] * x_transformed[i+4] * \
                     (np.sin(0.8 * x_transformed[i] + 0.5 * np.sin(2.5 * x_transformed[i])) + 
                      np.cos(0.9 * x_transformed[i+1] + 0.6 * np.cos(2.0 * x_transformed[i+1])) + 
                      np.sin(1.0 * x_transformed[i+2] + 0.4 * np.sin(3.5 * x_transformed[i+2])) +
                      np.cos(0.7 * x_transformed[i+3] + 0.3 * np.cos(4.0 * x_transformed[i+3])) +
                      np.sin(0.6 * x_transformed[i+4] + 0.2 * np.sin(5.0 * x_transformed[i+4])))
            
        # Add a perturbed quartic term with chaotic modulation for increased complexity
        f_val += 0.12 * np.sum((x_transformed**4) * (1.0 + 0.5 * np.sin(8.0 * x_transformed) + 0.3 * np.cos(6.0 * x_transformed)))
        
        # Add stochastic noise with adaptive variance and frequency
        noise = np.random.normal(0, self.noise_scale, self.dim)
        # Introduce frequency-dependent noise for increased ruggedness
        freq_noise = np.sin(self.noise_frequency * x_transformed) * noise
        f_val += np.sum(freq_noise * x_transformed)
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.15
        
        return f_val