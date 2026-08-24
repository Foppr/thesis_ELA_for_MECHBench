import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**25) + 0.98 * np.sum(x**24) + 0.85 * np.sum(x**23) + 0.70 * np.sum(x**22) + 0.50 * np.sum(x**21)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 22 + 12 * np.sin(x[i] * 1.3)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 1.3) * np.exp(-0.18 * x[i]**2) * np.sin(1.2 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.8, 4.8, min(20, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 3.8 + 3.2 * np.sin(0.95 * i)
            rbf += weight * np.exp(-0.85 * (x[i] - center)**2) * np.sin(11 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 6.5 + 2.5 * np.sin(1.1 * (x[i] + x[j]))
            cross += coupling * (x[i]**15 + x[j]**15) * np.sin(1.1 * (x[i] - x[j])**15)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 1.3 * np.sin(16 * x[i]))) * np.cos(x[i] * np.pi * (1 + 1.3 * np.cos(16 * x[i]))) * np.exp(-0.45 * x[i]**2)
        
        # Fractal-like self-similarity component with memory-dependent interactions
        fractal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                fractal += np.sin(140 * dist) * np.exp(-0.65 * dist**2) * (1 + 0.18 * np.sin(7.5 * x[i]) * np.cos(7.5 * x[j]))
        
        # Memory-dependent interaction term
        memory = 0
        for i in range(self.dim):
            memory += np.sin(0.55 * x[i]) * np.cos(0.55 * x[i]) * np.exp(-0.28 * x[i]**2) * (1 + 0.09 * np.sum(x[:i]))
        
        # Scale and combine all components with dynamic weights
        return 0.36 * poly + 0.29 * trig + 0.26 * rbf + 0.16 * cross + 0.07 * chaotic + 0.06 * fractal + 0.01 * memory