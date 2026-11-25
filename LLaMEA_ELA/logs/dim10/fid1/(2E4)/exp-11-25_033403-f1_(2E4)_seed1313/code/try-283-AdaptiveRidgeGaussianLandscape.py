import numpy as np

class AdaptiveRidgeGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize Gaussian mixture components
        self.n_components = 7
        self.gauss_means = np.random.uniform(-4.0, 4.0, (self.n_components, dim))
        self.gauss_stds = np.random.uniform(0.3, 1.5, (self.n_components, dim))
        self.gauss_weights = np.random.uniform(0.3, 1.8, self.n_components)
        # Initialize enhanced sinusoidal modulation parameters
        self.sin_freqs = np.random.uniform(1.5, 5.0, dim)
        self.sin_amplitudes = np.random.uniform(0.3, 2.0, dim)
        # Initialize ridge structure parameters
        self.ridge_centers = np.random.uniform(-4.0, 4.0, (5, dim))
        self.ridge_widths = np.random.uniform(0.3, 1.7, 5)
        self.ridge_heights = np.random.uniform(0.9, 2.8, 5)
        # Initialize adaptive scaling
        self.adaptive_scale = np.random.uniform(0.4, 2.0, dim)
        # Add enhanced fractal-like components for better complexity
        self.fractal_freqs = np.random.uniform(0.8, 2.5, dim)
        self.fractal_amplitudes = np.random.uniform(0.15, 1.0, dim)
        # Add additional chaotic modulation for improved landscape diversity
        self.chaos_freqs = np.random.uniform(3.0, 7.0, dim)
        self.chaos_amplitudes = np.random.uniform(0.2, 0.8, dim)
        # Add polynomial interaction terms for increased complexity
        self.poly_coeffs = np.random.uniform(-0.5, 0.5, (3, dim))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute Gaussian mixture potential
        gaussian_potential = 0.0
        for i in range(self.n_components):
            gauss_val = 0.0
            for j in range(self.dim):
                gauss_val += ((x[j] - self.gauss_means[i, j]) / self.gauss_stds[i, j])**2
            gaussian_potential += self.gauss_weights[i] * np.exp(-0.5 * gauss_val)
        
        # Add enhanced sinusoidal modulation
        sin_modulation = 0.0
        for j in range(self.dim):
            sin_modulation += self.sin_amplitudes[j] * np.sin(self.sin_freqs[j] * x[j])
        
        # Add ridge structure contributions
        ridge_potential = 0.0
        for i in range(5):
            ridge_dist = 0.0
            for j in range(self.dim):
                ridge_dist += ((x[j] - self.ridge_centers[i, j]) / self.ridge_widths[i])**2
            ridge_val = np.exp(-0.5 * ridge_dist)
            ridge_potential += self.ridge_heights[i] * ridge_val
        
        # Add adaptive scaling terms
        scale_terms = 0.0
        for j in range(self.dim):
            scale_terms += self.adaptive_scale[j] * x[j]**2
            
        # Add fractal-like components for enhanced landscape complexity
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_amplitudes[j] * np.sin(self.fractal_freqs[j] * x[j]) * np.cos(self.fractal_freqs[j] * x[j])
        
        # Add chaotic modulation for improved landscape diversity
        chaos_terms = 0.0
        for j in range(self.dim):
            chaos_terms += self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j]) * np.tan(self.chaos_freqs[j] * x[j])
        
        # Add polynomial interaction terms
        poly_terms = 0.0
        for i in range(3):
            for j in range(self.dim):
                poly_terms += self.poly_coeffs[i, j] * x[j]**(i+1)
        
        # Combine all components with optimized weights
        total = -gaussian_potential + sin_modulation + ridge_potential + 0.15 * scale_terms + 0.08 * fractal_terms + 0.05 * chaos_terms + 0.02 * poly_terms
        
        return total