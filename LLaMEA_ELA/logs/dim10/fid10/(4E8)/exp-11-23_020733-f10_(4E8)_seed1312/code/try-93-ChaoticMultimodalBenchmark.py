import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic base with condition number variation
        result = 0.5 * np.sum(x**2)
        
        # Add chaotic sine-cosine components with logistic map modulation
        for i in range(self.dim):
            # Logistic map for dynamic frequency modulation
            freq_mod = 1.0 + 0.5 * (np.sin(3.14159 * i) + np.cos(2.718 * i))
            freq = 2.0 + 0.8 * freq_mod
            amp = 1.2 + 0.3 * np.sin(i * 0.5)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Add radial basis function components with chaotic centers
        for i in range(self.dim):
            center = 2.0 * np.sin(1.5 * i) + 1.0 * np.cos(0.7 * i)
            sigma = 0.5 + 0.2 * np.sin(i * 0.3)
            result += 0.8 * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Add asymmetric saddle points with chaotic steepness
        for i in range(self.dim):
            steepness = 0.1 + 0.05 * np.sin(i * 1.3) + 0.03 * np.cos(i * 0.8)
            result += steepness * (x[i]**3 + 0.3 * x[i]**4 + 0.1 * np.sin(7 * x[i]))
        
        # Add cross-dimensional coupling with chaotic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.2 + 0.1 * np.sin(i * j * 0.5) + 0.05 * np.cos(i + j)
                coupling = weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                result += coupling
        
        # Introduce fractal-like noise with chaotic scaling
        noise = 0.05 * np.sum(np.sin(15 * x) + np.cos(11 * x) + np.tan(6 * x))
        result += noise
        
        # Apply boundary penalty for points near [-5, 5]
        penalty = 0.0
        for i in range(self.dim):
            if x[i] <= -4.8 or x[i] >= 4.8:
                penalty += 10.0 * (5.0 - abs(x[i]))**2
        result += penalty
        
        # Apply global scaling factor to control difficulty
        result *= 1.25
        
        # Add a new chaotic modulation term to increase landscape complexity
        chaos_factor = 0.01 * np.sum(np.sin(7 * x) * np.cos(5 * x) + np.tan(3 * x))
        result += chaos_factor
        
        # Introduce a modified conditioning term for better gradient behavior
        condition_term = 0.05 * np.sum((x**2) * (1.0 + 0.1 * np.sin(2.0 * x)))
        result += condition_term
        
        return result