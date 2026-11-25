import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms with varying degrees
        f1 = 0.0
        for i in range(self.dim):
            degree = 2 + int(3 * np.sin(0.3 * i))
            f1 += x[i]**degree
            
        # Radial harmonic interactions with adaptive frequencies
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(0.2 * i + 0.1 * r)
            f2 += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Cross-dimensional coupling with time-varying weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(0.1 * (i + j) + 0.2 * r)
                interaction = x[i]**2 * x[j] + x[i] * x[j]**2
                f3 += weight * interaction
                
        # Boundary attraction terms with exponential decay
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                penalty = 2.0 * (5.0 - np.abs(x[i]))**2
                f4 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Multi-scale sinusoidal modulations with adaptive amplitudes
        f5 = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.4 * i + 0.2 * r)
            freq = 2.0 + 3.0 * np.cos(0.3 * i)
            f5 += amp * np.sin(freq * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Cubic cross-terms with dynamic coupling coefficients
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.3 + 0.4 * np.sin(0.2 * (i - j) + 0.1 * r)
                f6 += coeff * x[i]**3 * x[j]
                
        # Quadratic harmonic interactions with complex phase shifts
        f7 = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.2 * i + 0.1 * r)
            f7 += (np.sin(x[i] + phase)**2 + np.cos(x[i] + phase)**2) * np.exp(-0.03 * x[i]**2)
            
        # Fractal-like polynomial combinations with varying exponents
        f8 = 0.0
        for i in range(self.dim):
            exp_factor = 1.5 + 0.5 * np.sin(0.3 * i + 0.1 * r)
            f8 += x[i]**exp_factor
            
        # Stochastic harmonic terms with varying frequencies and amplitudes
        f9 = 0.0
        for i in range(self.dim):
            amp = 0.8 + 0.4 * np.random.uniform(0, 1)
            freq = 1.5 + 2.5 * np.random.uniform(0, 1)
            f9 += amp * np.sin(freq * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Additional boundary repulsion with polynomial penalties
        f10 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty = 1.5 * (5.0 - np.abs(x[i]))**3
                f10 += penalty * np.exp(-0.08 * x[i]**2)
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10