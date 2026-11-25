import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial terms with adaptive coefficients
        adaptive_poly = np.sum((1 + 0.5 * np.sin(np.arange(1, self.dim + 1))) * x**2) + \
                       0.2 * np.sum(x**4) + \
                       0.05 * np.sum(x**6)
        
        # Radial multimodal structure with chaotic sinusoidal modulations
        radial_distance = np.sqrt(np.sum(x**2))
        chaotic_modulation = np.prod(np.sin(3.0 * x + np.pi * np.random.rand(self.dim))) * \
                           np.exp(-0.05 * radial_distance**2)
        
        # Multi-scale sinusoidal oscillations
        multi_scale_osc = 0
        for i in range(1, 6):
            multi_scale_osc += np.sum(np.sin(i * x) * np.cos(i * x * 0.5)) * \
                              np.exp(-0.1 * i * radial_distance)
        
        # Cross-term interactions with non-linear coupling
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += (x[i]**2 + x[i+1]**2) * np.sin(2 * x[i] * x[i+1])
        
        # Add a global trap term to increase difficulty
        trap_term = 10 * np.exp(-0.5 * radial_distance**2) * \
                   np.sum(np.sin(2 * np.pi * x / 2.0)**2)
        
        return adaptive_poly + chaotic_modulation + multi_scale_osc + cross_terms + trap_term