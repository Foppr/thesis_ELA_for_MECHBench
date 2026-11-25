import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly modified logistic map constants for enhanced chaos
        self.r_values = np.linspace(3.55, 3.85, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Modified chaotic component with different initial conditions and iteration counts
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            xi = 0.4 + 0.02 * np.random.rand()
            for _ in range(40):
                xi = r * xi * (1 - xi)
            for _ in range(15):
                xi = r * xi * (1 - xi)
            chaos += xi
        
        # Modified trigonometric interference with different frequencies and amplitudes
        wave = np.sum(np.sin(3.5 * np.pi * x_norm) * np.cos(5.5 * np.pi * x_norm) + 
                      np.sin(7.0 * np.pi * x_norm) * np.cos(9.0 * np.pi * x_norm) +
                      np.sin(11.0 * np.pi * x_norm) * np.cos(13.0 * np.pi * x_norm) +
                      np.sin(15.0 * np.pi * x_norm) * np.cos(17.0 * np.pi * x_norm))
        
        # Modified polynomial coupling with different coefficients
        poly = np.sum(0.8 * x_norm**3 + 0.5 * x_norm**2 + 0.3 * x_norm + 0.1)
        
        # Modified coupling with altered sinusoidal interactions
        coupling = np.prod(np.sin(0.7 * np.pi * x_norm) + np.cos(0.7 * np.pi * x_norm) + 
                          np.sin(1.3 * np.pi * x_norm) * np.cos(1.3 * np.pi * x_norm))
        
        # Modified radial basis function with different parameters
        rbf = np.sum(np.exp(-0.25 * x_norm**2) * np.sin(20 * x_norm) * np.cos(4 * x_norm))
        
        # Modified exponential modulation
        exp_mod = np.sum(np.exp(-0.35 * x_norm**2) * np.cos(8 * x_norm) * np.sin(2.5 * x_norm))
        
        # Combine all components with updated weights
        return 0.3 * chaos + 0.3 * wave + 0.18 * poly + 0.1 * coupling + 0.07 * rbf + 0.05 * exp_mod + 1.7