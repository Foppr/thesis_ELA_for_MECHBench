import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-cosine wave interactions with time-varying frequencies and multi-scale couplings
        sc_waves = np.sum(np.sin(3.1 * np.pi * x) * np.cos(5.2 * np.pi * x) * 
                         np.exp(-0.4 * np.abs(x)) * np.sin(1.7 * np.pi * x))
        
        # Novel adaptive radial basis functions with dynamic centers, variable widths, and overlapping kernels
        rbf_sum = 0.0
        for i in range(min(7, self.dim)):
            center = np.sin(i * np.pi / 1.8) * 4.2
            width = 1.5 + 0.4 * np.cos(i * np.pi / 3.1)
            rbf_sum += np.exp(-0.28 * ((x[i] - center) / width)**2)
        
        # Advanced hyperbolic tangent coupling with higher-order interactions and adaptive weights
        tanh_coupling = 0.75 * np.sum(np.tanh(x[:-3] + 0.5 * x[1:-2] + x[2:-1] + 0.3 * x[3:]) * 
                                   np.tanh(2.7 * x[:-3] - x[1:-2] + 0.8 * x[2:-1] - 0.6 * x[3:]))
        
        # Augmented polynomial cross-terms with higher degrees, alternating signs, and interaction scaling
        poly_cross = 0.42 * np.sum(x[:-3]**6 * x[1:-2]**5 * x[2:-1]**4 * x[3:]**6 - 
                                 x[:-3]**5 * x[1:-2]**6 * x[2:-1]**5 * x[3:]**5)
        
        # Dynamic conditioning with multi-scale factors and adaptive curvature
        condition_factor = 1.0 + 0.52 * np.sin(self.dim * 0.42) * np.mean(np.abs(x)) + \
                          0.35 * np.cos(self.dim * 0.28) * np.std(x) + \
                          0.15 * np.sin(self.dim * 0.62) * np.max(np.abs(x))
        
        # Quadratic basin with non-uniform weights, dynamic scaling, coupling terms, and noise modulation
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.35 * x**5))
        
        # Additional chaotic noise component with adaptive intensity and frequency modulation
        noise = 0.12 * np.random.rand() * np.sum(np.sin(7.1 * x) * np.cos(3.2 * x))
        
        # Enhanced exponential decay with multi-scale interactions and dynamic rates
        exp_decay = np.sum(np.exp(-0.6 * (x / (1.0 + 0.5 * np.abs(x)))**6))
        
        # Introduce additional multimodal complexity through sinusoidal modulation of polynomial terms
        sin_modulation = 0.2 * np.sum(np.sin(2.3 * x) * x**4)
        
        # Add fractal-like self-similarity through recursive polynomial combinations
        fractal_term = 0.15 * np.sum((x[:-2]**3 + x[1:-1]**3 + x[2:]**3)**2)
        
        # Combined function value with additional interaction terms and improved fitness landscape
        return quadratic + sc_waves + tanh_coupling + rbf_sum + poly_cross + exp_decay + noise + sin_modulation + fractal_term