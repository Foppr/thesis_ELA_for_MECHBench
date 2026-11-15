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
            rbfs += np.log(1 + 0.15 * (x[i] - 2)**2) * np.sin(4.5 * x[i]) + \
                   np.log(1 + 0.15 * (x[i] + 2)**2) * np.cos(3.5 * x[i])
        
        # Asymmetric saddle point structure with cubic modulation
        saddles = 0
        for i in range(self.dim):
            saddles += (x[i]**3 - 3.2 * x[i]**2 + 2.1 * x[i]) * np.sin(0.75 * x[i]) * np.exp(-0.12 * x[i]**2)
        
        # Cross-dimensional coupling with hyperbolic interactions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.35 * np.tanh(x[i] * x[j]) * np.sin(0.55 * (x[i]**2 + x[j]**2)) * \
                           np.exp(-0.035 * (x[i] - x[j])**2)
        
        # Enhanced periodic interference with chaotic frequency modulation
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(6.5 * x[i]) * np.cos(5.5 * x[i]) * np.tan(0.35 * x[i]) * np.exp(-0.055 * x[i]**2)
        
        # Modified exponential damping with asymmetric decay
        damping = 0
        for i in range(self.dim):
            damping += np.exp(-0.35 * np.abs(x[i])) * np.sin(0.25 * x[i]**3) * np.cos(0.15 * x[i])
        
        # Hyperbolic tangent modulation with polynomial enhancement
        tanh_mod = 0
        for i in range(self.dim):
            tanh_mod += np.tanh(x[i]) * np.cos(0.45 * x[i]**2) * np.exp(-0.025 * x[i]**2)
        
        # Quadratic base with enhanced sinusoidal perturbation and chaotic noise
        base = np.sum(x**2) + 0.25 * np.sum(np.sin(3.5 * x)**2) + 0.055 * np.sum(np.random.randn(self.dim) * x)
        
        return base + rbfs + saddles + coupling + periodic + damping + tanh_mod