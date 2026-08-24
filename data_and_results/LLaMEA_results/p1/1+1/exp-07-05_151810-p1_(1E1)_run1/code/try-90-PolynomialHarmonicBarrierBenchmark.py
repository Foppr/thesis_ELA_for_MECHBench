import numpy as np

class PolynomialHarmonicBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with mixed terms
        poly_chaos = np.sum(0.5 * x**4 - 2.0 * x**2 + 0.8 * x**6)
        
        # Logarithmic barrier function with multiple wells
        barrier = 0.0
        for i in range(self.dim):
            barrier += -np.log(0.1 + (x[i] - 2.0)**2) - np.log(0.1 + (x[i] + 2.0)**2)
        
        # Spherical harmonics component with angular dependencies
        sph_harm = 0.0
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            theta = np.arctan2(x[1], x[0]) if self.dim > 1 else 0.0
            phi = np.arccos(x[2] / r) if self.dim > 2 else 0.0
            sph_harm = 2.0 * np.sin(2.0 * theta) * np.cos(3.0 * phi) + 1.5 * np.cos(2.0 * theta) * np.sin(2.0 * phi)
        
        # Cross-terms with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.3 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(0.8 * (x[i] + x[j]))
        
        # Gaussian mixture with varying covariances
        gaussian_mixture = 0.0
        centers = np.linspace(-3.0, 3.0, 5)
        for c in centers:
            gaussian_mixture += 0.8 * np.exp(-0.5 * np.sum((x - c)**2) / (0.5 + 0.2 * np.abs(c)))
        
        # Combine all components
        result = poly_chaos + barrier + sph_harm + cross_term + gaussian_mixture
        
        return result