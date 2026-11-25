import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Add multiple overlapping quadratic wells with different centers
        wells = 0.0
        centers = np.linspace(-3.0, 3.0, 7)
        for center in centers:
            wells += 0.5 * np.sum((x - center)**2)
        
        # Add periodic modulation to create oscillating landscape
        f2 = 0.3 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Add a challenging deceptive term with multiple local minima
        f3 = 0.1 * np.sum(np.sin(8.0 * x) * np.exp(-0.5 * x**2))
        
        # Combine all terms with different weights to create complexity
        return f1 + 0.5 * wells + f2 + f3