import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum at origin
        result = np.sum(x**2)
        
        # Add multiple local minima using higher frequency sinusoidal terms with chaotic modulation
        for i in range(self.dim):
            result += 0.6 * np.sin(18 * x[i]) * np.cos(12 * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Add coupling between variables with more complex interaction and chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.07 * np.sin(x[i]**2 + x[j]**2) * np.cos(x[i] * x[j]) * np.exp(-0.07 * (x[i]**2 + x[j]**2))
                
        # Add a fourth-order polynomial term to increase landscape complexity with chaotic modulation
        for i in range(self.dim):
            result += 0.15 * x[i]**4 * np.sin(8 * x[i])
            
        # Add cross-terms with different frequencies and chaotic modulation to create more intricate structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * np.sin(6 * x[i]) * np.cos(10 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Add a fifth-order term with chaotic modulation
        for i in range(self.dim):
            result += 0.07 * x[i]**5 * np.cos(5 * x[i])
            
        # Add a sixth-order term with chaotic modulation
        for i in range(self.dim):
            result += 0.04 * x[i]**6 * np.sin(7 * x[i])
            
        # Add a seventh-order term for even more complexity and chaotic behavior
        for i in range(self.dim):
            result += 0.03 * x[i]**7 * np.exp(-0.03 * x[i]**2)
            
        # Add a highly oscillatory component to increase the number of local minima
        for i in range(self.dim):
            result += 0.2 * np.sin(35 * x[i]) * np.cos(25 * x[i]) * np.tanh(x[i])
            
        return result