import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**23) + 0.92 * np.sum(x**22) + 0.78 * np.sum(x**21) + 0.62 * np.sum(x**20) + 0.45 * np.sum(x**19)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 15 + 8 * np.sin(x[i] * 1.2)  # Increased frequency modulation
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 1.1) * np.exp(-0.12 * x[i]**2) * np.sin(0.9 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.9, 4.9, min(15, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 3.0 + 1.8 * np.sin(0.8 * i + 0.2)  # Increased phase shift in weights
            rbf += weight * np.exp(-0.3 * (x[i] - center)**2) * np.sin(9 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 5.0 + 1.5 * np.sin(0.9 * (x[i] + x[j]) + 0.3)  # Increased coupling strength
            cross += coupling * (x[i]**12 + x[j]**12) * np.sin(0.8 * (x[i] - x[j])**12)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 1.2 * np.sin(11 * x[i] + 0.2))) * np.cos(x[i] * np.pi * (1 + 1.2 * np.cos(11 * x[i] + 0.2))) * np.exp(-0.35 * x[i]**2)
        
        # Scale and combine all components with dynamic weights
        return 0.42 * poly + 0.35 * trig + 0.25 * rbf + 0.18 * cross + 0.12 * chaotic