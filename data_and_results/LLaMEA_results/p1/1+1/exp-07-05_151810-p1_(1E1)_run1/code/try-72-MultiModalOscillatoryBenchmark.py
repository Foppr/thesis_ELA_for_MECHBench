import numpy as np

class MultiModalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        oscillation = np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x))
        
        # Radial basis function with adaptive centers and widths
        rbf = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.5 * i)
            width = 0.5 + 0.3 * np.cos(0.7 * i)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-term interaction component with polynomial coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.3 * (x[i]**2) * (x[j]**3) * np.sin(0.5 * (x[i] + x[j]))
        
        # Polynomial landscape with mixed degree terms
        polynomial = np.sum(0.5 * x**4 - 2.0 * x**3 + 3.0 * x**2 - x)
        
        # Periodic potential with multiple local minima
        periodic = np.sum(2.0 * np.cos(0.8 * x) + 0.5 * np.cos(2.4 * x) + 0.3 * np.cos(4.0 * x))
        
        # Combined function
        result = oscillation + rbf + cross + polynomial + periodic
        
        return result