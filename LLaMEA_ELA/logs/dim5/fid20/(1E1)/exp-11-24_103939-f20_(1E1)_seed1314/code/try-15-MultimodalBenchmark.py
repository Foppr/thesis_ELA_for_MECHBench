import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Highly multimodal terms with multiple local minima
        f2 = 0.5 * np.sum(np.sin(12 * np.pi * x_normalized)**4 + 
                         np.cos(10 * np.pi * x_normalized)**4)
        
        # Additional complex oscillatory term with periodic global minima
        f3 = 0.2 * np.sum(np.sin(18 * np.pi * x_normalized) * 
                         np.cos(15 * np.pi * x_normalized) + 
                         np.sin(9 * np.pi * x_normalized)**3)
        
        # Add a periodic pattern that creates multiple global minima
        f4 = 0.3 * np.sum(np.cos(8 * np.pi * x_normalized) + 
                         np.sin(11 * np.pi * x_normalized))**2
        
        # Introduce a new high-frequency component to increase complexity
        f5 = 0.15 * np.sum(np.sin(20 * np.pi * x_normalized) * 
                          np.cos(17 * np.pi * x_normalized) * 
                          np.sin(13 * np.pi * x_normalized))
        
        # Add a polynomial modulation to the landscape
        f6 = 0.25 * np.sum((x_normalized**4 + x_normalized**3 - 2*x_normalized**2)**2)
        
        # Introduce a new chaotic component with exponential modulation
        f7 = 0.1 * np.sum(np.exp(-5 * np.abs(x_normalized)) * 
                         np.sin(25 * np.pi * x_normalized)**2)
        
        # Add a cross-term interaction between dimensions to increase complexity
        f8 = 0.18 * np.sum(np.sin(7 * np.pi * x_normalized) * 
                          np.cos(6 * np.pi * x_normalized) * 
                          np.sin(4 * np.pi * x_normalized))
        
        # Introduce a new periodic term with varying frequency
        f9 = 0.22 * np.sum(np.cos(14 * np.pi * x_normalized)**3 + 
                         np.sin(16 * np.pi * x_normalized)**3)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9