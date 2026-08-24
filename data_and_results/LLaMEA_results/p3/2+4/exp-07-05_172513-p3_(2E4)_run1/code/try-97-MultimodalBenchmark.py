import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with varying frequencies and enhanced nonlinearity
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled) * np.sin(8 * np.pi * x_scaled))
        
        # Enhanced exponential barrier terms with increased complexity and novel interaction
        barriers = np.sum(3.2 * np.exp(-4.0 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**3 + 
                         1.1 * np.exp(-6.0 * np.abs(x_scaled)) * np.cos(8 * np.pi * x_scaled)**3 +
                         0.8 * np.exp(-2.5 * np.abs(x_scaled)) * np.sin(10 * np.pi * x_scaled)**2)
        
        # Saddle point structure with added cubic, quartic, and quintic terms for increased complexity
        saddle = np.sum(x_scaled**5 - 2.5 * x_scaled**3 + 1.2 * x_scaled**4 + 0.8 * x_scaled**2 + 0.3 * x_scaled**6)
        
        # Novel cross-dimensional coupling with higher-order interactions and chaotic modulation
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * 
                         np.cos(5 * np.pi * x_scaled[1:]) * 1.5)
        
        # Additional high-order polynomial term with chaotic modulation to increase landscape ruggedness
        high_order = np.sum(0.5 * x_scaled**7 - 0.6 * x_scaled**6 + 0.2 * x_scaled**5)
        
        # Novel chaotic coupling between all dimensions
        chaotic_coupling = np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled) * 
                                np.sin(6 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Combine all components with adjusted weights
        return 0.5 * quadratic + 2.2 * chaotic + barriers + 0.3 * saddle + 0.25 * coupling + 0.15 * high_order + 0.2 * chaotic_coupling