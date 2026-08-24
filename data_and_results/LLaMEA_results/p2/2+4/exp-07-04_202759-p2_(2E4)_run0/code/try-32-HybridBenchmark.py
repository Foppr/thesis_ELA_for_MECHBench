import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**8) + 0.8 * np.sum(x**7) + 0.5 * np.sum(x**6) + 0.2 * np.sum(x**5) + 0.1 * np.sum(x**4)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 3 + 4 * np.sin(x[i] * 0.6)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8) * np.exp(-0.03 * x[i]**2) * np.sin(0.5 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.8, 4.8, min(9, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 1.2 + 0.6 * np.sin(0.4 * i)
            rbf += weight * np.exp(-0.4 * (x[i] - center)**2) * np.sin(5 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 1.5 + 0.4 * np.sin(0.3 * (x[i] + x[j]))
            cross += coupling * (x[i]**3 + x[j]**3) * np.sin(0.4 * (x[i] - x[j])**3)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.2 * np.sin(3 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.2 * np.cos(3 * x[i]))) * np.exp(-0.1 * x[i]**2)
        
        # Scale and combine all components with dynamic weights
        return 0.3 * poly + 0.3 * trig + 0.2 * rbf + 0.12 * cross + 0.08 * chaotic