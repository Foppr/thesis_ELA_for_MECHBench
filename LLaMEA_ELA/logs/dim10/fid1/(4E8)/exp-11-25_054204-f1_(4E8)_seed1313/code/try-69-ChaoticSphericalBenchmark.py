import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients
        self.sphere_coeffs = np.random.uniform(-1, 1, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component
        logistic_map = 0.0
        r = 3.9
        for i in range(self.dim):
            if i == 0:
                logistic_map += x[i] * (1 - x[i])
            else:
                logistic_map += x[i-1] * (1 - x[i-1]) * r
        
        # Spherical harmonic interaction term
        sph_harm = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                sph_harm += self.sphere_coeffs[i, j] * np.sin((i+1) * x[j]) * np.cos((j+1) * x[i])
        
        # Adaptive sigmoidal scaling component
        sig_scale = 0.0
        for i in range(self.dim):
            sig_scale += 1.0 / (1.0 + np.exp(-x[i] * (i+1)))
        
        # Fractal-like polynomial with mixed degrees
        fractal_poly = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                fractal_poly += x[i]**(i+2)
            else:
                fractal_poly += x[i]**(i+3) * np.sin(x[i])
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim-1):
            cross_coupling += np.exp(-0.1 * (x[i] - x[i+1])**2) * np.cos(3.0 * x[i])
        
        # Gaussian noise modulation
        noise_mod = np.random.normal(0, 0.1) * np.sum(np.exp(-0.5 * x**2))
        
        return logistic_map + sph_harm + sig_scale + fractal_poly + cross_coupling + noise_mod