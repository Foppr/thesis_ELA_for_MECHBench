import numpy as np

class HybridTrigonometricRBF:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis function component with chaotic widths and positions
        rbf = 0.0
        centers = np.linspace(-4.5, 4.5, 13)
        for i, center in enumerate(centers):
            width = 0.3 + 0.7 * np.sin(i * 0.8 + 1.2) * np.cos(i * 0.5)
            rbf += np.exp(-0.5 * np.sum(((x - center) / width) ** 2)) * np.sin(i * 0.3)
        
        # Highly oscillatory trigonometric component with dynamic frequencies and phases
        trig = 0.0
        for i in range(self.dim):
            freq = 2.0 + 6.0 * np.sin(i * 0.7 + 0.5) * np.cos(i * 0.4)
            phase = 0.2 * np.sin(i * 1.1)
            trig += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.7 + phase) * np.exp(-0.1 * x[i]**2)
        
        # Complex saddle point with polynomial and exponential modulation
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2 * x[i]**2) * np.exp(-0.2 * x[i]**2) + 0.5 * np.sin(3 * x[i])
        
        # Strong cross-dimensional interaction with multi-scale exponential decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(0.5 * (x[i] + x[j]))
        
        # Multi-modal peaks with varying heights, widths, and positions
        peaks = 0.0
        heights = np.linspace(1.0, 3.5, 7)
        widths = np.linspace(0.5, 1.5, 7)
        for i, (height, width) in enumerate(zip(heights, widths)):
            center = np.full(self.dim, (i - 3) * 1.2 + 0.5 * np.sin(i * 0.9))
            peaks += height * np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Nonlinear scaling with chaotic modulation
        scale = 1.0 + 0.6 * np.sum(np.sin(0.8 * x) * np.cos(0.5 * x) * np.sin(0.3 * x))
        
        # Chaotic modulation with multiple sine-cosine combinations and feedback
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * x[i]) * np.cos(10 * x[i]) * np.sin(5 * x[i]) * np.cos(2 * x[i])
        
        # Fractional power with chaotic exponent modulation
        fractional = 0.0
        for i in range(self.dim):
            exp = 1.3 + 0.4 * np.sin(i * 0.6)
            fractional += (np.abs(x[i]) ** exp) * np.sin(3 * x[i]) * np.cos(1.5 * x[i])
        
        # Additional high-frequency oscillation component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Combine all components with adjusted weights
        return 1.1 * rbf + 0.9 * trig + 0.8 * saddle + 0.7 * cross + 0.9 * peaks + 0.5 * scale + 0.4 * chaotic + 0.4 * fractional + 0.3 * high_freq