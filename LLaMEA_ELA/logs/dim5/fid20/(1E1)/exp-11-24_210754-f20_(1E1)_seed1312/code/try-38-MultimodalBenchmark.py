import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced high-frequency sinusoidal oscillations with exponential growth and phase modulation
        f2 = np.sum(np.sin(20.0 * np.exp(0.8 * np.abs(x)) * x + np.sin(x)))
        
        # Polynomial corruption with higher-degree terms and adaptive coefficients
        f3 = 0.01 * np.sum(0.8 * x**8 + 0.5 * x**7 + 0.3 * x**6 + 0.2 * x**5 + 0.1 * x**4)
        
        # Saddle point structure with stronger interaction and multi-scale components
        f4 = 0.2 * np.sum(np.cos(4.0 * x) * np.sin(0.8 * x) * np.exp(-0.15 * np.abs(x)) + 
                          np.sin(2.0 * x) * np.cos(0.5 * x) * np.exp(-0.2 * x**2))
        
        # Chaotic component with combined trigonometric and logarithmic mappings
        f5 = 0.08 * np.sum(np.sin(np.exp(x) + np.cos(x)) * np.cos(np.log(np.abs(x) + 1e-8) + np.sin(x)))
        
        # Additional harmonic interference term for increased complexity
        f6 = 0.03 * np.sum(np.sin(10.0 * x) * np.cos(5.0 * x) * np.exp(-0.05 * x**2))
        
        # Combine all terms with optimized weights
        return f1 + f2 + f3 + f4 + f5 + f6