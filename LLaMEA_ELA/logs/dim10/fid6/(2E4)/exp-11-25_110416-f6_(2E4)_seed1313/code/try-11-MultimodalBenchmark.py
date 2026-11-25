import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.2 * np.sin(13 * x[i]) * np.cos(9 * x[i]) * np.sin(5 * x[i])
            
        # Add multiple global minima with different shifted polynomial penalties
        for i in range(self.dim):
            result += 0.01 * (x[i] - 2.0)**6 + 0.005 * (x[i] + 3.0)**8 + 0.002 * (x[i] - 1.0)**10
            
        # Add cross-dimensional chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for complexity control
                result += 0.05 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(4 * x[i] - x[j])
                
        # Add a complex interaction term that creates many local minima
        interaction_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_sum += np.sin(x[i] * x[j]) / (1 + abs(x[i] - x[j]))
        result += 0.02 * interaction_sum
        
        # Add a highly oscillatory component to increase landscape complexity
        for i in range(self.dim):
            result += 0.15 * np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.sin(8 * x[i])
            
        return result