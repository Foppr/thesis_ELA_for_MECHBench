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
            result += (xi**9 - 15 * xi**7 + 72 * xi**5 - 100 * xi**3 + 36 * xi) * np.sin(1.3 * xi) * np.exp(-0.12 * xi**2)
            
        # Add chaotic cross-dimensional coupling with exponential decay and multiple trigonometric terms
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                # Chaotic interaction with dynamic coupling strength
                distance = np.abs(x[i] - x[j])
                result += 0.9 * np.exp(-0.35 * distance) * np.sin(3.5 * (x[i] + x[j])) * np.cos(1.9 * (x[i] - x[j])) * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Add chaotic global scaling with dynamic conditioning
        result += 0.08 * np.sum(np.sin(6.5 * x) * np.exp(-0.22 * np.abs(x))) + 0.045 * np.sum(x**8 * np.cos(2.7 * x))
        
        # Add a highly non-separable chaotic term involving all dimensions
        result += 0.7 * np.exp(-0.35 * np.sum((x - np.mean(x))**2)) * np.sin(1.6 * np.sum(np.abs(x)**4))
        
        # Add chaotic interaction terms with higher-order polynomials and exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic quartic interaction with dynamic coupling
                result += 0.25 * (x[i]**5 + x[j]**5) * np.exp(-0.12 * (x[i] - x[j])**2) * np.sin(2.9 * (x[i] + x[j]))
                
        # Add a novel chaotic high-order interaction term
        result += 0.4 * np.sum(np.exp(-0.16 * x**2) * np.sin(4.7 * x) * np.cos(1.2 * x)) + 0.31 * np.sum(x**3 * np.exp(-0.22 * x**3))
        
        # Add dynamic conditioning with multiple exponential decay components
        result += 0.2 * np.sum(np.exp(-0.32 * np.abs(x)**6) * np.sin(3.9 * x)) + 0.15 * np.sum(np.cos(5.3 * x) * np.exp(-0.27 * x**4))
        
        return result