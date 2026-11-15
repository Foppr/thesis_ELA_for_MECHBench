import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similar components with varying scales
        term1 = np.sum(x**2)
        term2 = 0.5 * np.sum(np.sin(13 * x) * np.cos(9 * x))
        term3 = 0.3 * np.sum(np.sin(2 * x) * np.cos(5 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Quantum-inspired interference patterns
        quantum = 0.2 * np.sum(np.sin(8 * x) * np.cos(12 * x) * np.sin(4 * x))
        
        # Dynamic saddle-point landscape with varying curvature
        saddle = 0.1 * np.sum(x**4 * np.cos(6 * x) * np.sin(3 * x))
        
        # Multi-scale fractal component with diminishing returns
        fractal = 0.15 * np.sum(np.sin(2**np.arange(1, self.dim + 1) * x) / np.arange(1, self.dim + 1))
        
        # Cross-dimensional coupling with dynamic weights
        coupling = 0.08 * np.sum((x[:-1] * x[1:] * np.sin(5 * (x[:-1]**2 + x[1:]**2))) / (1 + np.abs(x[:-1] - x[1:])))
        
        # Adaptive exponential barriers with quantum-like tunneling effects
        barrier = 0.25 * np.sum(np.exp(-0.5 * np.abs(x)) * np.cos(10 * x) * np.sin(2 * x))
        
        # Sharp regional transitions to create flat and steep areas
        transitions = 0.1 * np.sum(np.abs(x)**3.7 * np.sin(7 * x))
        
        result = term1 + term2 + term3 + quantum + saddle + fractal + coupling + barrier + transitions
        
        # Add small noise for robustness testing
        result += 0.001 * np.random.random()
        
        return result