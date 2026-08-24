import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive conditioning: each dimension has its own condition number
        condition_numbers = 10 ** np.linspace(0, 2, self.dim)
        
        # Chaotic component using logistic map-like behavior
        chaotic = np.zeros(self.dim)
        r = 3.95
        for i in range(self.dim):
            chaotic[i] = np.sin(r * x[i] * (1 - x[i])) if x[i] != 0 else 0
        
        # Harmonic oscillations with exponential decay
        oscillation = np.sum(np.exp(-0.1 * np.arange(1, self.dim + 1)) * 
                            np.sin(np.arange(1, self.dim + 1) * x) * 
                            np.cos(np.arange(1, self.dim + 1) * x))
        
        # Quadratic term with adaptive conditioning
        quadratic = np.sum(condition_numbers * x**2)
        
        # Exponentially decaying sinusoidal perturbations
        perturbations = np.sum(np.exp(-0.5 * np.arange(1, self.dim + 1)) * 
                              np.sin(2 * np.pi * np.arange(1, self.dim + 1) * x))
        
        # Nested global minima with varying depths
        minima_positions = [
            np.array([0.0] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim),
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim)
        ]
        
        # Penalty based on proximity to multiple global minima
        penalty = 0
        for pos in minima_positions:
            dist = np.sum((x - pos)**2)
            penalty += np.exp(-dist / 2.0) / (1 + dist)
        
        # Combine all components
        result = quadratic + oscillation + perturbations + 0.1 * np.sum(chaotic**2) - penalty
        
        # Add small random noise for robustness testing
        noise = 0.001 * np.random.random()
        
        return result + noise