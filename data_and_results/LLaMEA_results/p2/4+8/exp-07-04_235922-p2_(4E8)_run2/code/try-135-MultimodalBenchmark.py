import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with modified coefficients
        term1 = np.sum(x**2)
        term2 = 0.92 * np.sum(np.sin(8 * x) * np.cos(3 * x) * np.exp(-0.12 * np.abs(x)))
        term3 = 0.18 * np.sum(x**6 * np.sin(3.5 * x))
        term4 = 0.45 * np.sum(np.exp(-x**2) * np.sin(16 * x) * np.cos(4.5 * x))
        term5 = 0.09 * np.sum(np.abs(x) ** 4.5)
        term6 = 0.23 * np.sum(np.sin(x**3.5) * np.cos(x**1.8))
        
        # Add complex interaction terms between dimensions with modified coefficients
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 3.5 * np.sin(7.5 * (x[:-1] + x[1:])))
        interaction += 0.015 * np.sum((x[:-2] - x[2:]) ** 2.5 * np.cos(4.2 * (x[:-2] + x[2:])))
        
        # Add a dynamic exponential barrier component with altered parameters
        barrier = 0.58 * np.sum(np.exp(-0.42 * (x - np.mean(x))**2) * np.sin(21 * x))
        
        # Add multi-scale sinusoidal modulation with modified frequencies and coefficients
        modulation = 0.35 * np.sum(np.sin(26 * x) * np.cos(10.5 * x) * np.exp(-0.055 * x**2))
        modulation += 0.23 * np.sum(np.sin(36 * x) * np.cos(15.5 * x) * np.exp(-0.022 * np.abs(x)))
        
        # Add higher-order coupling terms with modified coefficients
        coupling = 0.12 * np.sum((x**3.2 - np.roll(x, 1)**3.2) * np.sin(5.2 * (x + np.roll(x, 1))))
        coupling += 0.06 * np.sum((x**4.1 - np.roll(x, 2)**4.1) * np.cos(3.1 * (x + np.roll(x, 2))))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + modulation + coupling
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result