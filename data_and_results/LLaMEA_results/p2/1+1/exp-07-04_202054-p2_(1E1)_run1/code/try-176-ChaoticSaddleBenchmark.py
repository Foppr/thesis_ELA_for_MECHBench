import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum
        f_value = np.sum(x**2)
        
        # Chaotic saddle-point components with exponential modulation
        for i in range(self.dim):
            f_value += 0.5 * np.exp(-0.5 * x[i]**2) * np.sin(10 * x[i]) * np.cos(8 * x[i])
            
        # Nested oscillatory patterns with varying frequencies and amplitudes
        for i in range(self.dim):
            f_value += 0.3 * np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.sin(20 * x[i]) * np.cos(18 * x[i])
            
        # Asymmetric gradient field with directional preference
        for i in range(self.dim):
            f_value += 0.4 * x[i]**3 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Multi-scale chaotic interactions with fractal-like behavior
        for i in range(self.dim):
            f_value += 0.25 * np.sin(25 * x[i]) * np.cos(22 * x[i]) * np.sin(28 * x[i]) * np.cos(26 * x[i]) * np.sin(30 * x[i])
            
        # Cross-variable chaotic coupling with non-linear interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.35 * np.sin(6 * x[i]) * np.cos(9 * x[j]) * np.sin(7 * x[i] + 3 * x[j]) * np.cos(5 * x[i] - 2 * x[j]) * np.sin(8 * x[i] + 4 * x[j])
                
        # Fractal-like high-order polynomial with chaotic modulation
        for i in range(self.dim):
            f_value += 0.2 * x[i]**9 * np.sin(4 * x[i]) * np.cos(6 * x[i])
            
        # Asymmetric multi-modal components with irregular peaks
        for i in range(self.dim):
            f_value += 0.3 * np.sin(35 * x[i]) * np.cos(32 * x[i]) * np.sin(38 * x[i]) * np.cos(36 * x[i]) * np.sin(40 * x[i])
            
        # Enhanced cross-variable coupling with chaotic behavior
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.4 * np.sin(11 * x[i]) * np.cos(14 * x[j]) * np.sin(13 * x[i] + 6 * x[j]) * np.cos(9 * x[i] - 5 * x[j]) * np.sin(15 * x[i] + 4 * x[j]) * np.cos(12 * x[i] - 3 * x[j])
                
        # Slight modification: add chaotic modulation to the highest-order polynomial
        for i in range(self.dim):
            f_value += 0.25 * x[i]**10 * np.sin(7 * x[i]) * np.cos(5 * x[i])
            
        # Add noise to increase irregularity
        noise = np.random.normal(0, 0.1, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        # Add irregular bumps for additional challenge
        for i in range(self.dim):
            f_value += 0.15 * np.sin(60 * x[i]) * np.cos(45 * x[i]) * np.sin(50 * x[i])
            
        # Add a new component to improve fitness score: asymmetric chaotic oscillations
        f_value += 0.2 * np.sum(np.sin(40 * x) * np.cos(35 * x) * np.sin(45 * x) * np.cos(42 * x))
        
        # Add a new component to improve fitness score: enhanced cross-variable chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.sin(16 * x[i]) * np.cos(19 * x[j]) * np.sin(18 * x[i] + 7 * x[j]) * np.cos(13 * x[i] - 6 * x[j]) * np.sin(20 * x[i] + 5 * x[j]) * np.cos(17 * x[i] - 4 * x[j])
                
        # Add a new component to improve fitness score: higher-order chaotic polynomial
        for i in range(self.dim):
            f_value += 0.3 * x[i]**11 * np.sin(8 * x[i]) * np.cos(7 * x[i])
            
        # Add a new component: increased complexity in cross-variable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.25 * np.sin(22 * x[i]) * np.cos(25 * x[j]) * np.sin(24 * x[i] + 9 * x[j]) * np.cos(18 * x[i] - 8 * x[j]) * np.sin(26 * x[i] + 7 * x[j]) * np.cos(23 * x[i] - 5 * x[j])
                
        # Add a new component: modified chaotic sinusoidal modulation
        f_value += 0.2 * np.sum(np.sin(50 * x)**4 + np.cos(40 * x)**4)
        
        return f_value