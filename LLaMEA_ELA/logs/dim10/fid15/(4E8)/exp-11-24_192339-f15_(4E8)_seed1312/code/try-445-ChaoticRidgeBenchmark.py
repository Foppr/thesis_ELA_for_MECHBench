import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperchaotic system parameters
        self.a, self.b, self.c, self.d = 1.4, 0.3, 1.0, 0.5
        # Memory effect parameters
        self.memory_weights = np.random.uniform(0.1, 0.9, dim)
        # Ridge structure parameters
        self.ridge_freqs = np.random.uniform(0.5, 2.0, dim)
        self.ridge_amplitudes = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic dynamics component
        chaotic = 0.0
        # Initialize hyperchaotic state
        x1, x2, x3, x4 = 0.1, 0.1, 0.1, 0.1
        for _ in range(100):  # Iterate to reach chaotic regime
            x1_new = self.a * x1 + x2 * x3 - self.b * x1 * x4
            x2_new = self.c * x2 + x1 * x4 - self.d * x2 * x3
            x3_new = self.d * x3 + x1 * x2 - self.a * x3 * x4
            x4_new = self.b * x4 + x1 * x3 - self.c * x2 * x4
            x1, x2, x3, x4 = x1_new, x2_new, x3_new, x4_new
        
        # Use chaotic state to modulate fitness
        for i in range(self.dim):
            chaotic += (x[i] - x1)**2 + (x[i] - x2)**2
            
        # Adaptive ridge structure
        ridge = 0.0
        for i in range(self.dim):
            # Combine multiple ridge components with dynamic frequencies and amplitudes
            ridge_component = 0.0
            for j in range(3):
                freq = self.ridge_freqs[i] * (j + 1)
                amp = self.ridge_amplitudes[i] * (j + 1)
                ridge_component += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
            ridge += ridge_component
            
        # Memory-dependent fitness modulation
        memory = 0.0
        for i in range(self.dim):
            # Incorporate previous evaluations through weighted averaging
            if i > 0:
                memory += self.memory_weights[i] * (x[i] - x[i-1])**2
                
        # Path-dependent component using cumulative gradient influence
        path = 0.0
        for i in range(1, self.dim):
            grad_influence = np.sin(x[i-1] + x[i]) * np.cos(x[i-1] - x[i])
            path += grad_influence
            
        # Deceptive valley component
        deceptive = 0.0
        for i in range(self.dim):
            # Create a deceptive minimum that is not the global optimum
            deceptive += (x[i] - 1.0)**2 + 0.5 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Combine all components with dynamic weighting based on dimensionality
        total = (0.3 * chaotic + 0.4 * ridge + 0.1 * memory + 
                0.1 * path + 0.1 * deceptive)
        
        return total