import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Intensified chaotic exponential decay with multi-scale interactions and enhanced non-linearity
        exp_decay = np.sum(np.exp(-0.8 * (x / (1.0 + 0.6 * np.abs(x)))**7))
        
        # Augmented trigonometric wave interactions with higher harmonics, dynamic phase modulation, and coupling
        trig_waves = np.sum(np.sin(5.0 * np.pi * x) * np.cos(7.0 * np.pi * x) * 
                           np.exp(-0.5 * np.abs(x)) * np.sin(2.0 * np.pi * x) * 
                           np.cos(3.0 * np.pi * x))
        
        # Novel hyperbolic tangent cascades with higher-order coupling and adaptive weights
        tanh_coupling = 1.2 * np.sum(np.tanh(x[:-3] + 0.8 * x[1:-2] + 0.6 * x[2:-1] + x[3:]) * 
                                   np.tanh(4.0 * x[:-3] - 1.2 * x[1:-2] + 0.8 * x[2:-1] - x[3:]))
        
        # Enhanced radial basis functions with dynamic centers, variable widths, overlapping kernels, and multi-scale interactions
        rbf_sum = 0.0
        for i in range(min(7, self.dim)):
            center = np.sin(i * np.pi / 2.0) * 4.0
            width = 2.0 + 0.8 * np.cos(i * np.pi / 3.0)
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**3)
        
        # Augmented polynomial cross-terms with higher degrees, alternating signs, interaction scaling, and multi-dimensional coupling
        poly_cross = 0.6 * np.sum(x[:-3]**9 * x[1:-2]**5 * x[2:-1]**8 * x[3:]**6 - 
                                x[:-3]**5 * x[1:-2]**9 * x[2:-1]**6 * x[3:]**8)
        
        # Dynamic conditioning with multi-scale factors, adaptive curvature, and enhanced interaction terms
        condition_factor = 1.0 + 0.7 * np.sin(self.dim * 0.5) * np.mean(np.abs(x)) + \
                          0.5 * np.cos(self.dim * 0.3) * np.std(x) + \
                          0.4 * np.sin(self.dim * 0.6) * np.max(np.abs(x)) + \
                          0.2 * np.cos(self.dim * 0.4) * np.min(np.abs(x))
        
        # Quadratic basin with non-uniform weights, dynamic scaling, coupling terms, noise modulation, and enhanced curvature
        quadratic = condition_factor * np.sum((x**3) * (1.0 + 0.5 * x**5))
        
        # Additional chaotic noise component with adaptive intensity, frequency modulation, and multi-scale interference
        noise = 0.12 * np.random.rand() * np.sum(np.sin(9 * x) * np.cos(4.0 * x) * np.tanh(x))
        
        # Combined function value with additional interaction terms and improved fitness landscape
        return quadratic + exp_decay + trig_waves + tanh_coupling + rbf_sum + poly_cross + noise