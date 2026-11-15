import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**21) + 0.9 * np.sum(x**20) + 0.7 * np.sum(x**19) + 0.5 * np.sum(x**18) + 0.3 * np.sum(x**17)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 12 + 8 * np.sin(x[i] * 0.9)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.9) * np.exp(-0.1 * x[i]**2) * np.sin(0.8 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.9, 4.9, min(12, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 2.5 + 1.5 * np.sin(0.7 * i)
            rbf += weight * np.exp(-0.6 * (x[i] - center)**2) * np.sin(8 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 4.0 + 1.1 * np.sin(0.8 * (x[i] + x[j]))
            cross += coupling * (x[i]**12 + x[j]**12) * np.sin(0.7 * (x[i] - x[j])**12)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.9 * np.sin(10 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.9 * np.cos(10 * x[i]))) * np.exp(-0.3 * x[i]**2)
        
        # Fractal-like self-similarity component with recursive scaling
        fractal = 0
        for i in range(self.dim):
            scale = 0.5 + 0.5 * np.sin(0.5 * x[i])
            fractal += scale * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Memory-dependent interaction component with delayed feedback
        memory = 0
        for i in range(self.dim):
            if i > 0:
                memory += 0.3 * np.sin(x[i] * x[i-1]) * np.exp(-0.1 * (x[i] - x[i-1])**2)
        
        # Scale and combine all components with dynamic weights
        return 0.3 * poly + 0.2 * trig + 0.15 * rbf + 0.1 * cross + 0.08 * chaotic + 0.07 * fractal + 0.05 * memory