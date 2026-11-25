import numpy as np

class AdaptiveWaveGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize Gaussian mixture parameters
        self.n_gaussians = 5
        self.gaussian_centers = np.random.uniform(-4.0, 4.0, (self.n_gaussians, dim))
        self.gaussian_weights = np.random.uniform(0.5, 2.0, self.n_gaussians)
        self.gaussian_std = np.random.uniform(0.5, 2.0, (self.n_gaussians, dim))
        # Trigonometric wave parameters
        self.wave_freq = np.random.uniform(1.0, 8.0, dim)
        self.wave_amp = np.random.uniform(0.5, 3.0, dim)
        self.wave_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        # Adaptive gradient modulation parameters
        self.adaptive_scale = np.random.uniform(0.1, 1.0, dim)
        self.adaptive_freq = np.random.uniform(0.5, 3.0, dim)
        # Interaction strength between dimensions
        self.interaction_strength = np.random.uniform(0.2, 1.5, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Gaussian mixture components
        for i in range(self.n_gaussians):
            gaussian_sum = 0.0
            for j in range(self.dim):
                gaussian_sum += ((x[j] - self.gaussian_centers[i][j]) ** 2) / (2 * self.gaussian_std[i][j] ** 2)
            result += self.gaussian_weights[i] * np.exp(-gaussian_sum)
        
        # Trigonometric wave interference patterns
        for i in range(self.dim):
            wave_term = self.wave_amp[i] * np.sin(self.wave_freq[i] * x[i] + self.wave_phase[i])
            result += wave_term
        
        # Polynomial chaos expansion terms
        for i in range(self.dim):
            poly_sum = 0.0
            for d in range(4):
                poly_sum += self.poly_coeffs[i][d] * (x[i] ** d)
            result += poly_sum
            
        # Cross-dimensional interaction terms with adaptive modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = self.interaction_strength[i][j] * np.sin(x[i]) * np.cos(x[j])
                result += interaction
                
        # Adaptive gradient modulation
        for i in range(self.dim):
            mod_term = self.adaptive_scale[i] * np.sin(self.adaptive_freq[i] * x[i]) * np.cos(x[i]**2)
            result += mod_term
            
        # Add a global scaling factor based on the sum of all coordinates
        result *= (1.0 + 0.2 * np.sum(np.abs(x)))
        
        return result