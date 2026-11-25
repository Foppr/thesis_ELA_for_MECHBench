import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential decay with time-varying rates and multi-scale interactions
        exp_decay = np.sum(np.exp(-0.5 * (x / (1.0 + 0.4 * np.abs(x)))**5))
        
        # Modified trigonometric wave interactions with dynamic phase shifts, harmonics, and coupling
        trig_waves = np.sum(np.sin(2.5 * np.pi * x) * np.cos(4.5 * np.pi * x) * 
                           np.exp(-0.3 * np.abs(x)) * np.sin(1.2 * np.pi * x))
        
        # Novel hyperbolic tangent coupling with higher-order interactions and adaptive weights
        tanh_coupling = 0.6 * np.sum(np.tanh(x[:-2] + 0.5 * x[1:-1] + x[2:]) * 
                                   np.tanh(2.5 * x[:-2] - x[1:-1] + 0.8 * x[2:]))
        
        # Enhanced radial basis functions with dynamic centers, variable widths, and overlapping kernels
        rbf_sum = 0.0
        for i in range(min(5, self.dim)):
            center = np.sin(i * np.pi / 2.3) * 3.3
            width = 1.4 + 0.4 * np.cos(i * np.pi / 2.3)
            rbf_sum += np.exp(-0.3 * ((x[i] - center) / width)**2)
        
        # Augmented polynomial cross-terms with higher degrees, alternating signs, and interaction scaling
        poly_cross = 0.35 * np.sum(x[:-2]**6 * x[1:-1]**3 * x[2:]**6 - 
                                 x[:-2]**3 * x[1:-1]**6 * x[2:]**3)
        
        # Dynamic conditioning with multi-scale factors and adaptive curvature
        condition_factor = 1.0 + 0.45 * np.sin(self.dim * 0.33) * np.mean(np.abs(x)) + \
                          0.28 * np.cos(self.dim * 0.19) * np.std(x) + \
                          0.09 * np.sin(self.dim * 0.52) * np.max(np.abs(x))
        
        # Quadratic basin with non-uniform weights, dynamic scaling, coupling terms, and noise modulation
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.28 * x**4))
        
        # Additional chaotic noise component with adaptive intensity and frequency modulation
        noise = 0.07 * np.random.rand() * np.sum(np.sin(6.5 * x) * np.cos(2.8 * x))
        
        # Combined function value with additional interaction terms and improved fitness landscape
        return quadratic + exp_decay + trig_waves + tanh_coupling + rbf_sum + poly_cross + noise