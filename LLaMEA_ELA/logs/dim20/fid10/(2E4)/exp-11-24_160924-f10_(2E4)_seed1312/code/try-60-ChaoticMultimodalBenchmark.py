import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic polynomial and sinusoidal components with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            # Chaotic interaction using exponential and trigonometric combinations
            result += (xi**9 - 15 * xi**7 + 72 * xi**5 - 100 * xi**3 + 36 * xi) * np.sin(1.2 * xi) * np.exp(-0.1 * xi**2)
            
        # Add chaotic cross-dimensional coupling with exponential decay and multiple trigonometric terms
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                # Chaotic interaction with dynamic coupling strength
                distance = np.abs(x[i] - x[j])
                result += 0.85 * np.exp(-0.4 * distance) * np.sin(3.2 * (x[i] + x[j])) * np.cos(1.8 * (x[i] - x[j])) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Add chaotic global scaling with dynamic conditioning
        result += 0.07 * np.sum(np.sin(6.3 * x) * np.exp(-0.2 * np.abs(x))) + 0.04 * np.sum(x**8 * np.cos(2.5 * x))
        
        # Add a highly non-separable chaotic term involving all dimensions
        result += 0.65 * np.exp(-0.3 * np.sum((x - np.mean(x))**2)) * np.sin(1.5 * np.sum(np.abs(x)**4))
        
        # Add chaotic interaction terms with higher-order polynomials and exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic quartic interaction with dynamic coupling
                result += 0.22 * (x[i]**5 + x[j]**5) * np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(2.7 * (x[i] + x[j]))
                
        # Add a novel chaotic high-order interaction term
        result += 0.38 * np.sum(np.exp(-0.15 * x**2) * np.sin(4.5 * x) * np.cos(1.1 * x)) + 0.29 * np.sum(x**3 * np.exp(-0.2 * x**3))
        
        # Add dynamic conditioning with multiple exponential decay components
        result += 0.18 * np.sum(np.exp(-0.3 * np.abs(x)**6) * np.sin(3.7 * x)) + 0.14 * np.sum(np.cos(5.1 * x) * np.exp(-0.25 * x**4))
        
        return result