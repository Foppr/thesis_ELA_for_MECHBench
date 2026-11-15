import numpy as np

class HybridTrigonometricRBF:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying widths and heights
        rbf = 0.0
        centers = np.linspace(-4.0, 4.0, 9)
        for i, center in enumerate(centers):
            width = 0.3 + 0.5 * np.sin(i * 0.7)
            height = 1.0 + 0.5 * np.cos(i * 0.5)
            rbf += height * np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Periodic trigonometric component with varying frequencies and phases
        trig = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            phase = 0.5 * np.cos(i * 0.3)
            trig += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.7 + phase)
        
        # Asymmetric saddle point component with modified exponential decay
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i] ** 2 - 2 * x[i] * np.sin(x[i])) * np.exp(-0.2 * x[i] ** 2)
        
        # Enhanced cross-dimensional interaction with cosine modulation
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.cos(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(0.5 * (x[i] + x[j]))
        
        # Modified Gaussian peaks with adaptive heights and positions
        peaks = 0.0
        heights = np.linspace(1.5, 3.0, 7)
        for i, height in enumerate(heights):
            center = np.full(self.dim, (i - 3) * 1.1)
            peaks += height * np.exp(-0.3 * np.sum((x - center)**2))
        
        # Nonlinear scaling component with enhanced complexity
        scale = 1.0 + 0.5 * np.sum(np.sin(0.7 * x) * np.cos(0.5 * x) * np.exp(-0.1 * x**2))
        
        # Chaotic modulation with higher frequency combinations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * x[i]) * np.cos(10 * x[i]) * np.sin(5 * x[i]) * np.cos(2 * x[i])
        
        # Fractional power component with varying exponents
        fractional = 0.0
        for i in range(self.dim):
            exponent = 1.3 + 0.4 * np.sin(i * 0.6)
            fractional += (np.abs(x[i]) ** exponent) * np.sin(3.0 * x[i])
        
        # Additional quadratic interaction term
        quadratic = 0.0
        for i in range(self.dim):
            quadratic += x[i] ** 2 * np.sin(0.3 * x[i])
        
        # Combine all components with optimized weights
        return 0.8 * rbf + 0.6 * trig + 0.5 * saddle + 0.4 * cross + 0.7 * peaks + 0.3 * scale + 0.2 * chaotic + 0.2 * fractional + 0.1 * quadratic