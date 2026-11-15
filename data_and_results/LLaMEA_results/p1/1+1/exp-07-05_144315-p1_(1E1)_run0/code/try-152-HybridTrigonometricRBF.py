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
            width = 0.3 + 0.5 * np.sin(i * 0.7)
            rbf += np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Periodic trigonometric component with varying frequencies
        trig = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.5 * np.sin(i * 0.5)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Asymmetric saddle point component
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i] ** 2 - 2 * x[i] * np.sin(x[i])) * np.exp(-0.2 * x[i] ** 2)
        
        # Cross-dimensional interaction with exponential decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Modified Gaussian peaks with different heights
        peaks = 0.0
        heights = np.linspace(1.0, 3.0, 7)
        for i, height in enumerate(heights):
            center = np.full(self.dim, (i - 3) * 1.2)
            peaks += height * np.exp(-0.3 * np.sum((x - center)**2))
        
        # Nonlinear scaling component
        scale = 1.0 + 0.5 * np.sum(np.sin(0.7 * x) * np.cos(0.5 * x))
        
        # Chaotic modulation with sine-cosine combinations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i]) * np.cos(6 * x[i]) * np.sin(3 * x[i])
        
        # Fractional power component for additional nonlinearity
        fractional = 0.0
        for i in range(self.dim):
            fractional += (np.abs(x[i]) ** 1.6) * np.sin(3.0 * x[i])
        
        # Additional quadratic interaction terms
        quadratic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quadratic += 0.1 * (x[i] - x[j])**2 * np.sin(x[i] + x[j])
        
        # Combine all components with appropriate weights
        return 0.8 * rbf + 0.6 * trig + 0.7 * saddle + 0.4 * cross + 0.9 * peaks + 0.3 * scale + 0.2 * chaotic + 0.2 * fractional + 0.5 * quadratic