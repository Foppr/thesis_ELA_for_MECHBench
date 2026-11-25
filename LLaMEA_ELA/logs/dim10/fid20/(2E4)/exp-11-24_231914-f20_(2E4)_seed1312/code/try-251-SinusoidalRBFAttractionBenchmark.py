import numpy as np

class SinusoidalRBFAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Sinusoidal components with varying frequencies and amplitudes
        self.sin_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.sin_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.sin_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Radial Basis Functions with centers, widths, and weights
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(10, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=10)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=10)
        # Gradient-based attraction fields with varying strengths and directions
        self.attraction_centers = np.random.uniform(-4.0, 4.0, size=(5, dim))
        self.attraction_strengths = np.random.uniform(1.0, 5.0, size=5)
        self.attraction_directions = np.random.rand(5, dim) - 0.5
        self.attraction_directions = self.attraction_directions / np.linalg.norm(self.attraction_directions, axis=1, keepdims=True)
        # Additional noise and scaling parameters
        self.noise_level = np.random.uniform(0.1, 1.0, size=dim)
        self.scaling_factors = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal component
        sin_component = 0.0
        for i in range(self.dim):
            sin_val = self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
            sin_component += sin_val
            
        # Radial Basis Function component
        rbf_component = 0.0
        for i in range(10):
            dist_sq = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_val = self.rbf_weights[i] * np.exp(-dist_sq / (2 * self.rbf_widths[i]**2))
            rbf_component += rbf_val
            
        # Gradient-based attraction component
        attr_component = 0.0
        for i in range(5):
            dist_vec = x - self.attraction_centers[i]
            dist = np.linalg.norm(dist_vec)
            if dist > 1e-8:
                direction = dist_vec / dist
                proj = np.dot(direction, self.attraction_directions[i])
                attr_val = self.attraction_strengths[i] * (1.0 - np.exp(-dist)) * proj
                attr_component += attr_val
                
        # Add noise and scaling
        noise = np.random.normal(0, 1, size=self.dim)
        scaled_noise = np.sum(self.noise_level * noise * self.scaling_factors)
        
        # Combine all components with weighted sum
        return (1.2 * sin_component + 
                1.5 * rbf_component + 
                1.3 * attr_component + 
                0.8 * scaled_noise)