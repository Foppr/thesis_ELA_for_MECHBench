import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add polynomial and sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Complex combination of polynomial and trigonometric terms with higher order
            result += (xi**9 - 15 * xi**7 + 80 * xi**5 - 100 * xi**3 + 30 * xi) * np.sin(1.2 * xi) + 0.6 * xi**8 * np.cos(2.0 * xi)
            
        # Add extended cross-dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+15, self.dim)):  # Increased coupling range
                # Introduce highly non-linear dependencies with dynamic interaction strength
                distance = (x[i] - x[j])**2
                result += 1.1 * np.exp(-0.5 * distance) * np.sin(7 * (x[i] + x[j])) * np.cos(0.9 * (x[i] - x[j]))
                
        # Add a global scaling term with enhanced conditioning difficulty
        result += 0.08 * np.sum(x**12) + 0.09 * np.sum(np.cos(9 * x)) + 0.05 * np.sum(np.sin(6 * x))
        
        # Add a highly non-separable interaction term involving all dimensions with quintic coupling
        result += 0.9 * np.exp(-0.3 * np.sum((x - np.mean(x))**2)) * np.cos(1.1 * np.sum(x**7))
        
        # Add a novel high-order interaction term for increased complexity
        result += 0.6 * np.sum(np.sin(4 * x) * np.cos(2.0 * x)) + 0.4 * np.sum(x**3 * np.exp(-0.2 * x**2))
        
        # Add additional sextic and septic interaction terms for enhanced multimodality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * (x[i]**6 + x[j]**6) * np.sin(3 * (x[i] - x[j])) * np.cos(1.5 * (x[i] + x[j]))
                
        # Add a highly non-separable term with exponential decay and multiple trigonometric components
        result += 0.35 * np.exp(-0.15 * np.sum(np.abs(x))) * np.sin(1.2 * np.sum(x**4)) * np.cos(0.6 * np.sum(x**8))
        
        # Add a novel interaction pattern with adaptive coupling strength based on dimensionality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.3 * np.sin(0.5 * (i + j))
                result += coupling_strength * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Add a new interaction term that penalizes solutions near the global optimum
        # This helps improve fitness by increasing the difficulty of converging to good solutions
        mean_x = np.mean(x)
        result += 0.7 * np.sum((x - mean_x)**4) + 0.5 * np.exp(-0.2 * np.sum((x - mean_x)**2))
        
        # Add a new term that increases the conditioning difficulty in high dimensions
        if self.dim > 10:
            result += 0.1 * np.sum(x**10) * np.exp(-0.05 * np.sum(x**2))
            
        return result