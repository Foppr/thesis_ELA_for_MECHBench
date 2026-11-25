import numpy as np

class AdaptiveRidgeGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced Gaussian mixture with higher variance and more components
        self.n_components = 12
        self.gauss_means = np.random.uniform(-4.5, 4.5, (self.n_components, dim))
        self.gauss_stds = np.random.uniform(0.1, 2.5, (self.n_components, dim))
        self.gauss_weights = np.random.uniform(0.1, 3.0, self.n_components)
        # Multi-scale sinusoidal modulation with harmonic frequencies
        self.sin_freqs = np.random.uniform(2.0, 8.0, dim)
        self.sin_harmonics = np.random.uniform(0.5, 3.0, (dim, 3))
        # Deep adaptive ridge structures with non-linear transformations
        self.ridge_centers = np.random.uniform(-4.5, 4.5, (8, dim)) + 0.5 * np.random.randn(8, dim)
        self.ridge_widths = np.random.uniform(0.2, 3.0, 8)
        self.ridge_heights = np.random.uniform(1.0, 5.0, 8)
        # Enhanced adaptive scaling with polynomial terms
        self.adaptive_scale = np.random.uniform(0.1, 3.0, dim)
        self.poly_orders = np.random.randint(2, 6, dim)
        # Chaotic fractal components with logistic map modulation
        self.fractal_freqs = np.random.uniform(0.5, 4.0, dim)
        self.fractal_amplitudes = np.random.uniform(0.1, 1.5, dim)
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute enhanced Gaussian mixture potential
        gaussian_potential = 0.0
        for i in range(self.n_components):
            gauss_val = 0.0
            for j in range(self.dim):
                gauss_val += ((x[j] - self.gauss_means[i, j]) / self.gauss_stds[i, j])**2
            gaussian_potential += self.gauss_weights[i] * np.exp(-0.5 * gauss_val)
        
        # Add multi-scale sinusoidal modulation with harmonics
        sin_modulation = 0.0
        for j in range(self.dim):
            sin_modulation += self.sin_freqs[j] * np.sin(self.sin_freqs[j] * x[j])
            for h in range(3):
                sin_modulation += self.sin_harmonics[j, h] * np.sin((h+2) * self.sin_freqs[j] * x[j])
        
        # Add deep ridge structure contributions with non-linear transformations
        ridge_potential = 0.0
        for i in range(8):
            ridge_dist = 0.0
            for j in range(self.dim):
                ridge_dist += ((x[j] - self.ridge_centers[i, j]) / self.ridge_widths[i])**2
            ridge_val = np.exp(-0.5 * ridge_dist)
            ridge_potential += self.ridge_heights[i] * ridge_val
        
        # Add enhanced adaptive scaling with polynomial terms
        scale_terms = 0.0
        for j in range(self.dim):
            scale_terms += self.adaptive_scale[j] * (x[j]**self.poly_orders[j])
            
        # Add chaotic fractal components with logistic map modulation
        fractal_terms = 0.0
        for j in range(self.dim):
            logistic_val = 0.5
            for _ in range(5):
                logistic_val = self.logistic_r[j] * logistic_val * (1 - logistic_val)
            fractal_terms += self.fractal_amplitudes[j] * np.sin(self.fractal_freqs[j] * x[j]) * logistic_val
        
        # Combine all components with new weights and nonlinear interactions
        total = -gaussian_potential + 2.0 * sin_modulation + ridge_potential + 0.3 * scale_terms + 0.2 * fractal_terms
        
        return total