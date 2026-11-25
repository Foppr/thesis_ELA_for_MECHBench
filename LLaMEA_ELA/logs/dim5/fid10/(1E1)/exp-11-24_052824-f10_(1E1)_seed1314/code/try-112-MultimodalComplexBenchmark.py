import numpy as np

class MultimodalComplexBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        polynomial = np.sum(x**4 + 0.5 * x**3 + 2 * x**2 + 0.1 * x)
        
        # Trigonometric component with multiple frequencies
        trigonometric = np.sum(np.sin(2 * x) + 0.5 * np.sin(5 * x) + 0.3 * np.sin(10 * x))
        
        # Radial basis function component with varying centers and widths
        rbf = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                rbf += np.exp(-0.5 * ((x[i] - centers[i % len(centers)]) / (1.0 + 0.1 * i))**2)
        
        # Coupling terms between dimensions with varying interaction strengths
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += 0.3 * np.sin(0.5 * x[i]) * np.cos(0.7 * x[j]) * (1 + 0.2 * np.sin(x[i] + x[j]))
                
        # Sine-wave modulation with amplitude variation
        modulated = np.sum(np.sin(x) * np.exp(-0.1 * x**2) * (1 + 0.3 * np.cos(3 * x)))
        
        # High-frequency oscillation component
        high_freq = np.sum(np.sin(15 * x) + 0.7 * np.sin(25 * x) + 0.4 * np.sin(40 * x))
        
        # Exponential decay with sinusoidal perturbation
        decay = np.sum(np.exp(-0.3 * x**2) * (1 + 0.2 * np.sin(2 * x)))
        
        # Cross-term interaction with chaotic-like behavior
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2) * (1 + 0.1 * np.sin(x[i] - x[j]))
        
        # Combine all components with carefully tuned weights
        return (0.25 * polynomial + 
                0.3 * trigonometric + 
                0.15 * rbf + 
                0.2 * coupling + 
                0.1 * modulated + 
                0.1 * high_freq + 
                0.05 * decay + 
                0.05 * cross_interaction)