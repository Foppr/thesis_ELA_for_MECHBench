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
            chaotic += np.sin(15 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Enhanced saddle point structure with higher-order terms and nonlinearity
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**10 - 7 * x[i]**8 + 25 * x[i]**6 - 40 * x[i]**4 + 30 * x[i]**2 - 5) * np.sin(x[i])
        
        # Enhanced cross-term interactions with non-linear coupling and interaction strength
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.7 * x[i] * x[j] * np.sin(0.8 * (x[i]**2 + x[j]**2)) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic modulation term with different frequencies and damping
        modulate = 0
        for i in range(self.dim):
            modulate += np.sin(7 * x[i]) * np.cos(11 * x[i]) * np.exp(-0.03 * x[i]**2)
        
        # Add a small chaotic noise term to increase landscape complexity
        noise = 0.05 * np.sum(np.sin(20 * x) * np.cos(15 * x))
        
        # Add cubic cross-terms for increased complexity
        cubic_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    cubic_cross += 0.15 * x[i] * x[j] * x[k] * np.sin(0.4 * (x[i]**2 + x[j]**2 + x[k]**2))
        
        # Add hyperbolic and logarithmic perturbations for increased complexity
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += np.tanh(x[i]) * np.log(np.abs(x[i]) + 1.1) * np.exp(-0.02 * x[i]**2)
        
        # Add logarithmic damping to the overall function
        log_damp = 0
        for i in range(self.dim):
            log_damp += np.log(np.abs(x[i]) + 1.05) * np.exp(-0.01 * x[i]**2)
        
        return quadratic + chaotic + saddle + cross + modulate + noise + cubic_cross + hyperbolic + log_damp