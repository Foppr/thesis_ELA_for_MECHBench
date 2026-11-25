import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize Gaussian mixture parameters
        self.n_gaussians = 7
        self.gaussian_centers = np.random.uniform(-4.9, 4.9, (self.n_gaussians, dim))
        self.gaussian_weights = np.random.uniform(0.1, 2.5, self.n_gaussians)
        self.gaussian_std = np.random.uniform(0.1, 2.0, (self.n_gaussians, dim))
        # Trigonometric wave parameters with chaotic modulation
        self.wave_freq = np.random.uniform(0.3, 8.0, dim)
        self.wave_amp = np.random.uniform(0.2, 3.5, dim)
        self.wave_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-1.2, 1.2, (dim, 6))
        # Adaptive gradient modulation parameters with chaotic tent map
        self.adaptive_scale = np.random.uniform(0.01, 1.2, dim)
        self.adaptive_freq = np.random.uniform(0.1, 3.5, dim)
        # Interaction strength between dimensions with time-varying coupling
        self.interaction_strength = np.random.uniform(0.03, 2.0, (dim, dim))
        # Fractal-like self-similarity parameters with hyper-chaotic scaling
        self.fractal_coeffs = np.random.uniform(0.03, 0.8, dim)
        # Memory-dependent evolutionary terms with chaotic feedback
        self.memory_weights = np.random.uniform(-0.5, 0.5, dim)
        # Hyper-chaotic sine wave interference patterns
        self.hyper_wave_freq = np.random.uniform(0.8, 12.0, dim)
        self.hyper_wave_amp = np.random.uniform(0.05, 1.8, dim)
        self.hyper_wave_phase = np.random.uniform(0.0, 3*np.pi, dim)
        
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
            for d in range(6):
                poly_sum += self.poly_coeffs[i][d] * (x[i] ** d)
            result += poly_sum
            
        # Cross-dimensional interaction terms with adaptive modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = self.interaction_strength[i][j] * np.sin(x[i]) * np.cos(x[j])
                result += interaction
                
        # Adaptive gradient modulation with chaotic tent map influence
        for i in range(self.dim):
            mod_term = self.adaptive_scale[i] * np.sin(self.adaptive_freq[i] * x[i]) * np.cos(x[i]**2)
            result += mod_term
            
        # Fractal-like self-similarity enhancement
        for i in range(self.dim):
            fractal_term = self.fractal_coeffs[i] * np.sin(x[i] ** 3) * np.cos(x[i])
            result += fractal_term
            
        # Memory-dependent evolutionary terms with chaotic feedback
        for i in range(self.dim):
            memory_term = self.memory_weights[i] * np.sin(x[i]) * np.exp(-x[i]**2)
            result += memory_term
            
        # Hyper-chaotic sine wave interference patterns
        for i in range(self.dim):
            hyper_term = self.hyper_wave_amp[i] * np.sin(self.hyper_wave_freq[i] * x[i] + self.hyper_wave_phase[i]) * np.cos(x[i]**3)
            result += hyper_term
            
        # Add a global scaling factor based on the sum of all coordinates with chaotic modulation
        chaotic_factor = 1.0 + 0.4 * np.sum(np.abs(x)) * np.sin(np.sum(x) * 0.6)
        result *= chaotic_factor
        
        return result