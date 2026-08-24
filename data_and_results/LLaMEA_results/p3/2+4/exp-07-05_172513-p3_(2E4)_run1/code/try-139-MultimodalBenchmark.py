import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with varying frequencies and added chaos
        chaotic = np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(25 * np.pi * x_scaled) + 
                         np.sin(15 * np.pi * x_scaled**2) * np.cos(10 * np.pi * x_scaled**3))
        
        # Enhanced exponential barrier terms with increased complexity and stronger interaction
        barriers = np.sum(6.0 * np.exp(-7.0 * np.abs(x_scaled)) * np.sin(10 * np.pi * x_scaled)**2 + 
                         2.0 * np.exp(-9.0 * np.abs(x_scaled)) * np.cos(15 * np.pi * x_scaled)**2 + 
                         1.0 * np.exp(-5.0 * np.abs(x_scaled)) * np.sin(20 * np.pi * x_scaled)**3)
        
        # Saddle point structure with added cubic and quartic terms for increased complexity
        saddle = np.sum(x_scaled**9 - 4.0 * x_scaled**2 + 2.0 * x_scaled**3 + 0.8 * x_scaled**10 + 
                       0.3 * x_scaled**7)
        
        # Modified cross-dimensional coupling with stronger interaction and additional sine terms
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(15 * np.pi * x_scaled[:-1]) * 
                         np.cos(8 * np.pi * x_scaled[1:]) * 3.0 + 
                         x_scaled[:-1]**2 * x_scaled[1:]**2 * np.sin(12 * np.pi * x_scaled[:-1]**2))
        
        # Additional high-order polynomial term to increase landscape ruggedness
        high_order = np.sum(1.0 * x_scaled**11 - 1.2 * x_scaled**8 + 0.6 * x_scaled**7 - 0.4 * x_scaled**5)
        
        # Add a chaotic logistic map component for further complexity with modified parameters
        logistic = np.sum(5.0 * x_scaled * (1 - x_scaled**3) + 0.5 * x_scaled**2 * np.sin(25 * np.pi * x_scaled))
        
        # Add a novel hyper-chaotic term with multiple interacting sinusoids
        hyperchaos = np.sum(np.sin(35 * np.pi * x_scaled) * np.cos(30 * np.pi * x_scaled) * 
                           np.sin(25 * np.pi * x_scaled**2) * np.cos(20 * np.pi * x_scaled**3))
        
        # Combine all components with adjusted weights
        return 0.8 * quadratic + 4.0 * chaotic + barriers + 0.6 * saddle + 0.4 * coupling + 0.3 * high_order + 0.25 * logistic + 0.3 * hyperchaos