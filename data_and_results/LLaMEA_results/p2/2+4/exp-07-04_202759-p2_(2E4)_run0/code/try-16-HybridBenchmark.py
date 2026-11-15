import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees and chaotic modulation
        poly = np.sum(x**6) + 0.3 * np.sum(x**5) + 0.1 * np.sum(x**4) + 0.05 * np.sum(x**3)
        
        # Trigonometric component with chaotic frequency modulation and phase shifts
        trig = 0
        for i in range(self.dim):
            freq_mod = 1 + 0.5 * np.sin(0.3 * i * np.pi)  # Chaotic frequency modulation
            trig += np.sin(freq_mod * x[i]) * np.cos(2 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Radial basis function component with chaotic center placement and multi-scale influence
        rbf = 0
        for i in range(self.dim):
            center = -4 + 8 * (i / (self.dim - 1) if self.dim > 1 else 0) + 0.5 * np.sin(0.7 * i * np.pi)
            scale = 0.5 + 0.3 * np.cos(0.4 * i * np.pi)
            rbf += np.exp(-0.5 * ((x[i] - center) / scale)**2) * np.sin(3 * (x[i] - center))
        
        # Cross-term interactions with chaotic coupling strengths and saddle-point creation
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 0.5 + 0.3 * np.sin(0.2 * i * np.pi)
            cross += coupling * (x[i]**2 + x[j]**2) * np.sin(0.3 * (x[i] - x[j])**2) + 0.1 * x[i] * x[j]
        
        # Saddle-point structure component to increase deception
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1)**2 * np.cos(0.5 * x[i])
        
        # Scale and combine components with dynamic weighting
        weights = [0.25, 0.35, 0.2, 0.15 + 0.05 * np.sin(0.1 * self.dim)]
        return weights[0] * poly + weights[1] * trig + weights[2] * rbf + weights[3] * cross + 0.1 * saddle