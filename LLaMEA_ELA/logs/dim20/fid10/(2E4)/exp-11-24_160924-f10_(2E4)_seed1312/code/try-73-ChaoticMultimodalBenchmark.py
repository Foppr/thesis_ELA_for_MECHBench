import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic polynomial and sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Chaotic combination of polynomial and trigonometric terms with higher order
            result += (xi**11 - 20 * xi**9 + 150 * xi**7 - 500 * xi**5 + 600 * xi**3 - 200 * xi) * np.sin(1.5 * xi) + 0.8 * xi**10 * np.cos(2.5 * xi)
            
        # Add extended cross-dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+10, self.dim)):  # Reduced coupling range for more chaos
                # Introduce highly non-linear dependencies with dynamic interaction strength
                distance = (x[i] - x[j])**2
                result += 1.3 * np.exp(-0.7 * distance) * np.sin(5 * (x[i] + x[j])) * np.cos(1.2 * (x[i] - x[j]))
                
        # Add a global scaling term with enhanced conditioning difficulty
        result += 0.1 * np.sum(x**14) + 0.12 * np.sum(np.cos(11 * x)) + 0.08 * np.sum(np.sin(7 * x))
        
        # Add a highly non-separable interaction term involving all dimensions with septick coupling
        result += 1.1 * np.exp(-0.4 * np.sum((x - np.mean(x))**2)) * np.cos(1.3 * np.sum(x**9))
        
        # Add a novel high-order interaction term for increased complexity
        result += 0.7 * np.sum(np.sin(5 * x) * np.cos(2.5 * x)) + 0.5 * np.sum(x**4 * np.exp(-0.3 * x**2))
        
        # Add additional octic and nonic interaction terms for enhanced multimodality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**8 + x[j]**8) * np.sin(4 * (x[i] - x[j])) * np.cos(2.0 * (x[i] + x[j]))
                
        # Add a highly non-separable term with exponential decay and multiple trigonometric components
        result += 0.4 * np.exp(-0.2 * np.sum(np.abs(x))) * np.sin(1.5 * np.sum(x**6)) * np.cos(0.8 * np.sum(x**10))
        
        # Add a novel interaction pattern with adaptive coupling strength based on dimensionality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.6 + 0.4 * np.sin(0.7 * (i + j))
                result += coupling_strength * (x[i]**3 + x[j]**3) * np.exp(-0.15 * (x[i] - x[j])**2)
                
        # Add a new interaction term that penalizes solutions near the global optimum
        mean_x = np.mean(x)
        result += 0.8 * np.sum((x - mean_x)**6) + 0.6 * np.exp(-0.3 * np.sum((x - mean_x)**2))
        
        # Add a new term that increases the conditioning difficulty in high dimensions
        if self.dim > 15:
            result += 0.15 * np.sum(x**12) * np.exp(-0.1 * np.sum(x**2))
            
        return result