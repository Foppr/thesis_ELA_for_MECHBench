import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine maps with dynamic frequencies and multi-scale coupling
        sine_map = np.sum(np.sin(2.0 * np.pi * x * (1.0 + 0.3 * np.sin(0.7 * np.pi * x))) * 
                         np.exp(-0.2 * np.abs(x)) * np.cos(1.5 * np.pi * x))
        
        # Modified spherical harmonics with adaptive angular frequencies and radial scaling
        sph_harm = 0.0
        for i in range(min(4, self.dim)):
            theta = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0.0
            phi = np.arccos(x[i] / (np.sqrt(x[i]**2 + x[(i+1) % self.dim]**2) + 1e-8))
            sph_harm += np.sin(2.0 * theta) * np.cos(3.0 * phi) * np.exp(-0.1 * (x[i]**2 + x[(i+1) % self.dim]**2))
        
        # Novel hyperbolic tangent coupling with higher-order cross-terms and dynamic weights
        tanh_coupling = 0.6 * np.sum(np.tanh(x[:-3] + 0.5 * x[1:-2] + 0.7 * x[2:-1] + 0.3 * x[3:]) * 
                                   np.tanh(2.0 * x[:-3] - 0.8 * x[1:-2] + 0.9 * x[2:-1] - 0.4 * x[3:]))
        
        # Enhanced radial basis functions with dynamic centers, variable widths, and overlapping kernels
        rbf_sum = 0.0
        for i in range(min(6, self.dim)):
            center = np.sin(i * np.pi / 3.0) * 4.0
            width = 1.2 + 0.8 * np.cos(i * np.pi / 3.0)
            rbf_sum += np.exp(-0.25 * ((x[i] - center) / width)**2)
        
        # Augmented polynomial cross-terms with higher degrees, alternating signs, and interaction scaling
        poly_cross = 0.5 * np.sum(x[:-3]**6 * x[1:-2]**5 * x[2:-1]**4 * x[3:]**3 - 
                                x[:-3]**5 * x[1:-2]**6 * x[2:-1]**3 * x[3:]**4)
        
        # Dynamic conditioning with multi-scale factors and adaptive curvature
        condition_factor = 1.0 + 0.7 * np.sin(self.dim * 0.4) * np.mean(np.abs(x)) + \
                          0.5 * np.cos(self.dim * 0.3) * np.std(x) + \
                          0.3 * np.sin(self.dim * 0.6) * np.max(np.abs(x))
        
        # Quadratic basin with non-uniform weights, dynamic scaling, coupling terms, and noise modulation
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.5 * x**4))
        
        # Additional chaotic noise component with adaptive intensity and frequency modulation
        noise = 0.06 * np.random.rand() * np.sum(np.sin(8 * x) * np.cos(2 * x))
        
        # Combined function value with additional interaction terms and improved fitness landscape
        return quadratic + sine_map + sph_harm + tanh_coupling + rbf_sum + poly_cross + noise