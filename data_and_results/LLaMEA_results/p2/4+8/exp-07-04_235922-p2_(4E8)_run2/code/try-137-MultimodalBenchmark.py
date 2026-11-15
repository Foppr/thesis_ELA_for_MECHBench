import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components
        term1 = np.sum(x**2)
        term2 = 0.8 * np.sum(np.sin(7 * x) * np.cos(4 * x) * np.exp(-0.1 * np.abs(x)))
        term3 = 0.15 * np.sum(x**6 * np.sin(3 * x))
        term4 = 0.4 * np.sum(np.exp(-x**2) * np.sin(15 * x) * np.cos(5 * x))
        term5 = 0.08 * np.sum(np.abs(x) ** 4.2)
        term6 = 0.2 * np.sum(np.sin(x**3) * np.cos(x**2))
        
        # Add complex interaction terms between dimensions
        interaction = 0.03 * np.sum((x[:-1] - x[1:]) ** 3 * np.sin(7 * (x[:-1] + x[1:])))
        interaction += 0.01 * np.sum((x[:-2] - x[2:]) ** 2 * np.cos(4 * (x[:-2] + x[2:])))
        
        # Add a dynamic exponential barrier component
        barrier = 0.5 * np.sum(np.exp(-0.5 * (x - np.mean(x))**2) * np.sin(20 * x))
        
        # Add multi-scale sinusoidal modulation
        modulation = 0.3 * np.sum(np.sin(25 * x) * np.cos(10 * x) * np.exp(-0.05 * x**2))
        modulation += 0.2 * np.sum(np.sin(35 * x) * np.cos(15 * x) * np.exp(-0.02 * np.abs(x)))
        
        # Add higher-order coupling terms
        coupling = 0.1 * np.sum((x**3 - np.roll(x, 1)**3) * np.sin(5 * (x + np.roll(x, 1))))
        coupling += 0.05 * np.sum((x**4 - np.roll(x, 2)**4) * np.cos(3 * (x + np.roll(x, 2))))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + modulation + coupling
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result