import numpy as np

class AdaptiveRidgeGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Ridge adaptation parameters for dynamic conditioning
        self.ridge_strengths = np.random.uniform(0.5, 2.5, min(10, dim)) * 1.2
        self.ridge_widths = np.logspace(0.3, 1.8, min(8, dim)) * 0.8
        # Gaussian mixing parameters with dynamic variances
        self.gaussian_centers = np.random.uniform(-3.0, 3.0, (min(6, dim), dim))
        self.gaussian_vars = np.logspace(0.1, 1.5, min(6, dim)) * 0.6
        # Resonance coupling parameters for cross-dimensional effects
        self.resonance_freqs = np.random.uniform(0.8, 3.2, min(7, dim)) * 1.1
        self.resonance_amplitudes = np.random.uniform(0.3, 1.7, min(7, dim)) * 0.9
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Adaptive ridge terms with varying strength and width
        ridge_term = 0.0
        for i in range(min(len(self.ridge_strengths), self.dim)):
            strength = self.ridge_strengths[i]
            width = self.ridge_widths[i]
            # Ridge with Gaussian-like shape and dynamic curvature
            ridge_val = strength * np.exp(-0.5 * (x_norm[i] / width) ** 2) + 0.3 * (x_norm[i] ** 4)
            ridge_term += ridge_val
            
        # Dynamic Gaussian mixture components with varying centers and variances
        gaussian_term = 0.0
        for i in range(min(len(self.gaussian_centers), 6)):
            center = self.gaussian_centers[i]
            var = self.gaussian_vars[i]
            # Multivariate Gaussian with dynamic scaling
            diff = x_norm - center
            gauss_val = np.exp(-0.5 * np.sum((diff ** 2) / var))
            gaussian_term += gauss_val
            
        # Cross-dimensional resonance effects with frequency modulation
        resonance_term = 0.0
        for i in range(self.dim):
            freq = self.resonance_freqs[i % len(self.resonance_freqs)]
            amp = self.resonance_amplitudes[i % len(self.resonance_amplitudes)]
            # Resonant interaction between dimensions with phase shifts
            resonance_val = amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[(i + 1) % self.dim])
            resonance_term += resonance_val
            
        # Additional multimodal structure with polynomial modulations
        poly_term = 0.0
        for i in range(self.dim):
            # Polynomial terms that create complex valley structures
            poly_val = 0.4 * (x_norm[i] ** 3) + 0.2 * (x_norm[i] ** 5) + 0.1 * (x_norm[i] ** 7)
            poly_term += poly_val
            
        # Combined terms with dynamic weights based on dimensionality
        dim_factor = 1.0 + 0.05 * self.dim
        result = 0.8 * ridge_term + 0.6 * gaussian_term + 0.5 * resonance_term + 0.4 * poly_term
        
        # Add adaptive noise with dimensionality-dependent amplitude
        noise_amplitude = 0.03 * dim_factor
        noise = noise_amplitude * np.random.randn()
        
        return result + noise