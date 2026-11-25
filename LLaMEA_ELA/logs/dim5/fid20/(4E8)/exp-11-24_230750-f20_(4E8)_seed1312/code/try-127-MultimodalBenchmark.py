import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine map component with dynamic frequency modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.3 + 1.0)
            chaotic_term += np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Spherical harmonics-based interaction term
        sph_harm = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                sph_harm += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Adaptive polynomial coupling with variable exponents
        poly_coupling = 0.0
        for i in range(self.dim - 2):
            exp1, exp2 = 2 + int(np.sin(i) * 3), 3 + int(np.cos(i) * 2)
            weight = 0.5 + 0.5 * np.sin(i * 0.4)
            poly_coupling += weight * (x[i]**exp1) * (x[i+1]**exp2) * (x[i+2]**(exp1 + exp2))
        
        # Multi-scale Gaussian mixture with varying amplitudes and locations
        gaussian_mixture = 0.0
        for i in range(min(5, self.dim)):
            amp = 1.0 + 0.5 * np.sin(i * 0.6)
            loc = -2.5 + 5.0 * (i / max(1, self.dim - 1))
            width = 0.8 + 0.4 * np.cos(i * 0.5)
            gaussian_mixture += amp * np.exp(-0.5 * ((x[i] - loc) / width)**2)
        
        # Dynamic conditioning based on dimensionality and input statistics
        cond_factor = 1.0 + 0.2 * np.sin(self.dim * 0.2) + 0.1 * np.cos(self.dim * 0.3) * np.std(x)
        
        # Quadratic base with dynamic scaling factor
        quadratic = cond_factor * (np.sum(x**2) + 0.2 * np.sum(x**4) + 0.05 * np.sum(np.abs(x)**3))
        
        # Cross-dimensional coupling using cosine interactions
        cross_coupling = 0.4 * np.sum(np.cos(0.5 * x[:-1]) * np.sin(0.3 * x[1:]))
        
        # Final function value with additive noise
        return quadratic + chaotic_term + sph_harm + poly_coupling + gaussian_mixture + cross_coupling + 0.02 * np.random.rand()