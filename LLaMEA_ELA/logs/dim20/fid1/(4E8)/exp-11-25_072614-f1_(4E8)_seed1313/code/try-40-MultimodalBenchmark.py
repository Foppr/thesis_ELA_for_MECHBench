import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with modified exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-r / 3.0) * (1.0 + 0.7 * np.sin(r * 1.5))
        
        # Enhanced trigonometric interference terms
        trig_interference = np.sum(np.cos(4.0 * x) * np.sin(8.0 * x) * np.exp(-r / 4.0))
        
        # Additional chaotic component with shifted sine
        chaotic = np.sum(np.sin(x**2 + 1.0) * np.cos(x + 0.5))
        
        # Add polynomial radial term for increased complexity
        polynomial = 0.005 * r**4
        
        # Combine all components with modified weights
        return radial + 0.4 * trig_interference + 0.15 * chaotic + polynomial