import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with modified exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-r / 2.5) * (1.0 + 0.8 * np.sin(r * 1.2))
        
        # Enhanced trigonometric interference terms
        trig_interference = np.sum(np.cos(3.5 * x) * np.sin(7.0 * x) * np.exp(-r / 3.5))
        
        # Additional chaotic component with shifted sine
        chaotic = np.sum(np.sin(x**2 + 0.8) * np.cos(x + 0.3))
        
        # Add polynomial radial term for increased complexity
        polynomial = 0.007 * r**5
        
        # Add cross-terms for higher interaction complexity
        cross_terms = 0.02 * np.sum(x[:-1] * x[1:] * np.sin(r))
        
        # Combine all components with modified weights
        return radial + 0.35 * trig_interference + 0.2 * chaotic + polynomial + cross_terms