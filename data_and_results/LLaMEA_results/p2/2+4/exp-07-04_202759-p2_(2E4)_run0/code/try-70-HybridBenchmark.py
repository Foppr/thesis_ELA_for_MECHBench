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
            freq = 8.5 + 3.0 * np.sin(x[i] * 0.95)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.95) * np.exp(-0.07 * x[i]**2) * np.sin(0.65 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.9, 4.9, min(12, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 2.1 + 0.7 * np.sin(0.75 * i)
            rbf += weight * np.exp(-0.37 * (x[i] - center)**2) * np.sin(4.7 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 2.3 + 0.4 * np.sin(0.65 * (x[i] + x[j]))
            cross += coupling * (x[i]**8 + x[j]**8) * np.sin(0.37 * (x[i] - x[j])**8)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.75 * np.sin(8.2 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.75 * np.cos(8.2 * x[i]))) * np.exp(-0.19 * x[i]**2)
        
        # Scale and combine all components with dynamic weights
        return 0.35 * poly + 0.28 * trig + 0.18 * rbf + 0.16 * cross + 0.08 * chaotic