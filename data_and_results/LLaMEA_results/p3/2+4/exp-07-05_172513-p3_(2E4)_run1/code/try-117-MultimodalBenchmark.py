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
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled))
        
        # Enhanced exponential barrier terms with increased complexity
        barriers = np.sum(3.0 * np.exp(-4.0 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**2 + 
                         0.8 * np.exp(-6.0 * np.abs(x_scaled)) * np.cos(8 * np.pi * x_scaled)**2)
        
        # Saddle point structure with added cubic and quartic terms for increased complexity
        saddle = np.sum(x_scaled**5 - 2.5 * x_scaled**2 + 1.1 * x_scaled**3 + 0.3 * x_scaled**6)
        
        # Modified cross-dimensional coupling with stronger interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * 1.5)
        
        # Additional high-order polynomial term to increase landscape ruggedness
        high_order = np.sum(0.5 * x_scaled**7 - 0.6 * x_scaled**5 + 0.2 * x_scaled**4)
        
        # Add a chaotic logistic map component for further complexity
        logistic = np.sum(4.0 * x_scaled * (1 - x_scaled))
        
        # Combine all components with adjusted weights
        return 0.5 * quadratic + 2.2 * chaotic + barriers + 0.3 * saddle + 0.2 * coupling + 0.15 * high_order + 0.1 * logistic