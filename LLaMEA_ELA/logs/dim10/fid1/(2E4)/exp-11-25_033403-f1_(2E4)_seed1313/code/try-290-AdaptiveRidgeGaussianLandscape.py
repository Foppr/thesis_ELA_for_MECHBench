import numpy as np

class AdaptiveRidgeGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize Gaussian mixture components
        self.n_components = 10
        self.gauss_means = np.random.uniform(-4.0, 4.0, (self.n_components, dim))
        self.gauss_stds = np.random.uniform(0.2, 1.5, (self.n_components, dim))
        self.gauss_weights = np.random.uniform(0.3, 2.5, self.n_components)
        # Initialize sinusoidal modulation parameters
        self.sin_freqs = np.random.uniform(2.0, 6.0, dim)
        self.sin_amplitudes = np.random.uniform(0.4, 2.5, dim)
        # Initialize ridge structure parameters with shifts
        self.ridge_centers = np.random.uniform(-4.0, 4.0, (8, dim)) + 0.3 * np.random.randn(8, dim)
        self.ridge_widths = np.random.uniform(0.2, 2.5, 8)
        self.ridge_heights = np.random.uniform(0.4, 3.5, 8)
        # Initialize adaptive scaling
        self.adaptive_scale = np.random.uniform(0.1, 2.5, dim)
        # Add fractal-like components for enhanced complexity
        self.fractal_freqs = np.random.uniform(0.2, 3.0, dim)
        self.fractal_amplitudes = np.random.uniform(0.03, 1.2, dim)
        # Additional hyperparameters to improve landscape characteristics
        self.hyper_weights = np.random.uniform(0.5, 3.0, 5)
        
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
        for i in range(8):
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
        
        # Add additional polynomial terms to increase gradient complexity
        poly_terms = 0.0
        for j in range(self.dim):
            poly_terms += (x[j]**4 + x[j]**2) * self.hyper_weights[j % 5]
        
        # Combine all components with modified weights
        total = -gaussian_potential + 1.8 * sin_modulation + ridge_potential + 0.3 * scale_terms + 0.15 * fractal_terms + 0.05 * poly_terms
        
        return total