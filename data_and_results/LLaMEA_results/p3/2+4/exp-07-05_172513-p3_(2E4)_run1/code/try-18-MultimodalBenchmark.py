import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced quadratic basin term with conditionally weighted dimensions
        quadratic = np.sum(x_scaled**2 * (1 + 0.5 * np.sin(5 * x_scaled)))
        
        # Chaotic sinusoidal component with dynamic frequency modulation
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Complex exponential barrier with multi-scale decay and oscillation
        barriers = np.sum(np.exp(-3 * np.abs(x_scaled)) * (np.sin(5 * np.pi * x_scaled)**2 + 0.3 * np.cos(9 * np.pi * x_scaled)**2))
        
        # Enhanced saddle point structure with non-separable mixed terms
        saddle = np.sum(x_scaled**6 - 3 * x_scaled**4 + 2 * x_scaled**2)
        
        # Additional high-frequency oscillation component for increased ruggedness
        oscillation = 0.5 * np.sum(np.sin(20 * x_scaled) * np.cos(17 * x_scaled) * np.exp(-0.3 * np.abs(x_scaled)))
        
        # Combine all components with varying weights
        return 0.3 * quadratic + 2.5 * chaotic + 2.0 * barriers + 0.4 * saddle + 0.7 * oscillation