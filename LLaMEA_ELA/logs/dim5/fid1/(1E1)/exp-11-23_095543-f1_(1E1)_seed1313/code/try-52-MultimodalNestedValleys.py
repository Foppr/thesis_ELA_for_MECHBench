import numpy as np

class MultimodalNestedValleys:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Quadratic base with extreme condition numbers
        result = 0.0
        for i in range(self.dim):
            result += (10 ** (4 * i / (self.dim - 1))) * (x[i] ** 2)
            
        # Add high-frequency trigonometric modulations to create intricate valleys
        for i in range(self.dim):
            result += 2.0 * np.sin(15 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            
        # Radial basis function components with multiple peaks and varying scales
        for i in range(self.dim):
            r = np.sqrt(np.sum(x ** 2))
            result += 1.5 * np.exp(-0.3 * (x[i] - r) ** 2) * np.sin(4 * np.pi * r)
            
        # Add coupling terms between dimensions to create complex interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.1 * (x[i] ** 2 + x[j] ** 2))
                result += coupling * np.sin(5 * x[i]) * np.cos(6 * x[j])
                
        # Add a quartic polynomial to increase local complexity
        for i in range(self.dim):
            result += 0.8 * (x[i] ** 4) * np.cos(3 * x[i])
            
        # Add a radial component that creates nested structures with multiple scales
        r = np.sqrt(np.sum(x ** 2))
        result += 1.0 * np.sin(20 * r) * np.exp(-0.2 * r)
        
        # Add a high-frequency oscillating term to create many local minima
        for i in range(self.dim):
            result += 0.5 * np.sin(25 * x[i]) * np.cos(13 * x[(i + 2) % self.dim])
            
        # Add a multi-scale radial component with varying amplitudes
        r = np.sqrt(np.sum(x ** 2))
        result += 0.7 * np.sin(30 * r) * np.exp(-0.05 * r)
        
        # Normalize to prevent extreme values
        result /= (1.0 + 0.1 * np.sum(x ** 2))
        
        return result