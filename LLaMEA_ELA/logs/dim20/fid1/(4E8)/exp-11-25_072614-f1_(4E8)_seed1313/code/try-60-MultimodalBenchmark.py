import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with modified exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-r / 2.0) * (1.0 + 0.9 * np.sin(r * 1.5))
        
        # Enhanced trigonometric interference terms with altered frequencies
        trig_interference = np.sum(np.cos(4.0 * x) * np.sin(6.5 * x) * np.exp(-r / 3.0))
        
        # Additional chaotic component with modified sine shift
        chaotic = np.sum(np.sin(x**2 + 0.9) * np.cos(x + 0.4))
        
        # Add polynomial radial term with increased complexity
        polynomial = 0.008 * r**5
        
        # Add enhanced cross-terms for higher interaction complexity
        cross_terms = 0.03 * np.sum(x[:-1] * x[1:] * np.sin(r * 0.8))
        
        # Combine all components with modified weights
        return radial + 0.4 * trig_interference + 0.25 * chaotic + polynomial + cross_terms