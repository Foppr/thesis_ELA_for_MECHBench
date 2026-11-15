import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with modified frequencies and exponential damping
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.tan(0.3 * x[i]) * 
                       np.exp(-0.03 * x[i]**2) * np.sin(0.15 * x[i]**3))
        
        # Higher-order saddle point structure with modified quartic and quintic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2.5 * x[i]**2 + 1.5 * x[i]) * np.cos(0.4 * x[i])
        
        # Complex cross-term interactions with adjusted polynomial degrees and trigonometric coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.3 * x[i] * x[j] * (x[i]**2 + x[j]**2) * np.cos(0.3 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic interference term with modified trigonometric and polynomial components
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced interaction range for complexity control
                interference += 0.15 * np.sin(1.5 * x[i] + 2.5 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.08 * (x[i] - x[j])**2)
        
        return quadratic + chaotic + saddle + cross + interference