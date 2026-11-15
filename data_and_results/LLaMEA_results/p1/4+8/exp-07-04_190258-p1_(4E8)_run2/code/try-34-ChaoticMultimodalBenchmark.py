import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with higher frequency and amplitude
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(8 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Enhanced saddle point structure with higher-order terms and nonlinearity
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 4 * x[i]**4 + 6 * x[i]**2 - 2) * np.sin(x[i])
        
        # Enhanced cross-term interactions with non-linear coupling and interaction strength
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.3 * x[i] * x[j] * np.sin(0.4 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic modulation term with different frequencies and damping
        modulate = 0
        for i in range(self.dim):
            modulate += np.sin(3 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.03 * x[i]**2)
        
        # Add a small chaotic noise term to increase landscape complexity
        noise = 0.01 * np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        return quadratic + chaotic + saddle + cross + modulate + noise