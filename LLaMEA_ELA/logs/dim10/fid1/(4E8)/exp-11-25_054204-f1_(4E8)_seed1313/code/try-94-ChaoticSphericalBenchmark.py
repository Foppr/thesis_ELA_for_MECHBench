import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients with increased complexity
        self.sphere_coeffs = np.random.uniform(-2, 2, (dim, dim))
        self.logistic_coeffs = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component with multiple iterations
        logistic_map = 0.0
        r = 3.9
        for i in range(self.dim):
            if i == 0:
                logistic_map += x[i] * r * (1 - x[i])
            else:
                logistic_map += self.logistic_coeffs[i-1] * x[i-1] * r * (1 - x[i-1])
        
        # Enhanced spherical harmonic interaction term with higher order terms
        sph_harm = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                sph_harm += self.sphere_coeffs[i, j] * np.sin((i+1) * x[j]) * np.cos((j+1) * x[i]) * np.exp(-0.1 * (i+j))
        
        # Adaptive sigmoidal scaling with dynamic weights
        sig_scale = 0.0
        for i in range(self.dim):
            sig_scale += 1.0 / (1.0 + np.exp(-x[i] * (i+1) * np.sin(i))) * np.cos(x[i])
        
        # Fractal-like polynomial with mixed degrees and additional trigonometric terms
        fractal_poly = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                fractal_poly += x[i]**(i+2) * np.sin(x[i] * (i+1))
            elif i % 3 == 1:
                fractal_poly += x[i]**(i+4) * np.cos(x[i])
            else:
                fractal_poly += x[i]**(i+5) * np.tan(x[i] * 0.5)
        
        # Enhanced cross-dimensional coupling with multiple interaction types
        cross_coupling = 0.0
        for i in range(self.dim-1):
            cross_coupling += np.exp(-0.2 * (x[i] - x[i+1])**2) * np.cos(3.0 * x[i]) * np.sin(x[i+1])
            cross_coupling += np.sin(0.5 * (x[i] + x[i+1])) * np.exp(-0.1 * (x[i] - x[i+1])**2)
        
        # Multi-scale noise modulation with varying amplitudes
        noise_mod = 0.0
        for i in range(self.dim):
            noise_mod += np.random.normal(0, 0.05 * (i+1)) * np.exp(-0.5 * x[i]**2) * np.sin(x[i] * (i+1))
        
        # Additional harmonic coupling terms
        harmonic_coupling = 0.0
        for i in range(self.dim):
            harmonic_coupling += np.sin(x[i] * (i+1)) * np.cos(x[i] * (i+2)) * np.exp(-0.05 * x[i]**2)
        
        # Combined result with additional scaling factors
        return 1.5 * logistic_map + 0.8 * sph_harm + 1.2 * sig_scale + 0.6 * fractal_poly + 1.0 * cross_coupling + 0.7 * noise_mod + 0.4 * harmonic_coupling