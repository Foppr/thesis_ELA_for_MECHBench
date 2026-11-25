import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential decay with time-varying rates
        exp_decay = np.sum(np.exp(-0.3 * (x / (1.0 + 0.2 * np.abs(x)))**3))
        
        # Modified trigonometric wave interactions with dynamic phase shifts and harmonics
        trig_waves = np.sum(np.sin(3 * np.pi * x) * np.cos(5 * np.pi * x) * 
                           np.exp(-0.15 * np.abs(x)) * np.sin(0.5 * np.pi * x))
        
        # Novel hyperbolic tangent coupling with higher-order interactions
        tanh_coupling = 0.7 * np.sum(np.tanh(x[:-2] + x[1:-1] + x[2:]) * 
                                   np.tanh(3 * x[:-2] - 2 * x[1:-1] + x[2:]))
        
        # Enhanced radial basis functions with dynamic centers and variable widths
        rbf_sum = 0.0
        for i in range(min(5, self.dim)):
            center = np.sin(i * np.pi / 4) * 3.5
            width = 1.5 + 0.3 * np.cos(i * np.pi / 4)
            rbf_sum += np.exp(-0.3 * ((x[i] - center) / width)**2)
        
        # Augmented polynomial cross-terms with higher degrees and alternating signs
        poly_cross = 0.4 * np.sum(x[:-2]**3 * x[1:-1]**2 * x[2:]**3 - 
                                x[:-2]**2 * x[1:-1]**3 * x[2:]**2)
        
        # Dynamic conditioning with multi-scale factors
        condition_factor = 1.0 + 0.4 * np.sin(self.dim * 0.3) * np.mean(np.abs(x)) + \
                          0.2 * np.cos(self.dim * 0.15) * np.std(x)
        
        # Quadratic basin with non-uniform weights, dynamic scaling, and coupling terms
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.2 * x**3))
        
        # Additional chaotic noise component with adaptive intensity
        noise = 0.08 * np.random.rand() * np.sum(np.sin(7 * x) * np.cos(3 * x))
        
        # Combined function value with additional interaction terms
        return quadratic + exp_decay + trig_waves + tanh_coupling + rbf_sum + poly_cross + noise