import numpy as np

class QuaternionSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic degrees and coefficients
        self.degrees = np.arange(1, dim + 1)
        self.coeffs = 1.0 / (1.0 + np.arange(dim))
        # Quaternion-inspired coupling parameters
        self.quat_weights = np.random.rand(dim) * 2.0 - 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with Chebyshev polynomials
        poly_chaos = 0.0
        for i in range(self.dim):
            T_n = np.cos(self.degrees[i] * np.arccos(np.clip(x[i] / 5.0, -1.0, 1.0)))
            poly_chaos += self.coeffs[i] * T_n * np.sin(0.5 * x[i])
        
        # Spherical harmonics component
        sph_harm = 0.0
        for i in range(self.dim):
            sph_harm += (x[i]**2) * np.cos(self.degrees[i] * np.arctan2(x[(i+1)%self.dim], x[i])) * np.sin(0.3 * x[i])
        
        # Quaternion-inspired coupling with imaginary components
        quat_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            quat_coupling += (x[i] * x[j] - x[k]) * self.quat_weights[i]
        
        # Cross-dimensional polynomial interactions with exponential decay
        cross_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_poly += (x[i]**3 + x[j]**3) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Fractal-like radial component with recursive scaling
        fractal_radial = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            fractal_radial += np.sin(r * (1.0 + 0.1 * i)) * np.cos(0.5 * x[i])
        
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combined function with dynamic weighting
        return cond_factor * (0.7 * poly_chaos + 0.6 * sph_harm + 0.5 * quat_coupling + 
                             0.4 * cross_poly + 0.3 * fractal_radial)