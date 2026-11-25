import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Modified chaotic sine-cosine wave interactions with altered frequency multipliers
        sc_waves = np.sum(np.sin(2.8 * np.pi * x) * np.cos(4.9 * np.pi * x) * 
                         np.exp(-0.35 * np.abs(x)) * np.sin(1.9 * np.pi * x))
        
        # Novel adaptive radial basis functions with dynamic centers, variable widths, and overlapping kernels
        rbf_sum = 0.0
        for i in range(min(7, self.dim)):
            center = np.sin(i * np.pi / 2.1) * 3.9
            width = 1.4 + 0.3 * np.cos(i * np.pi / 2.8)
            rbf_sum += np.exp(-0.25 * ((x[i] - center) / width)**2)
        
        # Advanced hyperbolic tangent coupling with higher-order interactions and adaptive weights
        tanh_coupling = 0.7 * np.sum(np.tanh(x[:-3] + 0.4 * x[1:-2] + x[2:-1] + 0.25 * x[3:]) * 
                                   np.tanh(2.5 * x[:-3] - x[1:-2] + 0.7 * x[2:-1] - 0.5 * x[3:]))
        
        # Added quartic polynomial cross-term with alternating signs and enhanced interaction scaling
        poly_cross = 0.38 * np.sum(x[:-3]**4 * x[1:-2]**3 * x[2:-1]**2 * x[3:]**4 - 
                                 x[:-3]**3 * x[1:-2]**4 * x[2:-1]**3 * x[3:]**3)
        
        # Dynamic conditioning with multi-scale factors and adaptive curvature
        condition_factor = 1.0 + 0.48 * np.sin(self.dim * 0.39) * np.mean(np.abs(x)) + \
                          0.32 * np.cos(self.dim * 0.25) * np.std(x) + \
                          0.18 * np.sin(self.dim * 0.59) * np.max(np.abs(x))
        
        # Quadratic basin with non-uniform weights, dynamic scaling, coupling terms, and noise modulation
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.32 * x**4))
        
        # Additional chaotic noise component with adaptive intensity and frequency modulation
        noise = 0.1 * np.random.rand() * np.sum(np.sin(6.9 * x) * np.cos(3.0 * x))
        
        # Enhanced exponential decay with multi-scale interactions and dynamic rates
        exp_decay = np.sum(np.exp(-0.55 * (x / (1.0 + 0.45 * np.abs(x)))**5))
        
        # Combined function value with additional interaction terms and improved fitness landscape
        return quadratic + sc_waves + tanh_coupling + rbf_sum + poly_cross + exp_decay + noise