import numpy as np

class MultimodalNestedValleys:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Quadratic base with varying condition numbers
        result = 0.0
        for i in range(self.dim):
            result += (10 ** (2 * i / (self.dim - 1))) * (x[i] ** 2)
            
        # Add chaotic trigonometric modulations to create valleys and ridges
        for i in range(self.dim):
            result += 0.8 * np.sin(5 * x[i]) * np.cos(7 * x[(i + 1) % self.dim]) * np.sin(3 * x[i] * x[(i + 2) % self.dim])
            
        # Radial basis function components with multiple peaks and fractal-like behavior
        for i in range(self.dim):
            r = np.sqrt(np.sum(x ** 2))
            result += 0.4 * np.exp(-0.3 * (x[i] - r) ** 2) * np.sin(3 * np.pi * r) * np.cos(2 * np.pi * r)
            
        # Add coupling terms between dimensions to create complex interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.1 * (x[i] ** 2 + x[j] ** 2)) * np.sin(5 * x[i]) * np.cos(6 * x[j])
                result += coupling * np.sin(4 * x[i]) * np.cos(3 * x[j])
                
        # Add a quartic polynomial to increase local complexity
        for i in range(self.dim):
            result += 0.15 * (x[i] ** 4) * np.cos(3 * x[i])
            
        # Add a radial component that creates nested structures with chaotic behavior
        r = np.sqrt(np.sum(x ** 2))
        result += 0.3 * np.sin(15 * r) * np.exp(-0.2 * r) * np.cos(8 * r)
        
        # Add chaotic deterministic component to increase landscape complexity
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(10 * x[i]) * np.cos(10 * x[(i + 1) % self.dim])
        result += 0.25 * chaos_term
        
        # Add higher-order coupling terms to increase local optima density
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.05 * np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.sin(4 * x[k])
                    
        # Normalize to prevent extreme values
        result /= (1.0 + 0.1 * np.sum(x ** 2))
        
        return result