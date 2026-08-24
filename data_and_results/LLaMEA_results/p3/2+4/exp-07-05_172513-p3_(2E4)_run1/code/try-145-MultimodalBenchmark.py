import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with modified frequencies
        chaotic = np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled))
        
        # Enhanced exponential barrier terms with increased complexity and stronger interaction
        barriers = np.sum(5.0 * np.exp(-6.0 * np.abs(x_scaled)) * np.sin(8 * np.pi * x_scaled)**2 + 
                         1.5 * np.exp(-8.0 * np.abs(x_scaled)) * np.cos(12 * np.pi * x_scaled)**2)
        
        # Saddle point structure with added cubic and quartic terms for increased complexity
        saddle = np.sum(x_scaled**7 - 3.5 * x_scaled**2 + 1.8 * x_scaled**3 + 0.5 * x_scaled**8)
        
        # Modified cross-dimensional coupling with stronger interaction and additional sine terms
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(12 * np.pi * x_scaled[:-1]) * 2.5 * np.cos(6 * np.pi * x_scaled[1:]))
        
        # Additional high-order polynomial term to increase landscape ruggedness
        high_order = np.sum(0.8 * x_scaled**9 - 0.9 * x_scaled**7 + 0.4 * x_scaled**6)
        
        # Add radial basis function component for increased local optima
        rbf = np.sum(np.exp(-5.0 * (x_scaled**2 + 0.5 * np.abs(x_scaled))**2))
        
        # Combine all components with adjusted weights
        return 0.7 * quadratic + 3.5 * chaotic + barriers + 0.5 * saddle + 0.3 * coupling + 0.25 * high_order + 0.3 * rbf