import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**11) + 0.8 * np.sum(x**10) + 0.5 * np.sum(x**9) + 0.25 * np.sum(x**8) + 0.12 * np.sum(x**7)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 5 + 4 * np.sin(x[i] * 0.6)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8) * np.exp(-0.03 * x[i]**2) * np.sin(0.7 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.8, 4.8, min(10, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 1.5 + 0.6 * np.sin(0.4 * i)
            rbf += weight * np.exp(-0.4 * (x[i] - center)**2) * np.sin(5 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 1.6 + 0.6 * np.sin(0.3 * (x[i] + x[j]))
            cross += coupling * (x[i]**5 + x[j]**5) * np.sin(0.4 * (x[i] - x[j])**5)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.4 * np.sin(5 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.4 * np.cos(5 * x[i]))) * np.exp(-0.1 * x[i]**2)
        
        # Scale and combine all components with dynamic weights
        return 0.3 * poly + 0.25 * trig + 0.2 * rbf + 0.15 * cross + 0.1 * chaotic