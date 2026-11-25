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
            f_val += np.exp(-0.12 * (x[i] - 1.2)**2) + 0.4 * np.exp(-0.25 * (x[i] + 1.8)**2)
        
        # Add multi-scale harmonic oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.35 * np.sin(2.2 * np.pi * x[i]) + 0.25 * np.sin(4.1 * np.pi * x[i]) + \
                     0.12 * np.sin(8.3 * np.pi * x[i]) + 0.06 * np.sin(16.2 * np.pi * x[i])
        
        # Add cross-dimensional interactions with adaptive coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling based on dimension indices and harmonic modulation
                coupling = 0.04 * (1 + np.cos(0.35 * (i - j)))
                f_val += coupling * np.sin(x[i] + x[j]) * np.cos(0.55 * (x[i] - x[j]))
        
        # Add polynomial conditioning with multi-scale exponents
        f_val += 0.25 * np.sum(x**3) + 0.15 * np.sum(x**5) + 0.08 * np.sum(x**7)
        
        # Add a complex interaction term with multiple harmonic components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.025 * np.sin(3.2 * x[i]) * np.cos(2.1 * x[j]) * np.exp(-0.06 * (x[i] - x[j])**2)
        
        # Add global sinusoidal modulation with adaptive frequency
        f_val += 0.18 * np.sin(0.55 * np.sum(x)) + 0.12 * np.cos(0.35 * np.sum(x)**2)
        
        return f_val