import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial and trigonometric components
        term1 = np.sum(x**2)
        term2 = 0.9 * np.sum(np.sin(8 * x) * np.cos(5 * x) * np.exp(-0.15 * np.abs(x)))
        term3 = 0.18 * np.sum(x**7 * np.sin(4 * x))
        term4 = 0.45 * np.sum(np.exp(-x**2) * np.sin(18 * x) * np.cos(6 * x))
        term5 = 0.1 * np.sum(np.abs(x) ** 4.5)
        term6 = 0.25 * np.sum(np.sin(x**4) * np.cos(x**3))
        
        # Enhanced interaction terms between dimensions
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 4 * np.sin(8 * (x[:-1] + x[1:])))
        interaction += 0.015 * np.sum((x[:-2] - x[2:]) ** 3 * np.cos(5 * (x[:-2] + x[2:])))
        
        # Modified exponential barrier component with dynamic conditioning
        barrier = 0.55 * np.sum(np.exp(-0.6 * (x - np.mean(x))**2) * np.sin(25 * x))
        
        # Multi-scale sinusoidal modulation with enhanced frequency components
        modulation = 0.35 * np.sum(np.sin(30 * x) * np.cos(12 * x) * np.exp(-0.06 * x**2))
        modulation += 0.25 * np.sum(np.sin(40 * x) * np.cos(18 * x) * np.exp(-0.03 * np.abs(x)))
        
        # Higher-order coupling terms with chaotic behavior
        coupling = 0.13 * np.sum((x**4 - np.roll(x, 1)**4) * np.sin(6 * (x + np.roll(x, 1))))
        coupling += 0.06 * np.sum((x**5 - np.roll(x, 2)**5) * np.cos(4 * (x + np.roll(x, 2))))
        
        # Additional chaotic coupling between non-adjacent dimensions
        chaotic_coupling = 0.03 * np.sum((x[:-3] - x[3:]) ** 2 * np.sin(10 * (x[:-3] + x[3:])))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + modulation + coupling + chaotic_coupling
        
        # Add controlled noise for increased difficulty
        result += 0.0015 * np.random.random()
        
        return result