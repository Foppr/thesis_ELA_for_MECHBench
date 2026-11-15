import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum
        f_value = np.sum(x**2)
        
        # Chaotic saddle-point structure with nested sinusoidal potentials
        for i in range(self.dim):
            f_value += 0.5 * np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.sin(20 * x[i])
            
        # Asymmetric gradient field with polynomial modulation
        for i in range(self.dim):
            f_value += 0.3 * x[i]**5 * np.sin(8 * x[i]) * np.cos(6 * x[i])
            
        # Nested periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_value += 0.4 * np.sin(25 * x[i]) * np.cos(30 * x[i]) * np.sin(35 * x[i]) * np.cos(40 * x[i])
            
        # Multi-scale chaotic interactions with exponential modulation
        for i in range(self.dim):
            f_value += 0.25 * np.exp(-x[i]**2) * np.sin(50 * x[i]) * np.cos(45 * x[i])
            
        # Cross-variable chaotic coupling with asymmetric interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.35 * np.sin(12 * x[i]) * np.cos(18 * x[j]) * np.sin(22 * x[i] + 10 * x[j]) * np.exp(-0.5 * (x[i] - x[j])**2)
                
        # Higher-order chaotic polynomial with sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.4 * x[i]**9 * np.sin(7 * x[i]) * np.cos(9 * x[i])
            
        # Nested multi-modal structure with varying scales
        f_value += 0.3 * np.sum(np.sin(40 * x) * np.cos(35 * x) * np.sin(50 * x))
        
        # Asymmetric cross-term interactions with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.2 * np.sin(15 * x[i]) * np.cos(20 * x[j]) * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(10 * x[i] + 5 * x[j])
                
        # Additional chaotic component with irregular frequency modulation
        f_value += 0.2 * np.sum(np.sin(60 * x) * np.cos(55 * x) * np.sin(65 * x) * np.cos(70 * x))
        
        # Polynomial chaos with asymmetric gradient
        for i in range(self.dim):
            f_value += 0.3 * x[i]**11 * np.sin(5 * x[i]) * np.cos(4 * x[i])
            
        # Multi-scale chaotic interaction with varying amplitudes
        for i in range(self.dim):
            f_value += 0.2 * np.exp(-0.1 * x[i]**2) * np.sin(30 * x[i]) * np.cos(25 * x[i]) * np.sin(35 * x[i])
            
        # Enhanced cross-variable chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.sin(20 * x[i]) * np.cos(25 * x[j]) * np.exp(-0.2 * (x[i] + x[j])**2) * np.sin(15 * x[i] - 10 * x[j])
                
        # Final chaotic modulation with complex multi-scale structure
        f_value += 0.25 * np.sum(np.sin(70 * x)**2 * np.cos(60 * x)**2 * np.sin(80 * x)**2)
        
        return f_value