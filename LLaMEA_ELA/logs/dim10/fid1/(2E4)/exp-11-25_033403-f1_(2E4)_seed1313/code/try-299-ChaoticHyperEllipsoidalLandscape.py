import numpy as np

class ChaoticHyperEllipsoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced Gaussian mixture components with chaotic distributions
        self.n_components = 15
        self.gauss_means = np.random.uniform(-4.5, 4.5, (self.n_components, dim))
        self.gauss_stds = np.random.uniform(0.1, 2.0, (self.n_components, dim))
        self.gauss_weights = np.random.uniform(0.2, 3.0, self.n_components)
        # Chaotic sine-wave modulation parameters with fractal frequency patterns
        self.sin_freqs = np.random.uniform(1.0, 8.0, dim) * (1.0 + 0.5 * np.sin(np.arange(dim) * 0.7))
        self.sin_amplitudes = np.random.uniform(0.3, 3.0, dim)
        # Dynamic hyper-ellipsoidal structures with time-varying parameters
        self.ellipse_centers = np.random.uniform(-4.0, 4.0, (10, dim)) + 0.5 * np.random.randn(10, dim)
        self.ellipse_axes = np.random.uniform(0.3, 3.0, (10, dim))
        self.ellipse_weights = np.random.uniform(0.5, 4.0, 10)
        # Momentum-based gradient steering parameters
        self.momentum_coeffs = np.random.uniform(0.05, 0.3, dim)
        self.gradient_shifts = np.random.uniform(-0.2, 0.2, dim)
        # Fractal-like components with multi-scale complexity
        self.fractal_freqs = np.random.uniform(0.1, 4.0, dim) * (1.0 + 0.3 * np.cos(np.arange(dim) * 0.5))
        self.fractal_amplitudes = np.random.uniform(0.02, 1.5, dim)
        # Additional hyperparameters for enhanced landscape characteristics
        self.hyper_weights = np.random.uniform(0.4, 4.0, 7)
        self.deception_params = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute enhanced Gaussian mixture potential with chaotic weights
        gaussian_potential = 0.0
        for i in range(self.n_components):
            gauss_val = 0.0
            for j in range(self.dim):
                gauss_val += ((x[j] - self.gauss_means[i, j]) / self.gauss_stds[i, j])**2
            gaussian_potential += self.gauss_weights[i] * np.exp(-0.5 * gauss_val)
        
        # Add chaotic sine-wave modulation with fractal frequency components
        sin_modulation = 0.0
        for j in range(self.dim):
            sin_modulation += self.sin_amplitudes[j] * np.sin(self.sin_freqs[j] * x[j] + 
                                                              self.fractal_freqs[j] * np.cos(x[j]))
        
        # Add dynamic hyper-ellipsoidal structure contributions
        ellipse_potential = 0.0
        for i in range(10):
            ell_dist = 0.0
            for j in range(self.dim):
                ell_dist += ((x[j] - self.ellipse_centers[i, j]) / self.ellipse_axes[i, j])**2
            ellipse_val = np.exp(-0.5 * ell_dist)
            ellipse_potential += self.ellipse_weights[i] * ellipse_val
        
        # Add momentum-based gradient steering terms
        momentum_terms = 0.0
        for j in range(self.dim):
            momentum_terms += self.momentum_coeffs[j] * (x[j] - self.gradient_shifts[j])**3
            
        # Add fractal-like components with multi-scale interactions
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_amplitudes[j] * np.sin(self.fractal_freqs[j] * x[j]) * \
                            np.cos(self.fractal_freqs[j] * x[j] * 0.5) * \
                            np.sin(x[j]**2 * 0.1)
        
        # Add additional polynomial and interaction terms for increased gradient complexity
        poly_terms = 0.0
        for j in range(self.dim):
            poly_terms += (x[j]**5 + x[j]**3 + x[j]**2) * self.hyper_weights[j % 7]
            
        # Add deception terms to create misleading optima
        deception_terms = 0.0
        for j in range(self.dim):
            deception_terms += self.deception_params[j] * np.sin(x[j] * 2.0) * np.cos(x[j] * 0.5)
        
        # Combine all components with modified weights and enhanced interaction
        total = -gaussian_potential + 2.0 * sin_modulation + ellipse_potential + \
                0.4 * momentum_terms + 0.2 * fractal_terms + 0.1 * poly_terms + 0.15 * deception_terms
        
        return total