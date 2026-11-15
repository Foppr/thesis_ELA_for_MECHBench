import numpy as np

class ScalableChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with global minimum at origin
        polynomial = np.sum(x**4) / 4.0
        
        # Trigonometric modulation with multiple local minima
        trigonometric = 0
        for i in range(self.dim):
            trigonometric += np.sin(3 * x[i]) * np.cos(2 * x[i]) + np.sin(5 * x[i])
        
        # Exponential decay component with varying rates
        exponential = 0
        for i in range(self.dim):
            exponential += np.exp(-0.1 * np.abs(x[i])) * np.sin(0.5 * x[i]**2)
        
        # Cross-dimensional coupling with interaction terms
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.01 * (x[i]**2 + x[j]**2) * np.sin(0.3 * x[i] * x[j])
        
        # Chaotic component with sensitive dependence on initial conditions
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi / 2.0) * np.cos(x[i] * np.pi / 3.0) * \
                      np.exp(-0.05 * x[i]**2) * np.sin(0.1 * np.sum(x**2))
        
        # Gaussian noise-like perturbation
        noise = 0.01 * np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        # Combine all components
        return polynomial + trigonometric + exponential + coupling + chaotic + noise