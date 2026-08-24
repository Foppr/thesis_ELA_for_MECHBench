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
        self.radial_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.radial_widths = np.random.uniform(0.5, 2.0, 10)
        self.radial_amplitudes = np.random.uniform(1.0, 3.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add chaotic radial basis functions with varying centers, widths, and amplitudes
        for i in range(10):
            center = self.radial_centers[i]
            width = self.radial_widths[i]
            amplitude = self.radial_amplitudes[i]
            # Radial basis function with chaotic modulation
            rbf = amplitude * np.exp(-width * np.sum((x_transformed - center)**2))
            f_val += rbf * (1.0 + 0.3 * np.sin(4.0 * np.sum((x_transformed - center)**2)))
            
        # Add cross-dimensional resonance terms with chaotic coupling
        for i in range(self.dim - 2):
            # Resonance term with chaotic phase modulation
            phase = np.sin(2.0 * x_transformed[i]) + 0.5 * np.sin(3.0 * x_transformed[i+1])
            resonance = x_transformed[i] * x_transformed[i+1] * x_transformed[i+2] * phase
            f_val += 1.5 * resonance * (1.0 + 0.2 * np.cos(5.0 * x_transformed[i]))
            
        # Add a perturbed quartic term with chaotic modulation for increased complexity
        f_val += 0.1 * np.sum((x_transformed**4) * (1.0 + 0.3 * np.sin(6.0 * x_transformed)))
        
        # Add stochastic noise with adaptive variance and frequency
        noise = np.random.normal(0, self.noise_scale, self.dim)
        # Introduce frequency-dependent noise for increased ruggedness
        freq_noise = np.sin(self.noise_frequency * x_transformed) * noise
        f_val += np.sum(freq_noise * x_transformed)
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.2
        
        return f_val