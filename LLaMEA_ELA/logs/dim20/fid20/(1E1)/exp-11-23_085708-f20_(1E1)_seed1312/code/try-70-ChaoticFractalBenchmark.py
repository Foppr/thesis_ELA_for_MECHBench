import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.5
        self.c = 0.1
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractal-like component using chaotic logistic map
        fractal_term = 0.0
        for i in range(self.dim):
            # Use previous dimension values to create chaotic dependency
            chaotic_val = 0.0
            if i > 0:
                chaotic_val = self.a * x_scaled[i-1] * (1 - x_scaled[i-1])
            else:
                chaotic_val = self.a * 0.5 * (1 - 0.5)
                
            # Inject fractal structure through recursive scaling
            fractal_term += np.sin(2 * np.pi * chaotic_val * (i + 1)) * np.cos(np.pi * x_scaled[i] * (i + 1))
        
        # Saddle point component with dynamic weights based on dimension
        saddle_term = 0.0
        for i in range(self.dim):
            # Create saddle points using multi-dimensional interaction
            saddle_term += (x_scaled[i]**2 - self.b * np.sin(3 * x_scaled[i])) * (i + 1)
            
        # Dynamic noise injection that varies with dimensionality
        noise = 0.0
        for i in range(self.dim):
            # Use a pseudo-random sequence based on dimension and value
            seed = int((x_scaled[i] * 1000 + i) % 1000)
            np.random.seed(seed)
            local_noise = np.random.normal(0, 0.1)
            noise += local_noise * (i + 1) * np.cos(x_scaled[i])
            
        # Interaction terms with exponential decay
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                interaction_term += np.exp(-dist) * np.sin(2 * np.pi * (i + j)) * (i + j)
                
        # Multi-scale periodic component
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(5 * x_scaled[i]) * np.cos(7 * x_scaled[i]) * np.sin(3 * x_scaled[i])
            
        # Global scaling and offset to ensure positive fitness values
        result = fractal_term + saddle_term + noise + interaction_term + periodic_term
        
        # Add a global minimum at origin with dynamic scaling
        global_min = 0.1 * (np.sum(x_scaled**2) + 0.5 * np.sum(np.sin(5 * x_scaled)**2))
        
        return result + global_min + 5.0