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
        
        # Enhanced exponential barrier terms with sharper transitions
        barriers = np.sum(np.exp(-7 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled)**2)
        
        # Modified saddle point structure with higher-order polynomial terms
        saddle = np.sum(x_scaled**6 - 3 * x_scaled**4 + 2 * x_scaled**2)
        
        # Additional ridge structure for increased complexity
        ridges = np.sum(np.cos(5 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Combine all components with adjusted weights
        return 0.3 * quadratic + 2.5 * chaotic + 2.0 * barriers + 0.2 * saddle + 0.8 * ridges