import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-like interference terms with phase modulation
        interference = np.sum(np.sin(np.pi * x) * np.cos(2 * np.pi * x) * 
                             np.exp(-0.1 * x**2))
        
        # Saddle-point attractor components with varying curvature
        saddle = 0.5 * np.sum(x[:-1]**2 * x[1:]**2 - x[:-1]**3 * x[1:]**3)
        
        # Adaptive penalty landscape with dimensionality-dependent scaling
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i]**2 + 1.0) * np.exp(-0.5 * (x[i] / (1.0 + 0.1 * np.abs(x[i])))**2)
        
        # Rugged terrain with multi-scale oscillations
        rugged = np.sum(np.sin(10 * x) * np.cos(5 * x) * 
                       np.exp(-0.05 * np.abs(x)))
        
        # Coupled harmonic oscillators with nonlinear coupling
        harmonic = 0.3 * np.sum((x[:-1] - x[1:])**2 + 0.1 * (x[:-1] + x[1:])**4)
        
        # Adaptive conditioning based on position and dimensionality
        condition = 1.0 + 0.2 * np.sin(self.dim * 0.1) * np.mean(np.abs(x))
        
        # Quadratic basin with non-uniform weights
        quadratic = condition * np.sum(x**2 * (1.0 + 0.05 * x**4))
        
        # Noise term with spatial correlation
        noise = 0.02 * np.random.rand() * np.sum(np.sin(3 * x) * np.cos(7 * x))
        
        # Combined function value
        return quadratic + interference + saddle + penalty + rugged + harmonic + noise