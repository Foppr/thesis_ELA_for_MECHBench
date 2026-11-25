import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters
        self.amp = 1.5 + 0.5 * np.sin(np.arange(dim) * 0.3)
        self.beta = 0.7 + 0.3 * np.cos(np.arange(dim) * 0.4)
        # Fractal Brownian motion parameters
        self.hurst = 0.3 + 0.4 * np.random.rand(dim)
        self.fractal_scale = 2.0 + 1.5 * np.sin(np.arange(dim) * 0.25)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component
        tent_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Tent map: f(x) = a * min(x, 1-x) if x < 0.5 else a * min(1-x, x)
            if xi < 0.5:
                tent_val = self.amp[i] * xi
            else:
                tent_val = self.amp[i] * (1 - xi)
            # Add chaotic modulation
            tent_term += tent_val * np.sin(self.beta[i] * xi) * np.exp(-0.1 * i)
        
        # Fractal Brownian motion component
        fbm_term = 0.0
        for i in range(self.dim):
            # Generate fractal noise using Hurst parameter
            noise_val = np.random.normal(0, 1) * self.fractal_scale[i]
            # Combine with position and dimension-dependent scaling
            fbm_term += noise_val * np.cos(2.0 * np.pi * x[i] * (i + 1)) * \
                       np.exp(-0.05 * (x[i]**2 + i**2))
        
        # Multi-scale radial basis function component with varying scales
        rbf_term = 0.0
        scales = np.linspace(0.5, 3.0, min(8, self.dim // 2 + 1))
        for level, scale in enumerate(scales):
            centers = np.linspace(-4.5, 4.5, max(3, self.dim // (level + 1)))
            for i, center in enumerate(centers):
                sigma = scale * (1.0 + 0.2 * np.sin(i * 0.5))
                rbf_term += np.exp(-0.5 * ((x[i % self.dim] - center) / sigma)**2) * \
                           np.sin(3.14 * (x[i % self.dim] - center) / sigma)
        
        # Saddle point structure with varying coefficients
        saddle_term = 0.0
        for i in range(self.dim):
            base = x[i]
            saddle_term += (base**5 - 5*base**3 + 4*base) * \
                          np.cos(0.5 * base) * np.exp(-0.1 * i)
        
        # Cross-dimensional interaction with fractal coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            k = (i + 5) % self.dim
            weight = 1.0 + 0.3 * np.sin(i * 0.4) * np.cos(x[j] * 0.3)
            cross_term += weight * np.sin(2.5 * x[i]) * np.cos(1.8 * x[j]) * \
                         np.tanh(0.7 * (x[k] - x[i])) * \
                         np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Combine all components
        result = 0.3 * np.sum(x**2) + 0.25 * tent_term + 0.2 * fbm_term + \
                 0.15 * rbf_term + 0.1 * saddle_term + 0.05 * cross_term
        
        return result