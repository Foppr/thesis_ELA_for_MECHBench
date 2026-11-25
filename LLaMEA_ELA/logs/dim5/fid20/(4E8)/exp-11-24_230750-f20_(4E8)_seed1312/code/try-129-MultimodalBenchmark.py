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
            freq = 1.5 + 2.0 * np.sin(i * 0.4 + 1.2)
            chaotic_term += np.sin(freq * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Spherical harmonics-based interaction term
        sph_harm = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                sph_harm += (x[i]**2 + x[i+1]**2) * np.cos(x[i] * x[i+1])
        
        # Adaptive polynomial coupling with variable exponents
        poly_coupling = 0.0
        for i in range(self.dim - 2):
            exp1, exp2 = 3 + int(np.cos(i) * 2), 2 + int(np.sin(i * 0.5) * 3)
            weight = 0.6 + 0.4 * np.cos(i * 0.3)
            poly_coupling += weight * (x[i]**exp1) * (x[i+1]**exp2) * (x[i+2]**(exp1 + exp2))
        
        # Multi-scale Gaussian mixture with varying amplitudes and locations
        gaussian_mixture = 0.0
        for i in range(min(5, self.dim)):
            amp = 1.2 + 0.3 * np.cos(i * 0.7)
            loc = -3.0 + 6.0 * (i / max(1, self.dim - 1))
            width = 0.9 + 0.3 * np.sin(i * 0.6)
            gaussian_mixture += amp * np.exp(-0.5 * ((x[i] - loc) / width)**2)
        
        # Dynamic conditioning based on dimensionality and input statistics
        cond_factor = 1.0 + 0.15 * np.cos(self.dim * 0.25) + 0.12 * np.sin(self.dim * 0.35) * np.std(x)
        
        # Quadratic base with dynamic scaling factor
        quadratic = cond_factor * (np.sum(x**2) + 0.25 * np.sum(x**4) + 0.06 * np.sum(np.abs(x)**3))
        
        # Cross-dimensional coupling using hyperbolic tangent interactions
        cross_coupling = 0.3 * np.sum(np.tanh(0.4 * x[:-1]) * np.sin(0.25 * x[1:]))
        
        # Final function value with additive noise
        return quadratic + chaotic_term + sph_harm + poly_coupling + gaussian_mixture + cross_coupling + 0.015 * np.random.rand()