import numpy as np

class ChaoticHyperEllipsoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize Gaussian mixture components with chaotic positioning
        self.n_components = 15
        self.gauss_means = np.random.uniform(-4.0, 4.0, (self.n_components, dim))
        # Add chaotic perturbations to means
        for i in range(self.n_components):
            for j in range(dim):
                self.gauss_means[i, j] += 0.5 * np.sin(13.0 * i * j + 2.0 * np.pi * np.random.rand())
        self.gauss_stds = np.random.uniform(0.1, 2.0, (self.n_components, dim))
        self.gauss_weights = np.random.uniform(0.2, 3.0, self.n_components)
        # Initialize chaotic sinusoidal modulation parameters
        self.sin_freqs = np.random.uniform(1.5, 8.0, dim)
        self.sin_amplitudes = np.random.uniform(0.3, 3.0, dim)
        # Add chaotic frequency modulations
        for j in range(dim):
            self.sin_freqs[j] += 0.8 * np.cos(7.0 * j + 3.0 * np.pi * np.random.rand())
        # Initialize hyper-ellipsoidal ridge structures with dynamic scaling
        self.ridge_centers = np.random.uniform(-4.0, 4.0, (12, dim)) + 0.5 * np.random.randn(12, dim)
        self.ridge_widths = np.random.uniform(0.1, 3.0, 12)
        self.ridge_heights = np.random.uniform(0.3, 4.0, 12)
        # Add dynamic scaling with chaotic components
        self.adaptive_scale = np.random.uniform(0.05, 3.0, dim)
        for j in range(dim):
            self.adaptive_scale[j] += 0.6 * np.sin(9.0 * j + 4.0 * np.pi * np.random.rand())
        # Add fractal-like components with chaotic frequencies
        self.fractal_freqs = np.random.uniform(0.1, 4.0, dim)
        for j in range(dim):
            self.fractal_freqs[j] += 0.9 * np.cos(5.0 * j + 2.0 * np.pi * np.random.rand())
        self.fractal_amplitudes = np.random.uniform(0.02, 1.5, dim)
        # Add hyper-ellipsoidal interaction terms
        self.ellipse_coeffs = np.random.uniform(0.5, 2.5, (6, dim))
        self.ellipse_weights = np.random.uniform(0.4, 3.5, 6)
        # Add dynamic coupling coefficients
        self.coupling_coeffs = np.random.uniform(-0.8, 0.8, (dim, dim))
        for i in range(dim):
            self.coupling_coeffs[i, i] = 0.0
        # Additional hyperparameters for enhanced complexity
        self.hyper_weights = np.random.uniform(0.3, 4.0, 7)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute Gaussian mixture potential with chaotic interactions
        gaussian_potential = 0.0
        for i in range(self.n_components):
            gauss_val = 0.0
            for j in range(self.dim):
                gauss_val += ((x[j] - self.gauss_means[i, j]) / self.gauss_stds[i, j])**2
            gaussian_potential += self.gauss_weights[i] * np.exp(-0.5 * gauss_val)
        
        # Add chaotic sinusoidal modulation
        sin_modulation = 0.0
        for j in range(self.dim):
            sin_modulation += self.sin_amplitudes[j] * np.sin(self.sin_freqs[j] * x[j])
        
        # Add hyper-ellipsoidal ridge structure contributions
        ridge_potential = 0.0
        for i in range(12):
            ridge_dist = 0.0
            for j in range(self.dim):
                ridge_dist += ((x[j] - self.ridge_centers[i, j]) / self.ridge_widths[i])**2
            ridge_val = np.exp(-0.5 * ridge_dist)
            ridge_potential += self.ridge_heights[i] * ridge_val
        
        # Add adaptive scaling terms with chaotic nonlinear interaction
        scale_terms = 0.0
        for j in range(self.dim):
            scale_terms += self.adaptive_scale[j] * x[j]**3
            
        # Add fractal-like components with chaotic frequency variations
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_amplitudes[j] * np.sin(self.fractal_freqs[j] * x[j]) * np.cos(self.fractal_freqs[j] * x[j])
        
        # Add hyper-ellipsoidal interaction terms with dynamic coupling
        ellipse_terms = 0.0
        for i in range(6):
            ell_val = 0.0
            for j in range(self.dim):
                ell_val += (x[j] - self.ellipse_coeffs[i, j])**2
            ellipse_terms += self.ellipse_weights[i] * np.exp(-0.5 * ell_val)
            
        # Add dynamic coupling terms between dimensions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_coeffs[i, j] * x[i] * x[j]
        
        # Add additional high-order polynomial terms to increase gradient complexity
        poly_terms = 0.0
        for j in range(self.dim):
            poly_terms += (x[j]**5 + x[j]**3 + x[j]**2) * self.hyper_weights[j % 7]
        
        # Combine all components with modified weights for enhanced difficulty
        total = -gaussian_potential + 2.0 * sin_modulation + ridge_potential + 0.4 * scale_terms + 0.2 * fractal_terms + 0.1 * ellipse_terms + 0.15 * coupling_terms + 0.08 * poly_terms
        
        return total