import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients with higher frequency components
        self.sphere_coeffs = np.random.uniform(-2, 2, (dim, dim))
        # Add chaotic parameter variation for each dimension
        self.chaotic_params = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logistic map with dimension-specific chaotic parameters
        logistic_map = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic_map += x[i] * (1 - x[i])
            else:
                logistic_map += x[i-1] * (1 - x[i-1]) * self.chaotic_params[i-1]
        
        # Modified spherical harmonic with weighted cross-terms
        sph_harm = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                # Add coupling strength that depends on dimension indices
                coupling_strength = (i+1) * (j+1) / (self.dim**2)
                sph_harm += self.sphere_coeffs[i, j] * coupling_strength * np.sin((i+1) * x[j]) * np.cos((j+1) * x[i])
        
        # Enhanced sigmoidal scaling with exponential weighting
        sig_scale = 0.0
        for i in range(self.dim):
            # Use exponential weighting to emphasize early dimensions
            weight = np.exp(-i * 0.5)
            sig_scale += weight * (1.0 / (1.0 + np.exp(-x[i] * (i+1) * 0.5)))
        
        # Improved fractal-like polynomial with mixed trigonometric and power terms
        fractal_poly = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                fractal_poly += x[i]**(i+2) * np.sin(x[i] * (i+1))
            elif i % 3 == 1:
                fractal_poly += x[i]**(i+3) * np.cos(x[i] * (i+1))
            else:
                fractal_poly += x[i]**(i+4) * np.tan(x[i] * (i+1) / 2.0)
        
        # Enhanced cross-dimensional coupling with multiple interaction types
        cross_coupling = 0.0
        for i in range(self.dim-1):
            # Add both exponential and trigonometric coupling
            cross_coupling += np.exp(-0.1 * (x[i] - x[i+1])**2) * np.cos(3.0 * x[i])
            cross_coupling += 0.5 * np.sin(0.5 * (x[i] + x[i+1])) * np.exp(-0.05 * (x[i] + x[i+1])**2)
        
        # Add a global scaling factor based on the norm of x
        norm_factor = np.linalg.norm(x) / self.dim
        
        # Add periodic modulation to increase landscape irregularity
        periodic_mod = 0.0
        for i in range(self.dim):
            periodic_mod += np.sin(x[i] * np.pi * (i+1)) * np.cos(x[i] * np.pi * (i+1) / 2.0)
        
        # Combine all components with adaptive weights
        result = logistic_map + sph_harm + sig_scale + fractal_poly + cross_coupling + periodic_mod
        
        # Add a final normalization and scaling term
        result *= (1.0 + 0.1 * norm_factor)
        
        return result