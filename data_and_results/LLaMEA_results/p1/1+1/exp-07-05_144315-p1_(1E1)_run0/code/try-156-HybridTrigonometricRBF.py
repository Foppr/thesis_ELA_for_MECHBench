import numpy as np

class HybridTrigonometricRBF:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying widths
        rbf = 0.0
        centers = np.linspace(-4.0, 4.0, 9)
        for i, center in enumerate(centers):
            width = 0.4 + 0.4 * np.sin(i * 0.6)
            rbf += np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Periodic trigonometric component with varying frequencies
        trig = 0.0
        for i in range(self.dim):
            freq = 1.8 + 3.5 * np.sin(i * 0.45)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.65)
        
        # Asymmetric saddle point component with cubic terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i] ** 2 - 2 * x[i] * np.sin(x[i]) + 0.1 * x[i] ** 3) * np.exp(-0.15 * x[i] ** 2)
        
        # Cross-dimensional interaction with exponential decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] * x[j]) * np.exp(-0.09 * (x[i]**2 + x[j]**2))
        
        # Modified Gaussian peaks with different heights
        peaks = 0.0
        heights = np.linspace(1.3, 2.7, 5)
        for i, height in enumerate(heights):
            center = np.full(self.dim, (i - 2) * 1.2)
            peaks += height * np.exp(-0.23 * np.sum((x - center)**2))
        
        # Nonlinear scaling component with cubic terms
        scale = 1.0 + 0.4 * np.sum(np.sin(0.6 * x) * np.cos(0.4 * x) + 0.05 * x ** 3)
        
        # Chaotic modulation with sine-cosine combinations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(13 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
        
        # Fractional power component for additional nonlinearity with cubic term
        fractional = 0.0
        for i in range(self.dim):
            fractional += (np.abs(x[i]) ** 1.45) * np.sin(2.6 * x[i]) + 0.02 * x[i] ** 3
        
        # Combine all components with appropriate weights
        return 0.85 * rbf + 0.75 * trig + 0.65 * saddle + 0.55 * cross + 0.85 * peaks + 0.45 * scale + 0.35 * chaotic + 0.35 * fractional