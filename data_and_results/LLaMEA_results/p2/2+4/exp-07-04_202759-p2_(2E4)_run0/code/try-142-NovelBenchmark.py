import numpy as np

class NovelBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying exponents and asymmetric scaling
        poly = 0
        for i in range(self.dim):
            exp = 2 + 3 * np.sin(i * 0.5)
            scale = 1.0 + 0.5 * np.cos(i * 0.3)
            poly += scale * (x[i] ** exp)
        
        # Sinusoidal component with frequency modulation and phase shifts
        sin_comp = 0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(x[i] * 0.7)
            phase = np.pi * np.cos(x[i] * 0.4)
            sin_comp += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.8 + phase)
        
        # Radial basis function with dynamic centers and varying widths
        rbf = 0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * 0.6)
            width = 0.5 + 0.3 * np.cos(i * 0.4)
            rbf += np.exp(-width * (x[i] - center)**2) * np.sin(8 * (x[i] - center))
        
        # Cross-term interactions with dynamic coupling coefficients
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 3.0 + 2.0 * np.sin(0.5 * (x[i] + x[j]))
                cross += coupling * np.sin(2 * (x[i] - x[j])) * np.cos(2 * (x[i] + x[j]))
        
        # Asymmetric scaling component to introduce conditioning bias
        asym = 0
        for i in range(self.dim):
            if x[i] >= 0:
                asym += 0.5 * x[i]**3
            else:
                asym += 1.5 * x[i]**3
        
        # Combined weighted sum of all components
        return 0.25 * poly + 0.30 * sin_comp + 0.20 * rbf + 0.15 * cross + 0.10 * asym