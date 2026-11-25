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
            # Enhanced chaotic interaction using exponential and trigonometric combinations
            result += (xi**10 - 18 * xi**8 + 95 * xi**6 - 150 * xi**4 + 70 * xi**2) * np.sin(1.3 * xi) * np.exp(-0.12 * xi**2)
            
        # Add chaotic cross-dimensional coupling with exponential decay and multiple trigonometric terms
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                # Enhanced chaotic interaction with dynamic coupling strength
                distance = np.abs(x[i] - x[j])
                result += 0.95 * np.exp(-0.35 * distance) * np.sin(3.5 * (x[i] + x[j])) * np.cos(2.0 * (x[i] - x[j])) * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Add chaotic global scaling with dynamic conditioning
        result += 0.08 * np.sum(np.sin(6.5 * x) * np.exp(-0.22 * np.abs(x))) + 0.05 * np.sum(x**9 * np.cos(2.7 * x))
        
        # Add a highly non-separable chaotic term involving all dimensions
        result += 0.75 * np.exp(-0.35 * np.sum((x - np.mean(x))**2)) * np.sin(1.7 * np.sum(np.abs(x)**5))
        
        # Add enhanced chaotic interaction terms with higher-order polynomials and exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced quartic interaction with dynamic coupling - increased complexity
                result += 0.28 * (x[i]**5 + x[j]**5) * np.exp(-0.15 * (x[i] - x[j])**2) * np.sin(3.0 * (x[i] + x[j]))
                
        # Add a novel chaotic high-order interaction term with improved balance
        result += 0.42 * np.sum(np.exp(-0.18 * x**2) * np.sin(4.8 * x) * np.cos(1.3 * x)) + 0.32 * np.sum(x**4 * np.exp(-0.25 * x**4))
        
        # Add enhanced dynamic conditioning with multiple exponential decay components
        result += 0.22 * np.sum(np.exp(-0.35 * np.abs(x)**6) * np.sin(4.0 * x)) + 0.18 * np.sum(np.cos(5.5 * x) * np.exp(-0.3 * x**4))
        
        # Add a new term to improve fitness score and algorithm challenge
        result += 0.30 * np.sum(np.sin(2.2 * x)**2 * np.exp(-0.12 * x**2)) + 0.18 * np.sum(x**7 * np.sin(1.7 * x))
        
        # Add additional chaotic complexity with modified coupling
        for i in range(self.dim):
            result += 0.15 * np.sin(3.0 * x[i]) * np.exp(-0.2 * x[i]**3) * np.cos(1.5 * x[i])
            
        return result