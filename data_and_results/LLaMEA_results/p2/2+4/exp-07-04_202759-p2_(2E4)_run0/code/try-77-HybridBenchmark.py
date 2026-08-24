import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sin_comp = 0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(0.3 * i)
            amp = 1.5 + 0.3 * np.cos(0.4 * i)
            sin_comp += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Radial basis function component with dynamic centers and varying widths
        rbf_comp = 0
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            width = 0.5 + 0.3 * np.sin(0.5 * i)
            rbf_comp += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.sin(3.0 * (x[i] - center))
        
        # Cross-dimensional interaction terms with exponential coupling
        cross_comp = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 + 0.2 * np.sin(0.5 * (x[i] + x[j]))
                cross_comp += coupling * np.exp(-0.1 * (x[i] - x[j])**2) * (x[i]**3 + x[j]**3)
        
        # Chaotic modulation component using logistic map-like behavior
        chaotic_comp = 0
        for i in range(self.dim):
            logistic = 3.8 * x[i] * (1 - x[i])
            chaotic_comp += np.sin(logistic * x[i]) * np.cos(logistic * x[i] * 0.8) * np.exp(-0.05 * x[i]**2)
        
        # Combine all components with weighted contributions
        return 0.3 * sin_comp + 0.25 * rbf_comp + 0.25 * cross_comp + 0.2 * chaotic_comp