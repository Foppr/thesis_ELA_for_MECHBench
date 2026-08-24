import numpy as np

class HybridTrigonometricRBF:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Multi-modal RBF with chaotic center placement and varying widths
        rbf = 0.0
        centers = np.array([np.sin(i * 1.7) * 4.0 for i in range(13)])
        for i, center in enumerate(centers):
            width = 0.3 + 0.7 * np.abs(np.sin(i * 0.8))
            rbf += np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Chaotic trigonometric component with fractional frequencies
        trig = 0.0
        for i in range(self.dim):
            freq = 2.0 + 6.0 * np.sin(i * 0.3 + 1.0) * np.cos(i * 0.7)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4) * np.tan(0.5 * x[i])
        
        # Enhanced asymmetric saddle with polynomial modulation
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i] ** 3 - 3 * x[i] * np.sin(x[i])) * np.exp(-0.2 * x[i] ** 2)
        
        # Strong cross-dimensional interaction with logarithmic decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] * x[j]) * np.log(1.0 + 0.1 * (x[i]**2 + x[j]**2))
        
        # Multi-peak landscape with fractal-like height variations
        peaks = 0.0
        heights = np.array([1.0 + 2.0 * np.sin(i * 0.9) for i in range(7)])
        for i, height in enumerate(heights):
            center = np.full(self.dim, (i - 3) * 1.1)
            peaks += height * np.exp(-0.3 * np.sum((x - center)**2))
        
        # Nonlinear scaling with chaotic modulation
        scale = 1.0 + 0.6 * np.sum(np.sin(0.8 * x) * np.cos(0.3 * x) * np.tan(0.2 * x))
        
        # Hyper-chaotic modulation with nested trigonometric combinations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * x[i]) * np.cos(10 * x[i]) * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Fractional power with sinusoidal modulation
        fractional = 0.0
        for i in range(self.dim):
            fractional += (np.abs(x[i]) ** 1.7) * np.sin(3.0 * x[i]) * np.cos(0.5 * x[i])
        
        # Additional high-frequency oscillation component
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with dynamic weights
        return 1.1 * rbf + 0.9 * trig + 0.8 * saddle + 0.7 * cross + 0.9 * peaks + 0.5 * scale + 0.4 * chaotic + 0.4 * fractional + 0.3 * oscillation