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
        self.noise_scale = 0.6
        self.noise_frequency = 3.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add highly oscillatory sinusoidal perturbations with varying frequencies
        for i in range(self.dim):
            f_val += 4.0 * np.sin(5.0 * x_transformed[i]) * np.cos(4.0 * x_transformed[i]) + \
                     3.0 * np.sin(7.0 * x_transformed[i]) * np.cos(6.0 * x_transformed[i]) + \
                     2.0 * np.sin(9.0 * x_transformed[i]) * np.cos(8.0 * x_transformed[i])
            
        # Add complex interaction terms between dimensions with higher-order terms
        for i in range(self.dim - 2):
            f_val += 0.8 * x_transformed[i] * x_transformed[i+1] * x_transformed[i+2] * \
                     (np.sin(0.5 * x_transformed[i]) + np.cos(0.6 * x_transformed[i+1]) + np.sin(0.7 * x_transformed[i+2]))
            
        # Add a quintic and sextic term for additional complexity with varying coefficients
        f_val += 0.05 * np.sum(x_transformed**5) + 0.02 * np.sum(x_transformed**6)
        
        # Add stochastic noise with adaptive variance and frequency
        noise = np.random.normal(0, self.noise_scale, self.dim)
        # Introduce frequency-dependent noise for increased ruggedness
        freq_noise = np.sin(self.noise_frequency * x_transformed) * noise
        f_val += np.sum(freq_noise * x_transformed)
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.1
        
        return f_val