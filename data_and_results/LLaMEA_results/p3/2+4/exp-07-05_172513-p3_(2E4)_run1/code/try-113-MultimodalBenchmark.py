import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Periodic trigonometric components with varying frequencies and amplitudes
        periodic = np.sum(np.sin(10 * x_scaled) * np.cos(7 * x_scaled) + 
                         0.5 * np.sin(15 * x_scaled) * np.cos(12 * x_scaled))
        
        # Asymmetric exponential barrier terms with different decay rates
        barriers = np.sum(2.0 * np.exp(-3.0 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**2 + 
                         1.5 * np.exp(-6.0 * np.abs(x_scaled)) * np.cos(8 * np.pi * x_scaled)**2)
        
        # Saddle point structure with asymmetric cubic and quartic terms
        saddle = np.sum(0.5 * x_scaled**4 - 2.0 * x_scaled**2 + 0.8 * x_scaled**3 + 0.3 * x_scaled**5)
        
        # Cross-dimensional coupling with asymmetric interaction weights
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * x_scaled[:-1]) * np.cos(6 * x_scaled[1:]) * 1.5)
        
        # Additional high-order polynomial for increased ruggedness
        high_order = np.sum(0.6 * x_scaled**9 - 0.7 * x_scaled**7 + 0.4 * x_scaled**6)
        
        # Logarithmic barrier component to create sharp gradients near boundaries
        log_barrier = np.sum(1.2 * np.log(1.0 + 5.0 * np.abs(x_scaled)) * np.sin(9 * np.pi * x_scaled)**2)
        
        # Combine all components with adjusted weights
        return 0.5 * quadratic + 2.0 * periodic + barriers + 0.3 * saddle + 0.3 * coupling + 0.15 * high_order + 0.2 * log_barrier