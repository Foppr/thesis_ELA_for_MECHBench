import numpy as np

class NovelBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        periodic = 0
        for i in range(self.dim):
            freq = 2 * np.pi * (1 + 0.5 * np.sin(i))
            amplitude = 1.5 + 0.5 * np.cos(i)
            periodic += amplitude * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial basis function component with varying centers and widths
        rbf = 0
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            width = 0.5 + 0.3 * np.sin(i)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.sin(3 * (x[i] - center))
        
        # Cross-dimensional interaction terms with varying coupling strengths
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.8 + 0.4 * np.sin(0.5 * (i + j))
                cross += coupling * (x[i]**3 + x[j]**3) * np.cos(0.3 * (x[i] - x[j]))
        
        # Polynomial terms with mixed degrees to create curvature variations
        poly = 0
        poly += 0.5 * np.sum(x**2) + 0.3 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Saddle point and local minimum inducing component
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1)**2 * np.sin(0.5 * x[i])
        
        # Combine all components with dynamic weights
        return 0.25 * periodic + 0.30 * rbf + 0.20 * cross + 0.15 * poly + 0.10 * saddle