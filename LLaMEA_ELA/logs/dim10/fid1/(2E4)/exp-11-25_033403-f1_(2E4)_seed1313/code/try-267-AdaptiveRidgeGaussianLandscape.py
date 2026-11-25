import numpy as np

class AdaptiveRidgeGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize Gaussian mixture components
        self.n_components = 5
        self.gauss_means = np.random.uniform(-4.0, 4.0, (self.n_components, dim))
        self.gauss_stds = np.random.uniform(0.5, 2.0, (self.n_components, dim))
        self.gauss_weights = np.random.uniform(0.5, 2.0, self.n_components)
        # Initialize sinusoidal modulation parameters
        self.sin_freqs = np.random.uniform(0.5, 3.0, dim)
        self.sin_amplitudes = np.random.uniform(0.1, 1.0, dim)
        # Initialize ridge structure parameters
        self.ridge_centers = np.random.uniform(-4.0, 4.0, (3, dim))
        self.ridge_widths = np.random.uniform(0.5, 2.0, 3)
        self.ridge_heights = np.random.uniform(1.0, 3.0, 3)
        # Initialize adaptive scaling
        self.adaptive_scale = np.random.uniform(0.5, 2.0, dim)
        
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
        for i in range(3):
            ridge_dist = 0.0
            for j in range(self.dim):
                ridge_dist += ((x[j] - self.ridge_centers[i, j]) / self.ridge_widths[i])**2
            ridge_val = np.exp(-0.5 * ridge_dist)
            ridge_potential += self.ridge_heights[i] * ridge_val
        
        # Add adaptive scaling terms
        scale_terms = 0.0
        for j in range(self.dim):
            scale_terms += self.adaptive_scale[j] * x[j]**2
            
        # Combine all components
        total = -gaussian_potential + sin_modulation + ridge_potential + 0.1 * scale_terms
        
        return total