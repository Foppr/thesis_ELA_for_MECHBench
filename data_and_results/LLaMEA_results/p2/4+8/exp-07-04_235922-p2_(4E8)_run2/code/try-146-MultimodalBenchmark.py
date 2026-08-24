import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with modified coefficients
        term1 = np.sum(x**2)
        term2 = 0.9 * np.sum(np.sin(7 * x) * np.cos(4 * x) * np.exp(-0.1 * np.abs(x)))
        term3 = 0.18 * np.sum(x**6 * np.sin(3 * x))
        term4 = 0.45 * np.sum(np.exp(-x**2) * np.sin(15 * x) * np.cos(5 * x))
        term5 = 0.09 * np.sum(np.abs(x) ** 4.2)
        term6 = 0.23 * np.sum(np.sin(x**3) * np.cos(x**2))
        
        # Add complex interaction terms between dimensions with modified coefficients
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 3 * np.sin(7 * (x[:-1] + x[1:])))
        interaction += 0.015 * np.sum((x[:-2] - x[2:]) ** 2 * np.cos(4 * (x[:-2] + x[2:])))
        
        # Add a dynamic exponential barrier component with altered parameters
        barrier = 0.6 * np.sum(np.exp(-0.35 * (x - np.mean(x))**2) * np.sin(20 * x))
        
        # Add multi-scale sinusoidal modulation with modified frequencies and coefficients
        modulation = 0.35 * np.sum(np.sin(25 * x) * np.cos(10 * x) * np.exp(-0.05 * x**2))
        modulation += 0.23 * np.sum(np.sin(35 * x) * np.cos(15 * x) * np.exp(-0.02 * np.abs(x)))
        
        # Add higher-order coupling terms with modified coefficients
        coupling = 0.12 * np.sum((x**3 - np.roll(x, 1)**3) * np.sin(5 * (x + np.roll(x, 1))))
        coupling += 0.06 * np.sum((x**4 - np.roll(x, 2)**4) * np.cos(3 * (x + np.roll(x, 2))))
        
        # Add a new component with chaotic coupling and additional noise
        chaotic = 0.08 * np.sum(np.sin(12 * x) * np.cos(8 * x) * np.exp(-0.03 * x**2))
        chaotic += 0.04 * np.sum(np.sin(18 * x) * np.cos(9 * x) * np.exp(-0.04 * np.abs(x)))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + modulation + coupling + chaotic
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result