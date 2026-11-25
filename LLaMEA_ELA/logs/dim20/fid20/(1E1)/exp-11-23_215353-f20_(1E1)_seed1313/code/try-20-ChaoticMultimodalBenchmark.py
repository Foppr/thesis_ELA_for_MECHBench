import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay term with variable rate
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(0.5 * x)**2)
        
        # Multi-scale trigonometric modulation
        trig_term = np.sum(np.sin(3 * np.pi * x) * np.cos(7 * np.pi * x) + 
                          0.5 * np.sin(5 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Enhanced polynomial distortion with mixed degrees
        poly_term = np.sum((x**4 + 0.3 * x**3 - 0.4 * x**2 + 0.1 * x + 1.0)**2)
        
        # Chaotic component with combined exponential and sinusoidal effects
        chaotic_term = np.sum(np.sin(np.exp(0.5 * x)) * np.cos(x**2))
        
        # Additional harmonic modulation for increased complexity
        harm_term = np.sum(np.sin(0.1 * x) * np.exp(-x**2))
        
        # Combine all terms with optimized weights
        return 0.4 * exp_term + 0.3 * trig_term + 0.2 * poly_term + 0.08 * chaotic_term + 0.02 * harm_term + 1.5