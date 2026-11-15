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
        chaotic = np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled))
        
        # Exponential barrier terms with increased complexity and modified weights
        barriers = np.sum(2.2 * np.exp(-5 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled)**2)
        
        # Saddle point structure using mixed polynomial terms with enhanced cubic addition
        saddle = np.sum(x_scaled**4 - 2 * x_scaled**2 + 0.8 * x_scaled**3)
        
        # Add cross-dimensional coupling term with stronger interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(6 * np.pi * x_scaled[:-1]) * 0.9)
        
        # Additional high-frequency oscillation term for increased complexity
        oscillation = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(13 * np.pi * x_scaled))
        
        # Combine all components with optimized weights
        return 0.6 * quadratic + 2.5 * chaotic + barriers + 0.4 * saddle + 0.2 * coupling + 0.3 * oscillation