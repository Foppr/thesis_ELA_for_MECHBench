import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis function component with logarithmic modulation
        rbfs = 0
        for i in range(self.dim):
            rbfs += np.log(1 + 0.1 * (x[i] - 2)**2) * np.sin(4 * x[i]) + \
                   np.log(1 + 0.1 * (x[i] + 2)**2) * np.cos(3 * x[i])
        
        # Asymmetric saddle point structure with cubic modulation
        saddles = 0
        for i in range(self.dim):
            saddles += (x[i]**3 - 3 * x[i]**2 + 2 * x[i]) * np.sin(0.7 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with hyperbolic interactions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.3 * np.tanh(x[i] * x[j]) * np.sin(0.5 * (x[i]**2 + x[j]**2)) * \
                           np.exp(-0.03 * (x[i] - x[j])**2)
        
        # Enhanced periodic interference with chaotic frequency modulation
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(6 * x[i]) * np.cos(5 * x[i]) * np.tan(0.3 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Modified exponential damping with asymmetric decay
        damping = 0
        for i in range(self.dim):
            damping += np.exp(-0.3 * np.abs(x[i])) * np.sin(0.2 * x[i]**3) * np.cos(0.1 * x[i])
        
        # Hyperbolic tangent modulation with polynomial enhancement
        tanh_mod = 0
        for i in range(self.dim):
            tanh_mod += np.tanh(x[i]) * np.cos(0.4 * x[i]**2) * np.exp(-0.02 * x[i]**2)
        
        # Quadratic base with enhanced sinusoidal perturbation and chaotic noise
        base = np.sum(x**2) + 0.2 * np.sum(np.sin(3 * x)**2) + 0.05 * np.sum(np.random.randn(self.dim) * x)
        
        return base + rbfs + saddles + coupling + periodic + damping + tanh_mod