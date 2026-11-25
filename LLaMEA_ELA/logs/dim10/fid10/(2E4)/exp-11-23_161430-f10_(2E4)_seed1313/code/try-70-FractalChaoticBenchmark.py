import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters with enhanced diversity
        self.amp = 1.5 + 0.5 * np.sin(np.arange(dim) * 0.3 + np.pi/4)
        self.beta = 0.7 + 0.3 * np.cos(np.arange(dim) * 0.4 + np.pi/3)
        # Fractal Brownian motion parameters with adaptive Hurst
        self.hurst = 0.1 + 0.7 * np.random.rand(dim)
        self.fractal_scale = 2.0 + 1.5 * np.sin(np.arange(dim) * 0.25 + np.pi/6)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with enhanced modulation
        tent_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Tent map with modified dynamics
            if xi < 0.5:
                tent_val = self.amp[i] * xi
            else:
                tent_val = self.amp[i] * (1 - xi)
            # Enhanced chaotic modulation with dimension-dependent frequency
            tent_term += tent_val * np.sin(self.beta[i] * xi + i * 0.15) * np.exp(-0.07 * i**1.3)
        
        # Fractal Brownian motion component with improved noise characteristics
        fbm_term = 0.0
        for i in range(self.dim):
            # Generate fractal noise with better correlation structure
            noise_val = np.random.normal(0, 1) * self.fractal_scale[i]
            # Enhanced positional dependence with periodic components
            fbm_term += noise_val * np.cos(2.5 * np.pi * x[i] * (i + 1) + i * 0.35) * \
                       np.exp(-0.04 * (x[i]**2 + i**1.6))
        
        # Enhanced multi-scale radial basis function component
        rbf_term = 0.0
        scales = np.linspace(0.4, 3.0, min(7, self.dim // 2 + 1))
        for level, scale in enumerate(scales):
            centers = np.linspace(-3.5, 3.5, max(2, self.dim // (level + 1) + 1))
            for i, center in enumerate(centers):
                sigma = scale * (1.0 + 0.4 * np.sin(i * 0.8 + level * 0.6))
                # Enhanced RBF with asymmetric and multi-frequency components
                rbf_term += np.exp(-0.5 * ((x[i % self.dim] - center) / sigma)**2) * \
                           np.sin(2.5 * np.pi * (x[i % self.dim] - center) / sigma + level * 0.5) * \
                           np.cos(1.8 * (x[i % self.dim] - center) / sigma)
        
        # Saddle point structure with improved conditioning
        saddle_term = 0.0
        for i in range(self.dim):
            base = x[i]
            # Enhanced saddle with varying curvature and phase shifts
            saddle_term += (base**5 - 5*base**3 + 4*base) * \
                          np.cos(0.4 * base + i * 0.25) * np.exp(-0.1 * i)
        
        # Cross-dimensional interaction with improved coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 3) % self.dim
            # Enhanced coupling with variable weights and improved interaction terms
            weight = 1.2 + 0.3 * np.sin(i * 0.6 + x[j] * 0.25) * np.cos(x[k] * 0.35)
            cross_term += weight * np.sin(3.5 * x[i] + i * 0.12) * np.cos(2.5 * x[j] + j * 0.18) * \
                         np.tanh(0.9 * (x[k] - x[i])) * \
                         np.exp(-0.09 * (x[i]**2 + x[j]**2))
        
        # Combine all components with adjusted weights for better balance
        result = 0.35 * np.sum(x**2) + 0.25 * tent_term + 0.18 * fbm_term + \
                 0.20 * rbf_term + 0.06 * saddle_term + 0.04 * cross_term
        
        return result