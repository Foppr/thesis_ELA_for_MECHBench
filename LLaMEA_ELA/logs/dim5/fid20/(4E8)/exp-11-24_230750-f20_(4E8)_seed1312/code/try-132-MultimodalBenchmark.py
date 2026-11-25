import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine map with dynamic frequency modulation and multi-scale coupling
        chaotic_sine = np.sum(np.sin(2.0 * np.pi * x * (1.0 + 0.3 * np.sin(0.7 * np.pi * x))) * 
                             np.exp(-0.2 * np.abs(x)) * np.cos(1.5 * np.pi * x))
        
        # Spherical harmonics with variable degree and angular coupling
        sph_harm = 0.0
        for i in range(min(4, self.dim)):
            theta = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0
            phi = np.arccos(x[i] / (np.sqrt(np.sum(x**2)) + 1e-8))
            sph_harm += np.sin((i+1) * theta) * np.cos((i+2) * phi) * np.exp(-0.1 * (x[i]**2 + x[(i+1)%self.dim]**2))
        
        # Adaptive polynomial interactions with dynamic exponents and cross-term scaling
        poly_interaction = 0.0
        for i in range(min(3, self.dim)):
            poly_interaction += (x[i]**(3 + i%2) * x[(i+1)%self.dim]**(4 - i%2) * 
                               np.exp(-0.1 * np.abs(x[i] - x[(i+1)%self.dim])))
        
        # Novel hyperbolic tangent coupling with higher-order cross-terms and dynamic weights
        tanh_coupling = 0.8 * np.sum(np.tanh(2.0 * x[:-3] + 1.5 * x[1:-2] + 0.9 * x[2:-1] + 0.6 * x[3:]) * 
                                   np.tanh(x[:-3] - 0.7 * x[1:-2] + 1.2 * x[2:-1] - 0.5 * x[3:]))
        
        # Enhanced radial basis functions with dynamic centers, variable widths, and overlapping kernels
        rbf_sum = 0.0
        for i in range(min(6, self.dim)):
            center = np.sin(i * np.pi / 3.0) * 4.0
            width = 2.0 + 0.8 * np.cos(i * np.pi / 3.0)
            rbf_sum += np.exp(-0.4 * ((x[i] - center) / width)**2)
        
        # Multi-scale chaotic exponential decay with adaptive time-varying rates
        exp_decay = np.sum(np.exp(-0.6 * (x / (1.0 + 0.3 * np.abs(x)))**7))
        
        # Quadratic basin with non-uniform weights, dynamic scaling, and coupling terms
        quadratic = np.sum((x**2) * (1.0 + 0.5 * np.sin(0.5 * np.pi * x)) * 
                          (1.0 + 0.3 * np.cos(0.3 * np.pi * x)))
        
        # Additional chaotic noise component with adaptive intensity and frequency modulation
        noise = 0.1 * np.random.rand() * np.sum(np.sin(8 * x) * np.cos(4 * x))
        
        # Combined function value with additional interaction terms and improved fitness landscape
        return quadratic + chaotic_sine + sph_harm + poly_interaction + tanh_coupling + rbf_sum + exp_decay + noise