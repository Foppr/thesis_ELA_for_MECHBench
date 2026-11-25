import numpy as np

class RadialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add radial basis function components with varying widths and centers
        for i in range(self.dim):
            # Radial basis with Gaussian-like decay
            f_val += np.exp(-0.1 * (x[i] - 1.0)**2) + 0.5 * np.exp(-0.2 * (x[i] + 2.0)**2)
        
        # Add multi-scale harmonic oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(2 * np.pi * x[i]) + 0.2 * np.sin(4 * np.pi * x[i]) + \
                     0.1 * np.sin(8 * np.pi * x[i]) + 0.05 * np.sin(16 * np.pi * x[i])
        
        # Add cross-dimensional interactions with adaptive coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling based on dimension indices and harmonic modulation
                coupling = 0.03 * (1 + np.cos(0.3 * (i - j)))
                f_val += coupling * np.sin(x[i] + x[j]) * np.cos(0.5 * (x[i] - x[j]))
        
        # Add polynomial conditioning with multi-scale exponents
        f_val += 0.2 * np.sum(x**3) + 0.1 * np.sum(x**5) + 0.05 * np.sum(x**7)
        
        # Add a complex interaction term with multiple harmonic components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.02 * np.sin(3 * x[i]) * np.cos(2 * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Add global sinusoidal modulation with adaptive frequency
        f_val += 0.15 * np.sin(0.5 * np.sum(x)) + 0.1 * np.cos(0.3 * np.sum(x)**2)
        
        return f_val