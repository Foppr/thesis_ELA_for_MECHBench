import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for self-similar structure
        self.fractal_dims = np.linspace(0.3, 0.8, dim)
        self.freq_mod = np.linspace(2.0, 6.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal component with self-similar structure using fractional dimensions
        fractal = 0.0
        for i in range(self.dim):
            # Generate fractal-like pattern with varying dimensionality
            dim_factor = self.fractal_dims[i]
            fractal += np.sin(2 ** (i + 1) * x_norm[i]) * (1 - np.abs(x_norm[i])) ** dim_factor
        
        # Chaotic frequency modulation component
        chaos_freq = 0.0
        for i in range(self.dim):
            freq = self.freq_mod[i]
            # Apply chaotic modulation to frequency
            mod = np.sin(freq * x_norm[i]) + 0.5 * np.cos(2 * freq * x_norm[i])
            chaos_freq += mod * np.exp(-0.1 * x_norm[i]**2)
        
        # Adaptive ridge structure with varying curvature
        ridges = 0.0
        for i in range(self.dim):
            # Create adaptive ridge with different curvature per dimension
            curvature = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            ridges += (x_norm[i] ** 2) * np.exp(-curvature * x_norm[i]**2)
        
        # Multi-scale sinusoidal interference with varying amplitudes
        multi_scale = 0.0
        scales = [1, 2, 4, 8]
        for scale in scales:
            if scale <= self.dim:
                multi_scale += np.sum(np.sin(scale * np.pi * x_norm[:scale]) * 
                                    np.cos(scale * np.pi * x_norm[:scale]))
        
        # Asymmetric Gaussian mixture with varying means and variances
        gaussian_mixture = 0.0
        for i in range(self.dim):
            mean = 0.3 * np.sin(i)
            variance = 0.2 + 0.1 * np.cos(i)
            gaussian_mixture += np.exp(-0.5 * ((x_norm[i] - mean) ** 2) / variance)
        
        # Combine all components with optimized weights
        return 0.25 * fractal + 0.3 * chaos_freq + 0.15 * ridges + 0.2 * multi_scale + 0.1 * gaussian_mixture + 1.5