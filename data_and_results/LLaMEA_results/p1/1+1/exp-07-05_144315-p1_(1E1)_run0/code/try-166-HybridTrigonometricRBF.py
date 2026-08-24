import numpy as np

class HybridTrigonometricRBF:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying widths and shifted centers
        rbf = 0.0
        centers = np.linspace(-4.5, 4.5, 11)
        for i, center in enumerate(centers):
            width = 0.3 + 0.5 * np.sin(i * 0.5)
            rbf += np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Periodic trigonometric component with varying frequencies and phase shifts
        trig = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.3)
            phase = 0.5 * np.cos(i * 0.7)
            trig += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.7 + phase)
        
        # Asymmetric saddle point component with modified exponential decay
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i] ** 2 - 2 * x[i] * np.sin(x[i])) * np.exp(-0.2 * x[i] ** 2)
        
        # Cross-dimensional interaction with cosine decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.cos(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Modified Gaussian peaks with varying heights and widths
        peaks = 0.0
        heights = np.linspace(1.0, 3.0, 7)
        widths = np.linspace(0.5, 1.5, 7)
        for i, (height, width) in enumerate(zip(heights, widths)):
            center = np.full(self.dim, (i - 3) * 1.1)
            peaks += height * np.exp(-0.3 * np.sum(((x - center) / width) ** 2))
        
        # Nonlinear scaling component with modified trigonometric functions
        scale = 1.0 + 0.5 * np.sum(np.sin(0.7 * x) * np.cos(0.5 * x))
        
        # Chaotic modulation with multiple sine-cosine combinations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * x[i]) * np.cos(10 * x[i]) * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Fractional power component with modified exponents
        fractional = 0.0
        for i in range(self.dim):
            fractional += (np.abs(x[i]) ** 1.6) * np.sin(3.0 * x[i])
        
        # Additional harmonic component for increased complexity
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with adjusted weights
        return 0.8 * rbf + 0.6 * trig + 0.7 * saddle + 0.4 * cross + 0.9 * peaks + 0.5 * scale + 0.4 * chaotic + 0.3 * fractional + 0.2 * harmonic