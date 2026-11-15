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
        
        # Enhanced cross-dimensional coupling with exponential interaction
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.5 * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * \
                           np.sin(0.3 * x[i] * x[j]) * \
                           np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Increased trigonometric interference with higher frequency components
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(7 * x[i]) * np.cos(5 * x[i]) * np.tan(0.3 * x[i]) + \
                       np.cos(6 * x[i]) * np.sin(4 * x[i]) * np.exp(-0.02 * x[i]**2)
        
        # Modified exponential damping with asymmetric decay
        damping = 0
        for i in range(self.dim):
            damping += np.exp(-0.3 * np.abs(x[i])) * np.sin(0.15 * x[i]**3) * \
                       np.cos(0.2 * x[i])
        
        # Enhanced hyperbolic tangent modulation with polynomial scaling
        tanh_mod = 0
        for i in range(self.dim):
            tanh_mod += np.tanh(x[i]) * np.cos(0.3 * x[i]**2) * \
                       np.exp(-0.05 * x[i]**2)
        
        # Quadratic base with enhanced sinusoidal perturbation
        base = np.sum(x**2) + 0.15 * np.sum(np.sin(3 * x)**2) + \
               0.05 * np.sum(np.cos(2 * x)**2)
        
        # Additional chaotic component with fractional Brownian motion inspired terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(11 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.01 * x[i]**3) + \
                       np.cos(10 * x[i]) * np.sin(8 * x[i]) * np.tan(0.4 * x[i]) + \
                       np.sin(13 * x[i]) * np.cos(11 * x[i]) * np.exp(-0.005 * x[i]**4)
        
        # Add a global minimum perturbation term
        global_min_pert = 0.02 * np.sum(np.abs(x - 1.5)**4)
        
        return base + rbfs + saddles + coupling + periodic + damping + tanh_mod + chaotic + global_min_pert