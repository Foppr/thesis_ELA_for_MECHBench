import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential decay with time-varying rates and memory effects
        exp_decay = np.sum(np.exp(-0.4 * (x / (1.0 + 0.3 * np.abs(x)))**4) * 
                          np.sin(0.2 * x)**2)
        
        # Modified trigonometric wave interactions with dynamic phase shifts, harmonics and coupling
        trig_waves = np.sum(np.sin(4 * np.pi * x) * np.cos(6 * np.pi * x) * 
                           np.exp(-0.2 * np.abs(x)) * np.sin(0.7 * np.pi * x) * 
                           np.cos(0.3 * np.pi * x))
        
        # Novel hyperbolic tangent coupling with higher-order interactions and adaptive weights
        tanh_coupling = 0.8 * np.sum(np.tanh(x[:-3] + x[1:-2] + x[2:-1] + x[3:]) * 
                                   np.tanh(2 * x[:-3] - x[1:-2] + 0.5 * x[2:-1] - x[3:]))
        
        # Enhanced radial basis functions with dynamic centers, variable widths and multi-scale influences
        rbf_sum = 0.0
        for i in range(min(6, self.dim)):
            center = np.sin(i * np.pi / 5) * 4.0
            width = 2.0 + 0.4 * np.cos(i * np.pi / 5)
            rbf_sum += np.exp(-0.4 * ((x[i] - center) / width)**3)
        
        # Augmented polynomial cross-terms with higher degrees, alternating signs and coupling
        poly_cross = 0.5 * np.sum(x[:-3]**4 * x[1:-2]**3 * x[2:-1]**2 * x[3:]**4 - 
                                x[:-3]**2 * x[1:-2]**3 * x[2:-1]**4 * x[3:]**2)
        
        # Dynamic conditioning with multi-scale factors and memory-dependent dynamics
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.4) * np.mean(np.abs(x)) + \
                          0.3 * np.cos(self.dim * 0.2) * np.std(x) + \
                          0.1 * np.sin(0.1 * self.dim) * np.max(np.abs(x))
        
        # Quadratic basin with non-uniform weights, dynamic scaling, coupling terms and chaotic modulation
        quadratic = condition_factor * np.sum((x**3) * (1.0 + 0.3 * x**2) * np.cos(0.1 * x))
        
        # Additional chaotic noise component with adaptive intensity and memory effects
        noise = 0.1 * np.random.rand() * np.sum(np.sin(8 * x) * np.cos(4 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combined function value with additional interaction terms and fractal-like scaling
        return quadratic + exp_decay + trig_waves + tanh_coupling + rbf_sum + poly_cross + noise