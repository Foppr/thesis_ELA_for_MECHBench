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
        
        # Exponential barrier terms with modified weights and enhanced ruggedness
        barriers = np.sum(2.0 * np.exp(-5 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled)**2)
        
        # Saddle point structure using mixed polynomial terms
        saddle = np.sum(x_scaled**4 - 2.5 * x_scaled**2)
        
        # Enhanced cross-dimensional coupling with stronger interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(6 * np.pi * x_scaled[:-1]) * np.cos(3 * np.pi * x_scaled[1:]))
        
        # Additional high-frequency oscillation term
        high_freq = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled))
        
        # Combine all components with optimized weights
        return 0.6 * quadratic + 2.5 * chaotic + barriers + 0.4 * saddle + 0.2 * coupling + 0.1 * high_freq