import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced chaotic sinusoidal component with higher frequency variations
        chaotic = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled) + 
                         np.sin(12 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled))
        
        # Modified exponential barrier terms with increased complexity and varied parameters
        barriers = np.sum(2.5 * np.exp(-5.0 * np.abs(x_scaled)) * np.sin(6 * np.pi * x_scaled)**2 + 
                         1.2 * np.exp(-7.0 * np.abs(x_scaled)) * np.cos(10 * np.pi * x_scaled)**2 +
                         0.8 * np.exp(-3.0 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled)**3)
        
        # Saddle point structure with added higher-order polynomial terms
        saddle = np.sum(x_scaled**6 - 3.0 * x_scaled**2 + 1.5 * x_scaled**4 + 0.4 * x_scaled**7)
        
        # Modified cross-dimensional coupling with stronger interaction and additional trigonometric terms
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(10 * np.pi * x_scaled[:-1]) * 
                         np.cos(5 * np.pi * x_scaled[1:]) * 2.0)
        
        # Additional high-order polynomial term to increase landscape ruggedness
        high_order = np.sum(0.6 * x_scaled**8 - 0.7 * x_scaled**6 + 0.3 * x_scaled**5)
        
        # Add a modified logistic map component with different parameters for further complexity
        logistic = np.sum(3.8 * x_scaled * (1 - x_scaled**2))
        
        # Combine all components with adjusted weights for better balance
        return 0.4 * quadratic + 2.5 * chaotic + barriers + 0.25 * saddle + 0.2 * coupling + 0.18 * high_order + 0.12 * logistic