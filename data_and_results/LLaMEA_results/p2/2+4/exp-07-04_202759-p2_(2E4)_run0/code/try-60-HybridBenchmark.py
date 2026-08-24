import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**13) + 0.9 * np.sum(x**12) + 0.6 * np.sum(x**11) + 0.35 * np.sum(x**10) + 0.18 * np.sum(x**9)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 4.2 + 5.2 * np.sin(x[i] * 0.95)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.95) * np.exp(-0.07 * x[i]**2) * np.sin(0.85 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.9, 4.9, min(12, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 1.6 + 0.9 * np.sin(0.75 * i)
            rbf += weight * np.exp(-0.5 * (x[i] - center)**2) * np.sin(6.2 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 2.2 + 0.6 * np.sin(0.65 * (x[i] + x[j]))
            cross += coupling * (x[i]**6 + x[j]**6) * np.sin(0.75 * (x[i] - x[j])**6)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.35 * np.sin(6.2 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.35 * np.cos(6.2 * x[i]))) * np.exp(-0.22 * x[i]**2)
        
        # Scale and combine all components with dynamic weights
        return 0.35 * poly + 0.3 * trig + 0.2 * rbf + 0.1 * cross + 0.05 * chaotic