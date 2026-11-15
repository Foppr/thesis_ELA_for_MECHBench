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
        # Chaotic parameters for radial basis functions
        self.rb_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rb_widths = np.random.uniform(0.5, 2.0, 10)
        # Resonance coupling parameters
        self.resonance_freqs = np.random.uniform(1.0, 5.0, dim)
        self.resonance_ampls = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add chaotic radial basis function components
        for i in range(10):
            center = self.rb_centers[i]
            width = self.rb_widths[i]
            # Radial basis with chaotic modulation
            rbf_val = np.exp(-width * np.sum((x_transformed - center)**2))
            f_val += 2.0 * rbf_val * np.sin(3.0 * np.sum(x_transformed - center) + 1.5 * np.sin(2.0 * np.sum(x_transformed - center)))
            
        # Add cross-dimensional resonance terms
        for i in range(self.dim):
            f_val += self.resonance_ampls[i] * np.sin(self.resonance_freqs[i] * x_transformed[i] + 
                                                       0.5 * np.sin(2.0 * x_transformed[(i+1) % self.dim]))
            
        # Add complex interaction terms with chaotic coupling
        for i in range(self.dim - 2):
            f_val += 1.2 * x_transformed[i] * x_transformed[i+1] * x_transformed[i+2] * \
                     (np.sin(0.8 * x_transformed[i] + 0.3 * np.sin(2.5 * x_transformed[i])) + 
                      np.cos(0.7 * x_transformed[i+1] + 0.4 * np.cos(1.8 * x_transformed[i+1])) + 
                      np.sin(0.9 * x_transformed[i+2] + 0.2 * np.sin(3.2 * x_transformed[i+2])))
            
        # Add a perturbed quartic term with chaotic modulation for increased complexity
        f_val += 0.08 * np.sum((x_transformed**4) * (1.0 + 0.3 * np.sin(6.0 * x_transformed)))
        
        # Add stochastic noise with adaptive variance and frequency
        noise = np.random.normal(0, self.noise_scale, self.dim)
        # Introduce frequency-dependent noise for increased ruggedness
        freq_noise = np.sin(self.noise_frequency * x_transformed) * noise
        f_val += np.sum(freq_noise * x_transformed)
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.1
        
        return f_val