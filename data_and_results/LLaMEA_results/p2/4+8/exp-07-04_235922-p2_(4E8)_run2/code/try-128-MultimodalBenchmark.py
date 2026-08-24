import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with modified coefficients
        term1 = np.sum(x**2)
        term2 = 0.9 * np.sum(np.sin(8 * x) * np.cos(3 * x) * np.exp(-0.15 * np.abs(x)))
        term3 = 0.2 * np.sum(x**6 * np.sin(4 * x))
        term4 = 0.35 * np.sum(np.exp(-x**2) * np.sin(18 * x) * np.cos(6 * x))
        term5 = 0.1 * np.sum(np.abs(x) ** 4.5)
        term6 = 0.25 * np.sum(np.sin(x**3) * np.cos(x**2))
        
        # Improved interaction terms between dimensions
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 3 * np.sin(8 * (x[:-1] + x[1:])))
        interaction += 0.02 * np.sum((x[:-2] - x[2:]) ** 2 * np.cos(5 * (x[:-2] + x[2:])))
        
        # Refined exponential barrier component
        barrier = 0.6 * np.sum(np.exp(-0.4 * (x - np.mean(x))**2) * np.sin(25 * x))
        
        # Enhanced multi-scale sinusoidal modulation
        modulation = 0.35 * np.sum(np.sin(30 * x) * np.cos(12 * x) * np.exp(-0.06 * x**2))
        modulation += 0.25 * np.sum(np.sin(40 * x) * np.cos(18 * x) * np.exp(-0.03 * np.abs(x)))
        
        # Modified higher-order coupling terms
        coupling = 0.15 * np.sum((x**3 - np.roll(x, 1)**3) * np.sin(6 * (x + np.roll(x, 1))))
        coupling += 0.08 * np.sum((x**4 - np.roll(x, 2)**4) * np.cos(4 * (x + np.roll(x, 2))))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + modulation + coupling
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result