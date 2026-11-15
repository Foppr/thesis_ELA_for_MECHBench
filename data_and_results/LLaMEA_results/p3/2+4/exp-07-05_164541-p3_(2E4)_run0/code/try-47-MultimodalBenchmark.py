import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal waves with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) + 
                          np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x) + 
                          np.sin(9 * np.pi * x) * np.cos(11 * np.pi * x))
        
        # Polynomial chaos with mixed degrees and nonlinear interactions
        poly_term = np.sum(0.1 * x**10 - 0.5 * x**8 + 1.2 * x**6 - 1.8 * x**4 + 1.5 * x**2)
        
        # Radial basis function correlations with varying centers and widths
        rbfs = []
        for i in range(self.dim):
            center = np.random.uniform(-5.0, 5.0)
            width = np.random.uniform(0.5, 2.0)
            rbf = np.exp(-0.5 * ((x[i] - center) / width)**2)
            rbfs.append(rbf)
        rbf_term = np.sum(rbfs)
        
        # Cross-dimensional coupling with chaotic phase shifts
        coupling_term = 0.0
        for i in range(self.dim - 1):
            phase_shift = np.sin(np.pi * x[i]) * np.cos(np.pi * x[i+1])
            coupling_term += (x[i] - x[i+1])**2 * phase_shift
        
        # Fractional power chaotic interactions
        frac_term = np.sum(np.sin(np.pi * x**1.3) * np.cos(2 * np.pi * x**1.7) * 
                           np.sin(3 * np.pi * x**1.5) * np.cos(4 * np.pi * x**1.9))
        
        # Global offset and scaling
        return 0.3 * sin_term + 0.2 * poly_term + 0.1 * rbf_term + 0.15 * coupling_term + 0.05 * frac_term + 3.0