import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with periodic modulation
        rbfs = 0
        for i in range(self.dim):
            rbfs += 0.8 * np.exp(-0.15 * (x[i] - 2)**2) * np.sin(3.5 * x[i]) + \
                   1.2 * np.exp(-0.08 * (x[i] + 2)**2) * np.cos(1.8 * x[i])
        
        # Asymmetric saddle point structure
        saddles = 0
        for i in range(self.dim):
            saddles += (x[i]**3 - 1.8 * x[i]**2 + 0.8 * x[i]) * np.sin(0.4 * x[i])
        
        # Cross-dimensional coupling with polynomial interactions (slightly modified)
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.3 * (x[i]**2 + x[j]**2) * np.sin(0.4 * x[i] * x[j]) * \
                           np.exp(-0.03 * (x[i] - x[j])**2)
        
        # Periodic interference with varying frequencies
        periodic = 0
        for i in range(self.dim):
            periodic += 0.7 * np.sin(4.5 * x[i]) * np.cos(3.8 * x[i]) * np.tan(0.25 * x[i])
        
        # Asymmetric exponential damping (modified)
        damping = 0
        for i in range(self.dim):
            damping += 0.8 * np.exp(-0.25 * np.abs(x[i])) * np.sin(0.12 * x[i]**3)
        
        # Hyperbolic tangent modulation
        tanh_mod = 0
        for i in range(self.dim):
            tanh_mod += np.tanh(x[i]) * np.cos(0.35 * x[i]**2)
        
        # Quadratic base with added sinusoidal perturbation
        base = np.sum(x**2) + 0.12 * np.sum(np.sin(2.2 * x)**2)
        
        return base + rbfs + saddles + coupling + periodic + damping + tanh_mod