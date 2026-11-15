import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**17) + 0.9 * np.sum(x**16) + 0.6 * np.sum(x**15) + 0.35 * np.sum(x**14) + 0.2 * np.sum(x**13)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 9 + 5 * np.sin(x[i] * 0.9)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.9) * np.exp(-0.07 * x[i]**2) * np.sin(0.8 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.9, 4.9, min(12, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 2.0 + 1.1 * np.sin(0.7 * i)
            rbf += weight * np.exp(-0.5 * (x[i] - center)**2) * np.sin(6 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 2.5 + 0.8 * np.sin(0.6 * (x[i] + x[j]))
            cross += coupling * (x[i]**9 + x[j]**9) * np.sin(0.5 * (x[i] - x[j])**9)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.7 * np.sin(8 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.7 * np.cos(8 * x[i]))) * np.exp(-0.2 * x[i]**2)
        
        # Scale and combine all components with dynamic weights
        return 0.35 * poly + 0.32 * trig + 0.22 * rbf + 0.17 * cross + 0.10 * chaotic