import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**19) + 0.85 * np.sum(x**18) + 0.65 * np.sum(x**17) + 0.4 * np.sum(x**16) + 0.25 * np.sum(x**15)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 10 + 6 * np.sin(x[i] * 0.85)  # Slight change in frequency modulation
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.85) * np.exp(-0.08 * x[i]**2) * np.sin(0.7 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.8, 4.8, min(10, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 2.2 + 1.3 * np.sin(0.6 * i)
            rbf += weight * np.exp(-0.5 * (x[i] - center)**2) * np.sin(7 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 3.0 + 0.9 * np.sin(0.7 * (x[i] + x[j]))
            cross += coupling * (x[i]**10 + x[j]**10) * np.sin(0.6 * (x[i] - x[j])**10)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.8 * np.sin(9 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.8 * np.cos(9 * x[i]))) * np.exp(-0.25 * x[i]**2)
        
        # Scale and combine all components with dynamic weights
        return 0.37 * poly + 0.30 * trig + 0.20 * rbf + 0.15 * cross + 0.08 * chaotic