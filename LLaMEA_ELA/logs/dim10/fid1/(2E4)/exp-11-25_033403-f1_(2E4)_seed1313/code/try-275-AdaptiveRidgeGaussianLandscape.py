import numpy as np

class AdaptiveRidgeGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize Gaussian mixture components
        self.n_components = 7
        self.gauss_means = np.random.uniform(-4.0, 4.0, (self.n_components, dim))
        self.gauss_stds = np.random.uniform(0.3, 1.5, (self.n_components, dim))
        self.gauss_weights = np.random.uniform(0.3, 1.8, self.n_components)
        # Initialize sinusoidal modulation parameters
        self.sin_freqs = np.random.uniform(1.0, 4.0, dim)
        self.sin_amplitudes = np.random.uniform(0.2, 1.5, dim)
        # Initialize ridge structure parameters with shifts
        self.ridge_centers = np.random.uniform(-4.0, 4.0, (5, dim)) + 0.5 * np.random.randn(5, dim)
        self.ridge_widths = np.random.uniform(0.4, 1.8, 5)
        self.ridge_heights = np.random.uniform(0.8, 2.5, 5)
        # Initialize adaptive scaling
        self.adaptive_scale = np.random.uniform(0.3, 1.7, dim)
        # Add fractal-like components for enhanced complexity
        self.fractal_freqs = np.random.uniform(0.5, 2.0, dim)
        self.fractal_amplitudes = np.random.uniform(0.1, 0.8, dim)
        
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
        
        # Add sinusoidal modulation
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
        
        # Add adaptive scaling terms with nonlinear interaction
        scale_terms = 0.0
        for j in range(self.dim):
            scale_terms += self.adaptive_scale[j] * x[j]**3
            
        # Add fractal-like components for enhanced landscape complexity
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_amplitudes[j] * np.sin(self.fractal_freqs[j] * x[j]) * np.cos(self.fractal_freqs[j] * x[j])
        
        # Combine all components with modified weights
        total = -gaussian_potential + 1.2 * sin_modulation + ridge_potential + 0.15 * scale_terms + 0.08 * fractal_terms
        
        return total