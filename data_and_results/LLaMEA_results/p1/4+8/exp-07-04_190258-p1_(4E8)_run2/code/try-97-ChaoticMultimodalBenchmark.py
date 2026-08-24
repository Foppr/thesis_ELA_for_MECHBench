import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Convex quadratic base
        quadratic = np.sum(x**2)
        
        # Periodic peaks with varying frequencies
        periodic = 0
        for i in range(self.dim):
            periodic += 5 * np.sin(2 * np.pi * x[i]) * np.cos(0.5 * np.pi * x[i])
        
        # Gaussian valleys with adaptive width
        gaussian = 0
        for i in range(self.dim):
            gaussian += -np.exp(-0.5 * (x[i] / 1.5)**2)
        
        # Cross-dimensional interaction terms
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.1 * (x[i]**2 + x[j]**2) * np.sin(0.3 * x[i] * x[j])
        
        # Saddle point structure with higher-order terms
        saddle = 0
        for i in range(self.dim):
            saddle += x[i]**4 - 2 * x[i]**2
        
        # Chaotic modulation using logistic map-like behavior
        chaotic = 0
        r = 3.9
        for i in range(self.dim):
            chaotic += np.sin(r * x[i] * (1 - x[i])) * np.cos(0.2 * x[i]**3)
        
        # Logarithmic coupling between dimensions
        log_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                log_coupling += 0.05 * np.log(1 + np.abs(x[i] * x[j])) * np.sin(0.1 * (x[i]**2 + x[j]**2))
        
        # Trigonometric interference with multiple harmonics
        interference = 0
        for i in range(self.dim):
            interference += 0.2 * np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.tan(0.2 * x[i])
        
        return quadratic + periodic + gaussian + cross + saddle + chaotic + log_coupling + interference