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
        
        # Enhanced exponential barrier terms with increased complexity
        barriers = np.sum(2.0 * np.exp(-5 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled)**2)
        
        # Saddle point structure using mixed polynomial terms with cubic and quartic additions
        saddle = np.sum(x_scaled**4 - 2 * x_scaled**2 + 0.7 * x_scaled**3 + 0.2 * x_scaled**4)
        
        # Enhanced cross-dimensional coupling term with stronger interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(6 * np.pi * x_scaled[:-1]) * 0.8)
        
        # Additional cubic polynomial coupling for increased complexity
        cubic_coupling = np.sum(x_scaled**3 * np.sin(3 * np.pi * x_scaled))
        
        # Combine all components with adjusted weights
        return 0.6 * quadratic + 2.5 * chaotic + barriers + 0.4 * saddle + 0.2 * coupling + 0.15 * cubic_coupling