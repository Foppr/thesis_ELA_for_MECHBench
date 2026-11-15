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
            rbfs += np.exp(-0.1 * (x[i] - 2)**2) * np.sin(3 * x[i]) + \
                   np.exp(-0.1 * (x[i] + 2)**2) * np.cos(2 * x[i])
        
        # Asymmetric saddle point structure
        saddles = 0
        for i in range(self.dim):
            saddles += (x[i]**3 - 2 * x[i]**2 + x[i]) * np.sin(0.5 * x[i])
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.5 * (x[i]**2 + x[j]**2) * np.sin(0.3 * x[i] * x[j]) * \
                           np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Periodic interference with varying frequencies
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(5 * x[i]) * np.cos(4 * x[i]) * np.tan(0.2 * x[i])
        
        # Asymmetric exponential damping
        damping = 0
        for i in range(self.dim):
            damping += np.exp(-0.2 * np.abs(x[i])) * np.sin(0.1 * x[i]**3)
        
        # Hyperbolic tangent modulation
        tanh_mod = 0
        for i in range(self.dim):
            tanh_mod += np.tanh(x[i]) * np.cos(0.3 * x[i]**2)
        
        # Quadratic base with added sinusoidal perturbation
        base = np.sum(x**2) + 0.1 * np.sum(np.sin(2 * x)**2)
        
        return base + rbfs + saddles + coupling + periodic + damping + tanh_mod