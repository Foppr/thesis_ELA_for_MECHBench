import numpy as np

class ChaoticFractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add periodic trigonometric components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.8 * np.sin(2 * np.pi * x[i]) + 0.4 * np.sin(4 * np.pi * x[i]) + \
                     0.2 * np.sin(8 * np.pi * x[i]) + 0.1 * np.sin(16 * np.pi * x[i])
        
        # Add adaptive polynomial conditioning with chaotic coefficients
        for i in range(self.dim):
            coeff = 0.5 + 0.5 * np.sin(0.3 * i)
            f_val += coeff * (x[i]**4) + (1 - coeff) * (x[i]**6)
        
        # Add cross-dimensional cubic interaction terms with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * (1 + np.sin(0.5 * (i + j)))
                f_val += coupling * (x[i]**3) * (x[j]**3) * np.cos(2 * (x[i] - x[j]))
        
        # Add fractal-like self-similar structures with recursive scaling
        scale_factor = 0.1
        for k in range(1, 5):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 10 * x[i]) * np.cos(k * 8 * x[i])
            scale_factor *= 0.6
        
        # Add chaotic interaction terms with multi-scale modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.15 * np.sin(3 * x[i]) * np.cos(2 * x[j]) * \
                         np.exp(-0.2 * (x[i] - x[j])**2) * (1 + 0.2 * np.sin(4 * (x[i] + x[j])))
        
        # Add global sinusoidal modulation with multiple frequencies
        f_val += 0.3 * np.sin(np.sum(x)) + 0.2 * np.cos(2 * np.sum(x)) + \
                 0.1 * np.sin(3 * np.sum(x)**2) + 0.05 * np.cos(4 * np.sum(x)**3)
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.7:
                penalty += 15 * (abs(x[i]) - 4.7)**2
        f_val += penalty
        
        return f_val