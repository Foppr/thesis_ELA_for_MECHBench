import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic with chaotic sine modulation
        base_quad = np.sum(x_norm**2 * (1 + 0.5 * np.sin(10 * x_norm) * np.cos(7 * x_norm)))
        
        # Radial basis function with adaptive weights and chaotic perturbations
        rbf = 0.0
        for i in range(self.dim):
            rbf += np.exp(-5 * (x_norm[i] - 0.3)**2) * np.sin(12 * x_norm[i]) + \
                   0.7 * np.exp(-3 * (x_norm[i] + 0.4)**2) * np.cos(9 * x_norm[i]) + \
                   0.5 * np.exp(-2 * (x_norm[i] - 0.1)**2) * np.sin(15 * x_norm[i])
        
        # Cross-dimensional coupling with chaotic sine-wave interactions
        coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            coupling += np.sin(8 * x_norm[i] + 3 * np.sin(5 * x_norm[j])) * \
                       np.cos(6 * x_norm[i] + 2 * np.cos(4 * x_norm[k])) * \
                       np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Multi-scale periodic structure with varying amplitudes
        periodic = 0.0
        for i in range(self.dim):
            periodic += 0.8 * np.sin(18 * x_norm[i]) * np.cos(13 * x_norm[i]) + \
                       0.6 * np.sin(25 * x_norm[i]) * np.cos(20 * x_norm[i]) + \
                       0.4 * np.sin(30 * x_norm[i]) * np.cos(25 * x_norm[i])
        
        # Adaptive ridge structure with exponential decay
        ridge = 0.0
        for i in range(self.dim):
            ridge += np.exp(-0.3 * (x_norm[i] - 0.2)**2) * np.sin(20 * x_norm[i]) + \
                     0.8 * np.exp(-0.5 * (x_norm[i] + 0.3)**2) * np.cos(18 * x_norm[i])
        
        # Chaotic modulation with frequency mixing
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * x_norm[i] + 0.3 * np.sin(10 * x_norm[i])) * \
                      np.cos(12 * x_norm[i] + 0.4 * np.cos(8 * x_norm[i]))
        
        # Fractal-like basin with multi-scale interference
        fractal = 0.0
        r = np.sqrt(np.sum(x_norm**2))
        fractal = 0.9 * np.exp(-r**2) + 0.6 * np.sin(14 * r) * np.cos(9 * r) + \
                  0.4 * np.sin(22 * r) * np.cos(15 * r) + 0.2 * np.sin(30 * r)
        
        # Final combined function with weighted components
        return 0.25 * base_quad + 0.2 * rbf + 0.15 * coupling + 0.1 * periodic + \
               0.1 * ridge + 0.1 * chaotic + 0.05 * fractal