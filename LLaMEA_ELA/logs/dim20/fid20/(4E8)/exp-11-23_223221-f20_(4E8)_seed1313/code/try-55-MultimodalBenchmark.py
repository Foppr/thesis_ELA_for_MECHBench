import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with high-degree terms for complexity
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Trigonometric components with varying frequencies and phase shifts
        trig1 = np.sum(np.sin(2.0 * x + np.pi/4) * np.cos(3.0 * x + np.pi/3))
        trig2 = np.sum(np.sin(5.0 * x + np.pi/6) * np.cos(7.0 * x + np.pi/2))
        trig3 = np.sum(np.sin(x**2) * np.cos(x**3))
        
        # Cross-dimensional interactions with exponential decay
        cross_interaction = np.sum(np.exp(-0.1 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Grid-based modulation with chaotic sine waves
        grid_modulation = np.prod(np.sin(0.5 * x) + 1.0) + 1.0
        chaotic_component = np.sum(np.sin(np.exp(x)) * grid_modulation)
        
        # Adaptive noise term that depends on the solution's position
        adaptive_noise = 0.05 * np.std(x) * np.random.rand()
        
        # Add a radial basis function component for multi-modal behavior
        rbf = np.sum(np.exp(-0.5 * (x - np.mean(x))**2))
        
        return polynomial + trig1 + trig2 + trig3 + cross_interaction + chaotic_component + adaptive_noise + rbf