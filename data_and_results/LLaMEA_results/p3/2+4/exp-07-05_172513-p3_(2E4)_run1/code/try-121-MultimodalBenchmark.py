import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic base term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        periodic = np.sum(2.0 * np.sin(10 * x_scaled) + 1.5 * np.cos(7 * x_scaled) + 0.8 * np.sin(15 * x_scaled))
        
        # Asymmetric exponential barrier terms
        barriers = np.sum(2.0 * np.exp(-3.0 * np.abs(x_scaled)) * np.sin(6 * np.pi * x_scaled)**2 + 
                         1.2 * np.exp(-5.0 * np.abs(x_scaled)) * np.cos(9 * np.pi * x_scaled)**2)
        
        # Saddle point structure with asymmetric cubic terms
        saddle = np.sum(0.5 * x_scaled**3 - 1.5 * x_scaled**2 + 0.8 * x_scaled**4)
        
        # Cross-dimensional coupling with asymmetric interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(5 * np.pi * x_scaled[:-1]) * 2.0 + 
                         x_scaled[:-1] * x_scaled[1:] * np.cos(3 * np.pi * x_scaled[1:]) * 1.5)
        
        # High-order polynomial with mixed signs for ruggedness
        high_order = np.sum(0.3 * x_scaled**8 - 0.7 * x_scaled**6 + 0.4 * x_scaled**5 - 0.2 * x_scaled**3)
        
        # Additional chaotic component with logistic map-like behavior
        logistic = np.sum(3.5 * x_scaled * (1 - x_scaled**2))
        
        # Combine all components with adjusted weights
        return 0.3 * quadratic + 1.8 * periodic + barriers + 0.4 * saddle + 0.25 * coupling + 0.1 * high_order + 0.08 * logistic