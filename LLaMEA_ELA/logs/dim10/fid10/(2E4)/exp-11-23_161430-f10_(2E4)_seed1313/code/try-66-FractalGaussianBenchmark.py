import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters for fractional Brownian motion
        self.hurst_exponents = 0.3 + 0.4 * np.sin(np.arange(dim) * 0.6)
        # Gaussian radial basis function centers and widths
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = 0.5 + 1.0 * np.random.rand(10)
        # Adaptive conditioning factors
        self.conditioning_factors = 1.0 + 0.5 * np.cos(np.arange(dim) * 0.8)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            rbf_sum += self.widths[i] * np.exp(-0.5 * np.sum(diff**2 / (self.conditioning_factors**2 + 0.1)))
        
        # Fractional Brownian motion component with varying Hurst exponent
        fbm_term = 0.0
        for i in range(self.dim):
            hurst = self.hurst_exponents[i]
            # Simple fractal-like perturbation using power law
            fbm_term += np.sin(x[i]) * np.cos(x[i]**2) * (1.0 + 0.3 * np.sin(hurst * x[i]))
        
        # Cross-dimensional coupling with fractal scaling
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            scale_factor = 0.5 + 0.5 * np.sin(i * 0.4)
            cross_coupling += scale_factor * np.sin(2.0 * x[i]) * np.cos(3.0 * x[j]) * \
                             np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Adaptive conditioning term
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning_factors[i] * (x[i]**6 - 15*x[i]**4 + 75*x[i]**2 - 125)
        
        # Combine all components
        result = 0.2 * np.sum(x**2) + 0.5 * rbf_sum + 0.2 * fbm_term + \
                 0.1 * cross_coupling + 0.05 * cond_term
        
        return result