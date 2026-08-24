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
        chaotic = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Enhanced exponential barrier terms with increased complexity
        barriers = np.sum(2.0 * np.exp(-3 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled)**2 + 
                         0.5 * np.exp(-5 * np.abs(x_scaled)) * np.cos(6 * np.pi * x_scaled)**2)
        
        # Saddle point structure with added cubic and quartic terms for increased complexity
        saddle = np.sum(x_scaled**4 - 2 * x_scaled**2 + 0.8 * x_scaled**3 + 0.2 * x_scaled**5)
        
        # Modified cross-dimensional coupling with stronger interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(6 * np.pi * x_scaled[:-1]) * 0.9)
        
        # Additional high-order polynomial term to increase landscape ruggedness
        high_order = np.sum(0.3 * x_scaled**6 - 0.4 * x_scaled**5)
        
        # Combine all components with adjusted weights
        return 0.4 * quadratic + 1.8 * chaotic + barriers + 0.25 * saddle + 0.15 * coupling + 0.1 * high_order