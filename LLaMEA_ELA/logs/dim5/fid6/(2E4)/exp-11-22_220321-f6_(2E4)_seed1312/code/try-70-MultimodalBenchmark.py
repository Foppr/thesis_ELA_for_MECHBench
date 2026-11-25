import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 0.8
        self.beta = 2.5
        self.gamma = 1.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with asymmetric scaling
        result = 0.0
        for i in range(self.dim):
            result += (x[i] ** 2) * (1 + self.alpha * np.sin(i * 0.6))
            
        # Asymmetric sine-wave interaction terms
        sine_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sine_interaction += np.sin(1.7 * x[i] * x[j]) * np.cos(self.beta * (x[i] + x[j]))
                
        # Polynomial chaos component with dynamic weights
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += (x[i]**4 + self.gamma * x[i]**6) * np.exp(-0.2 * x[i]**2)
            
        # Dynamic cross-dimensional coupling with varying strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j]) * np.sin(2.0 * np.pi * (x[i] - x[j])) * \
                           (1 + 0.4 * np.cos(i * j * 0.8))
                           
        # Non-convex penalty with asymmetric polynomial terms
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i]**9 + x[i]**5 + x[i]**3) * (1 + self.beta * np.sin(i * 0.4))
            
        return result + 0.45 * sine_interaction + 0.35 * chaos_term + 0.3 * coupling + 0.45 * penalty