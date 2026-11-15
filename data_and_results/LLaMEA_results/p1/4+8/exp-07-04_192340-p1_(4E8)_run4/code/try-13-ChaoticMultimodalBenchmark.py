import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x_scaled = x
        
        # Base quadratic term
        f1 = np.sum(x_scaled**2)
        
        # Sinusoidal modulations creating multiple local minima
        f2 = 0.5 * np.sum(np.sin(3 * x_scaled) * np.cos(7 * x_scaled))
        
        # Chaotic component using sine map for complex landscape
        chaotic = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic += np.sin(x_scaled[i]) * np.cos(x_scaled[i])
            else:
                chaotic += np.sin(x_scaled[i-1] * x_scaled[i]) * np.cos(x_scaled[i])
        
        # Saddle point structure
        f3 = 0.1 * np.sum(np.sin(x_scaled) * np.cos(x_scaled)**2)
        
        # Combine all components
        return f1 + f2 + f3 + 0.01 * chaotic