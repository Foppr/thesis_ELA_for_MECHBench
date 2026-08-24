import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.chaotic_params = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum
        f_value = np.sum(x**2) * 0.5
        
        # Chaotic logistic map component
        chaotic_term = 0.0
        for i in range(self.dim):
            # Logistic map with parameter modulation
            r = self.chaotic_params[i]
            x_0 = (x[i] + 5.0) / 10.0  # Normalize to [0,1]
            x_prev = x_0
            for _ in range(10):  # Iterate to reach chaotic regime
                x_prev = r * x_prev * (1 - x_prev)
            chaotic_term += x_prev * np.sin(2 * np.pi * x[i])
        f_value += 0.8 * chaotic_term
        
        # Multi-scale sinusoidal components with chaotic modulation
        for i in range(self.dim):
            f_value += 0.5 * np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.sin(20 * x[i])
            
        # Polynomial interactions with chaotic coefficients
        for i in range(self.dim):
            f_value += 0.3 * x[i]**9 * np.sin(x[i] * self.chaotic_params[i])
            
        # Cross-variable chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction using logistic map
                r1 = self.chaotic_params[i]
                r2 = self.chaotic_params[j]
                x1_0 = (x[i] + 5.0) / 10.0
                x2_0 = (x[j] + 5.0) / 10.0
                x1_prev = x1_0
                x2_prev = x2_0
                for _ in range(5):
                    x1_prev = r1 * x1_prev * (1 - x1_prev)
                    x2_prev = r2 * x2_prev * (1 - x2_prev)
                f_value += 0.4 * x1_prev * x2_prev * np.sin(5 * x[i] + 3 * x[j])
                
        # High-frequency chaotic sinusoidal terms
        f_value += 0.6 * np.sum(np.sin(50 * x) * np.cos(40 * x) * np.sin(30 * x))
        
        # Polynomial chaos with sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.25 * x[i]**10 * np.cos(x[i] * self.chaotic_params[i])
            
        # Saddle point enhancement
        for i in range(self.dim):
            f_value += 0.3 * x[i]**4 * np.sin(2 * x[i]) * np.cos(3 * x[i])
            
        # Multi-modal chaotic structure
        f_value += 0.4 * np.sum(np.sin(25 * x) * np.cos(20 * x) * np.sin(15 * x))
        
        # Cross-variable chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.35 * np.sin(12 * x[i]) * np.cos(18 * x[j]) * np.sin(10 * x[i] + 8 * x[j]) * np.cos(6 * x[i] - 4 * x[j])
                
        # Enhanced chaotic polynomial interactions
        for i in range(self.dim):
            f_value += 0.2 * x[i]**11 * np.sin(2 * x[i] * self.chaotic_params[i])
            
        # Add chaotic noise
        noise = np.random.uniform(-0.1, 0.1, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        return f_value