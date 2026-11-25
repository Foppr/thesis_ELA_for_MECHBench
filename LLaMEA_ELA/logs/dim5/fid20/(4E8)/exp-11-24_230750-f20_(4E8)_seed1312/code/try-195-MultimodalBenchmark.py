import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Modified chaotic sine-cosine wave interactions with altered frequencies and polynomial exponents
        sc_waves = np.sum(np.sin(3.1 * np.pi * x) * np.cos(5.2 * np.pi * x) * 
                         np.exp(-0.4 * np.abs(x)) * np.sin(2.1 * np.pi * x)**3)
        
        # Novel adaptive radial basis functions with modified widths and dynamic centers
        rbf_sum = 0.0
        for i in range(min(7, self.dim)):
            center = np.sin(i * np.pi / 2.3) * 4.1
            width = 1.4 + 0.25 * np.cos(i * np.pi / 3.1)
            rbf_sum += np.exp(-0.35 * ((x[i] - center) / width)**2)
        
        # Advanced hyperbolic tangent coupling with modified weights and interaction terms
        tanh_coupling = 0.85 * np.sum(np.tanh(x[:-3] + 0.45 * x[1:-2] + x[2:-1] + 0.3 * x[3:]) * 
                                    np.tanh(2.7 * x[:-3] - 1.0 * x[1:-2] + 0.75 * x[2:-1] - 0.55 * x[3:]))
        
        # Augmented polynomial cross-terms with modified exponents and interaction scaling
        poly_cross = 0.42 * np.sum(x[:-3]**6 * x[1:-2]**3 * x[2:-1]**4 * x[3:]**6 - 
                                 x[:-3]**3 * x[1:-2]**6 * x[2:-1]**3 * x[3:]**3)
        
        # Dynamic conditioning with multi-scale factors and adaptive curvature
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.4) * np.mean(np.abs(x)) + \
                          0.35 * np.cos(self.dim * 0.27) * np.std(x) + \
                          0.2 * np.sin(self.dim * 0.6) * np.max(np.abs(x))
        
        # Quadratic basin with non-uniform weights, dynamic scaling, coupling terms, and noise modulation
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.35 * x**5))
        
        # Additional chaotic noise component with adaptive intensity and frequency modulation
        noise = 0.12 * np.random.rand() * np.sum(np.sin(7.0 * x) * np.cos(3.2 * x))
        
        # Enhanced exponential decay with multi-scale interactions and dynamic rates
        exp_decay = np.sum(np.exp(-0.6 * (x / (1.0 + 0.45 * np.abs(x)))**6))
        
        # Combined function value with additional interaction terms and improved fitness landscape
        return quadratic + sc_waves + tanh_coupling + rbf_sum + poly_cross + exp_decay + noise