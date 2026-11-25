import numpy as np

class MultimodalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Central polynomial attraction basin (quartic term for sharper minimum)
        basin = 0.05 * np.sum(x**4)
        
        # Sinusoidal oscillations with varying frequencies
        oscillation = np.sum(np.sin(2 * np.pi * x) ** 2 + 0.5 * np.sin(4 * np.pi * x) ** 2)
        
        # Cross-dimensional interaction terms with coupling strength
        cross_interaction = 0.3 * np.sum((x[:-1] - x[1:]) ** 2 * (1 + 0.1 * np.abs(x[:-1]) + 0.1 * np.abs(x[1:])))
        
        # Adaptive boundary repulsion based on distance from boundaries
        boundary_penalty = np.sum(10.0 * (5.0 - np.abs(x)) ** 2 * (np.abs(x) > 2.0))
        
        # Additional high-frequency oscillation with amplitude modulation
        high_freq = 0.4 * np.sum((1 + 0.3 * np.sin(15 * np.pi * x)) * np.sin(12 * np.pi * x) ** 2)
        
        # Add a small Gaussian noise component to increase problem difficulty
        noise = 0.01 * np.sum(np.random.normal(0, 1, len(x)) ** 2)
        
        return basin + oscillation + cross_interaction + boundary_penalty + high_freq + noise