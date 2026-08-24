import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with increased complexity
        term1 = np.sum(x**2)
        term2 = 1.2 * np.sum(np.sin(9 * x) * np.cos(5 * x) * np.exp(-0.15 * np.abs(x)))
        term3 = 0.25 * np.sum(x**7 * np.sin(4 * x))
        term4 = 0.6 * np.sum(np.exp(-x**2) * np.sin(20 * x) * np.cos(8 * x))
        term5 = 0.12 * np.sum(np.abs(x) ** 5.0)
        term6 = 0.3 * np.sum(np.sin(x**4) * np.cos(x**3))
        
        # Add complex interaction terms between dimensions with higher order coupling
        interaction = 0.05 * np.sum((x[:-1] - x[1:]) ** 4 * np.sin(9 * (x[:-1] + x[1:])))
        interaction += 0.02 * np.sum((x[:-2] - x[2:]) ** 3 * np.cos(6 * (x[:-2] + x[2:])))
        interaction += 0.015 * np.sum((x[:-3] - x[3:]) ** 2 * np.sin(8 * (x[:-3] + x[3:])))
        
        # Add a stronger dynamic exponential barrier component
        barrier = 0.7 * np.sum(np.exp(-0.3 * (x - np.mean(x))**2) * np.sin(25 * x))
        barrier += 0.25 * np.sum(np.exp(-0.1 * (x - np.median(x))**2) * np.cos(15 * x))
        
        # Add intensified multi-scale sinusoidal modulation
        modulation = 0.45 * np.sum(np.sin(30 * x) * np.cos(12 * x) * np.exp(-0.08 * x**2))
        modulation += 0.3 * np.sum(np.sin(40 * x) * np.cos(18 * x) * np.exp(-0.04 * np.abs(x)))
        modulation += 0.15 * np.sum(np.sin(50 * x) * np.cos(20 * x) * np.exp(-0.03 * x**3))
        
        # Add stronger higher-order coupling terms
        coupling = 0.15 * np.sum((x**4 - np.roll(x, 1)**4) * np.sin(7 * (x + np.roll(x, 1))))
        coupling += 0.08 * np.sum((x**5 - np.roll(x, 2)**5) * np.cos(4 * (x + np.roll(x, 2))))
        coupling += 0.04 * np.sum((x**6 - np.roll(x, 3)**6) * np.sin(6 * (x + np.roll(x, 3))))
        
        # Add a more complex adaptive component
        adaptive = 0.1 * np.sum(np.sin(3 * x) * np.cos(2 * x) * np.exp(-0.2 * np.abs(x)) * np.log(1 + np.abs(x)))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + modulation + coupling + adaptive
        
        # Add a larger noise term to make it more challenging
        result += 0.005 * np.random.random()
        
        return result