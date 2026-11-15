import numpy as np

class HybridTrigonometricRBF:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis function component with chaotic widths and positions
        rbf = 0.0
        centers = np.sin(np.linspace(0, np.pi, 11)) * 4.5
        for i, center in enumerate(centers):
            width = 0.2 + 0.6 * np.abs(np.sin(i * 0.7 + 1.2))
            rbf += np.exp(-0.5 * np.sum(((x - center) / width) ** 2)) * np.cos(i * 0.5)
        
        # Multi-frequency trigonometric component with chaotic modulation
        trig = 0.0
        for i in range(self.dim):
            freq = 2.0 + 6.0 * np.abs(np.sin(i * 0.3 + 0.5))
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.sin(x[i] * 0.3)
        
        # Asymmetric saddle point with polynomial scaling
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i] ** 3 - 3 * x[i] * np.sin(x[i])) * np.exp(-0.2 * x[i] ** 2)
        
        # Cross-dimensional interaction with logarithmic decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] * x[j]) * np.log(1 + 0.1 * (x[i]**2 + x[j]**2))
        
        # Multi-modal peaks with varying heights and chaotic centers
        peaks = 0.0
        heights = np.linspace(1.0, 3.5, 7)
        for i, height in enumerate(heights):
            center = np.full(self.dim, np.sin(i * 0.8) * 3.0)
            peaks += height * np.exp(-0.3 * np.sum((x - center)**2)) * np.cos(i * 0.4)
        
        # Nonlinear scaling with chaotic sine-cosine combination
        scale = 1.0 + 0.6 * np.sum(np.sin(0.7 * x) * np.cos(0.5 * x) * np.sin(0.3 * x))
        
        # Chaotic modulation with higher frequency components
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * x[i]) * np.cos(10 * x[i]) * np.sin(5 * x[i]) * np.cos(2 * x[i])
        
        # Fractional power with exponential modulation
        fractional = 0.0
        for i in range(self.dim):
            fractional += (np.abs(x[i]) ** 1.7) * np.sin(3.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Additional chaotic coupling term
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += np.cos(x[i] * x[j] * 0.5) * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * np.sin(i * 0.2)
        
        # Combine all components with dynamic weights
        return 1.1 * rbf + 0.9 * trig + 0.7 * saddle + 0.6 * cross + 0.9 * peaks + 0.5 * scale + 0.4 * chaotic + 0.4 * fractional + 0.3 * coupling