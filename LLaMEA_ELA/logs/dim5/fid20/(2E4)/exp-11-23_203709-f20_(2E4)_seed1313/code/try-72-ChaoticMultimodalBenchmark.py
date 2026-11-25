import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic trigonometric component with varying frequencies and phases
        trig_component = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            phase = 0.5 * np.cos(0.7 * i)
            trig_component += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
        
        # Adaptive Gaussian peaks with dynamic centers and variances
        gaussian_component = 0
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.5 + 1.0 * np.sin(0.3 * i)
            gaussian_component += 3.0 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional interaction terms with chaotic coupling
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(3.0 * dx) * np.cos(2.0 * dx)
                cross_interaction += 1.5 * (dx**2 + dy**2) / (1.0 + np.abs(dx) + np.abs(dy))
        
        # Dynamic scaling with chaotic modulation
        scaling_factor = 1.0 + 0.2 * np.sin(0.3 * self.dim) * np.cos(0.4 * self.dim)
        
        # Noise injection to increase complexity and robustness
        noise = np.random.normal(0, 0.1) if self.dim > 1 else 0
        
        # Combine all components with adjusted weights
        return scaling_factor * (2.0 * trig_component + 3.0 * gaussian_component + 0.8 * cross_interaction) + noise + 25.0