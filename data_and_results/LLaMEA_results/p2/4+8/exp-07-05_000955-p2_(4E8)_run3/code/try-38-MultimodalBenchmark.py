import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for conditioning
        f1 = np.sum(x**2)
        
        # Enhanced multimodal component with multiple frequencies
        f2 = 0.2 * np.sum(np.sin(10.0 * x) * np.cos(5.0 * x))
        
        # Chaotic sine-wave interaction for increased complexity
        f3 = 0.15 * np.sum(np.sin(15.0 * x) * np.sin(7.0 * x) * np.cos(3.0 * x))
        
        # Radial gradient component to guide convergence
        f4 = 0.05 * np.sum(x**4)
        
        # Adaptive scaling term to increase nonlinearity
        f5 = 0.1 * np.sum(np.sin(20.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Penalty term for large values to encourage convergence to origin
        f6 = 0.02 * np.sum(np.abs(x)**1.5)
        
        return f1 + f2 + f3 + f4 + f5 + f6