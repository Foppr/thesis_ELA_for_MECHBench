import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis function component with logarithmic coupling
        rbfs = 0
        for i in range(self.dim):
            rbfs += np.log(1 + 0.1 * (x[i] - 2)**2) * np.sin(3 * x[i]) + \
                   np.log(1 + 0.1 * (x[i] + 2)**2) * np.cos(2 * x[i])
        
        # Asymmetric saddle point structure with modified polynomial
        saddles = 0
        for i in range(self.dim):
            saddles += (x[i]**3 - 2 * x[i]**2 + x[i]) * np.sin(0.5 * x[i]) * \
                       np.exp(-0.1 * np.abs(x[i]))
        
        # Cross-dimensional coupling with enhanced trigonometric interference
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.5 * (x[i]**2 + x[j]**2) * np.sin(0.3 * x[i] * x[j]) * \
                           np.exp(-0.05 * (x[i] - x[j])**2) * \
                           (1 + 0.2 * np.sin(0.4 * (x[i] + x[j])))
        
        # Increased trigonometric interference with varying frequencies
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(5 * x[i]) * np.cos(4 * x[i]) * np.tan(0.2 * x[i]) * \
                       np.exp(-0.02 * x[i]**2)
        
        # Modified exponential damping with chaotic modulation
        damping = 0
        for i in range(self.dim):
            damping += np.exp(-0.2 * np.abs(x[i])) * np.sin(0.1 * x[i]**3) * \
                      (1 + 0.1 * np.sin(0.5 * x[i]))
        
        # Hyperbolic tangent modulation with additional chaotic component
        tanh_mod = 0
        for i in range(self.dim):
            tanh_mod += np.tanh(x[i]) * np.cos(0.3 * x[i]**2) * \
                       (1 + 0.15 * np.sin(0.7 * x[i]))
        
        # Quadratic base with enhanced sinusoidal perturbation
        base = np.sum(x**2) + 0.1 * np.sum(np.sin(2 * x)**2) + \
               0.05 * np.sum(np.sin(0.5 * x)**4)
        
        # Add chaotic coupling between all dimensions
        chaotic_coupling = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    chaotic_coupling += 0.01 * np.sin(x[i] * x[j]) * \
                                       np.exp(-0.01 * (x[i] - x[j])**2)
        
        return base + rbfs + saddles + coupling + periodic + damping + tanh_mod + chaotic_coupling