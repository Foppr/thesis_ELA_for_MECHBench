import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with varying frequencies
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled))
        
        # Enhanced exponential barrier terms with increased complexity
        barriers = np.sum(3.2 * np.exp(-4.2 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**2 + 
                         0.8 * np.exp(-6.8 * np.abs(x_scaled)) * np.cos(7 * np.pi * x_scaled)**2)
        
        # Saddle point structure with added cubic and quartic terms for increased complexity
        saddle = np.sum(x_scaled**5 - 2.8 * x_scaled**2 + 1.1 * x_scaled**3 + 0.35 * x_scaled**6)
        
        # Modified cross-dimensional coupling with stronger interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * 1.3)
        
        # Additional high-order polynomial term to increase landscape ruggedness
        high_order = np.sum(0.45 * x_scaled**7 - 0.55 * x_scaled**6 + 0.1 * x_scaled**8)
        
        # New component: Nonlinear frequency modulation with phase shifts
        modulation = np.sum(np.sin(9 * np.pi * x_scaled + 0.5 * np.sin(3 * np.pi * x_scaled)) * 
                           np.cos(8 * np.pi * x_scaled + 0.3 * np.cos(4 * np.pi * x_scaled)))
        
        # New component: Multi-scale oscillatory pattern with random phase shifts
        multi_scale = np.sum(1.5 * np.sin(12 * np.pi * x_scaled + np.random.rand() * np.pi) * 
                            np.cos(10 * np.pi * x_scaled + np.random.rand() * np.pi))
        
        # Combine all components with adjusted weights
        return 0.5 * quadratic + 2.1 * chaotic + barriers + 0.32 * saddle + 0.22 * coupling + 0.15 * high_order + 0.25 * modulation + 0.18 * multi_scale