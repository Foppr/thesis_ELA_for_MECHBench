import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential decay with sinusoidal modulation
        exp_decay = np.sum(np.exp(-0.3 * (x / (1.0 + 0.2 * np.abs(x)))**2) * 
                          np.sin(3 * x + np.pi/4))
        
        # Complex trigonometric wave interactions with dynamic phase shifts
        trig_waves = np.sum(np.sin(3 * np.pi * x) * np.cos(5 * np.pi * x) * 
                           np.exp(-0.15 * np.abs(x)) * 
                           np.cos(0.5 * np.pi * x**2))
        
        # Novel hyperbolic tangent coupling with higher-order interactions
        tanh_coupling = 0.7 * np.sum(np.tanh(x[:-2] + x[1:-1] + x[2:]) * 
                                   np.tanh(3 * x[:-2] - 2 * x[1:-1] + x[2:]))
        
        # Multi-scale radial basis functions with varying centers and widths
        rbf_sum = 0.0
        for i in range(min(5, self.dim)):
            center = np.sin(i * np.pi / 5) * 3.5
            width = 1.5 + 0.8 * np.cos(i * np.pi / 5)
            rbf_sum += np.exp(-0.3 * ((x[i] - center) / width)**2)
        
        # Enhanced polynomial cross-terms with non-uniform exponents and coefficients
        poly_cross = 0.4 * np.sum(x[:-1]**3 * x[1:]**4 - x[:-1]**4 * x[1:]**3 + 
                                0.5 * x[:-2]**2 * x[1:-1]**3 * x[2:]**2)
        
        # Dynamic conditioning with multi-scale modulation
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.3) * np.mean(np.abs(x)) * 
                          np.cos(0.2 * self.dim)
        
        # Quadratic basin with enhanced non-uniform weights and dynamic scaling
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.2 * x**3 + 0.1 * x**4))
        
        # Additional chaotic noise term with multiple frequency components
        noise = 0.1 * np.random.rand() * np.sum(np.sin(7 * x) + np.cos(4 * x) * 
                                               np.exp(-0.2 * np.abs(x)))
        
        # Combined function value
        return quadratic + exp_decay + trig_waves + tanh_coupling + rbf_sum + poly_cross + noise