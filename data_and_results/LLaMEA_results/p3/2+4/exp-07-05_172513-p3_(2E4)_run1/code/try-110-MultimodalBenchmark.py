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
        chaotic = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled))
        
        # Enhanced exponential barrier terms with increased complexity and stronger interaction
        barriers = np.sum(4.0 * np.exp(-5.0 * np.abs(x_scaled)) * np.sin(7 * np.pi * x_scaled)**2 + 
                         1.2 * np.exp(-7.0 * np.abs(x_scaled)) * np.cos(10 * np.pi * x_scaled)**2)
        
        # Saddle point structure with added cubic and quartic terms for increased complexity
        saddle = np.sum(x_scaled**6 - 3.0 * x_scaled**2 + 1.5 * x_scaled**3 + 0.4 * x_scaled**7)
        
        # Modified cross-dimensional coupling with stronger interaction and additional sine terms
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(10 * np.pi * x_scaled[:-1]) * 2.0 * np.cos(5 * np.pi * x_scaled[1:]))
        
        # Additional high-order polynomial term to increase landscape ruggedness
        high_order = np.sum(0.7 * x_scaled**8 - 0.8 * x_scaled**6 + 0.3 * x_scaled**5)
        
        # Add a chaotic logistic map component for further complexity with modified parameters
        logistic = np.sum(3.8 * x_scaled * (1 - x_scaled**2))
        
        # Combine all components with adjusted weights
        return 0.6 * quadratic + 2.5 * chaotic + barriers + 0.4 * saddle + 0.25 * coupling + 0.2 * high_order + 0.15 * logistic