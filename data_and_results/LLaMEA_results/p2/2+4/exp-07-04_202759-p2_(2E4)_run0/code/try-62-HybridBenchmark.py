import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**15) + 0.8 * np.sum(x**14) + 0.5 * np.sum(x**13) + 0.25 * np.sum(x**12) + 0.15 * np.sum(x**11)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 7 + 4 * np.sin(x[i] * 0.8)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.85) * np.exp(-0.05 * x[i]**2) * np.sin(0.7 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.8, 4.8, min(10, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 1.8 + 0.9 * np.sin(0.6 * i)
            rbf += weight * np.exp(-0.4 * (x[i] - center)**2) * np.sin(5 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 2.0 + 0.6 * np.sin(0.5 * (x[i] + x[j]))
            cross += coupling * (x[i]**7 + x[j]**7) * np.sin(0.4 * (x[i] - x[j])**7)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.6 * np.sin(7 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.6 * np.cos(7 * x[i]))) * np.exp(-0.15 * x[i]**2)
        
        # Scale and combine all components with dynamic weights
        return 0.32 * poly + 0.30 * trig + 0.20 * rbf + 0.15 * cross + 0.08 * chaotic