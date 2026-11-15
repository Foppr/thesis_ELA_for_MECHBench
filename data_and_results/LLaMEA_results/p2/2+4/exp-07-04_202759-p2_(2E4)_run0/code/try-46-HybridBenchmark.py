import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**9) + 0.7 * np.sum(x**8) + 0.4 * np.sum(x**7) + 0.15 * np.sum(x**6) + 0.08 * np.sum(x**5)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 2.7 + 3.3 * np.sin(x[i] * 0.65)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.85) * np.exp(-0.035 * x[i]**2) * np.sin(0.55 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(8, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 1.0 + 0.55 * np.sin(0.5 * i)
            rbf += weight * np.exp(-0.32 * (x[i] - center)**2) * np.sin(4.2 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 1.25 + 0.35 * np.sin(0.42 * (x[i] + x[j]))
            cross += coupling * (x[i]**4 + x[j]**4) * np.sin(0.52 * (x[i] - x[j])**4)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.16 * np.sin(4.1 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.14 * np.cos(4.2 * x[i]))) * np.exp(-0.11 * x[i]**2)
        
        # Scale and combine all components with dynamic weights
        return 0.25 * poly + 0.25 * trig + 0.2 * rbf + 0.15 * cross + 0.15 * chaotic