import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**23) + 0.8 * np.sum(x**22) + 0.6 * np.sum(x**21) + 0.4 * np.sum(x**20) + 0.2 * np.sum(x**19)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 15 + 10 * np.sin(x[i] * 0.8)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8) * np.exp(-0.15 * x[i]**2) * np.sin(0.7 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.8, 4.8, min(10, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 3.0 + 2.0 * np.sin(0.6 * i)
            rbf += weight * np.exp(-0.5 * (x[i] - center)**2) * np.sin(9 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 5.0 + 1.2 * np.sin(0.9 * (x[i] + x[j]))
            cross += coupling * (x[i]**13 + x[j]**13) * np.sin(0.6 * (x[i] - x[j])**13)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.8 * np.sin(12 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.8 * np.cos(12 * x[i]))) * np.exp(-0.25 * x[i]**2)
        
        # Fractal-like self-similarity component with recursive scaling
        fractal = 0
        for i in range(self.dim):
            scale = 0.6 + 0.4 * np.sin(0.6 * x[i])
            fractal += scale * np.sin(12 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Memory-dependent interaction component with delayed feedback
        memory = 0
        for i in range(self.dim):
            if i > 0:
                memory += 0.4 * np.sin(x[i] * x[i-1]) * np.exp(-0.12 * (x[i] - x[i-1])**2)
        
        # Scale and combine all components with dynamic weights
        return 0.35 * poly + 0.25 * trig + 0.18 * rbf + 0.12 * cross + 0.09 * chaotic + 0.06 * fractal + 0.05 * memory